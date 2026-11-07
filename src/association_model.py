"""Modelo descritivo para a relação entre registros RAND e homicídios."""

import numpy as np
import pandas as pd
from scipy.stats import t as student_t


def fit_within_state(panel):
    """OLS com regras/economia do ano anterior e efeitos fixos estado/ano.

    O coeficiente mede associação condicional, não impacto causal.
    """
    required = {"state", "year", "homicide_rate", "restrictive_records",
                "permissive_records", "unemployment_rate", "income_per_capita"}
    missing = required - set(panel.columns)
    if missing:
        raise ValueError(f"Colunas ausentes: {sorted(missing)}")
    if panel.duplicated(["state", "year"]).any() or panel[list(required)].isna().any().any():
        raise ValueError("Painel com chaves duplicadas ou valores ausentes")

    data = panel.sort_values(["state", "year"]).reset_index(drop=True)
    if not data.groupby("state")["year"].diff().dropna().eq(1).all():
        raise ValueError("Anos não consecutivos dentro de um estado")
    previous = data.groupby("state")[["restrictive_records", "permissive_records",
                                      "unemployment_rate", "income_per_capita"]].shift(1)
    previous.columns = ["restrictive_previous_year", "permissive_previous_year",
                        "unemployment_previous_year", "income_previous_year_10k"]
    data = pd.concat([data, previous], axis=1).dropna(subset=previous.columns).reset_index(drop=True)
    core = data[list(previous.columns)].astype(float)
    core["income_previous_year_10k"] /= 10000
    dummies = pd.concat([
        pd.get_dummies(data["state"], prefix="state", drop_first=True, dtype=float),
        pd.get_dummies(data["year"], prefix="year", drop_first=True, dtype=float),
    ], axis=1)
    x = np.column_stack([np.ones(len(data)), core.to_numpy(), dummies.to_numpy()])
    y = data["homicide_rate"].to_numpy(dtype=float)
    n, k = x.shape
    if np.linalg.matrix_rank(x) != k:
        raise ValueError("Sem variação suficiente para estimar o modelo")
    beta = np.linalg.lstsq(x, y, rcond=None)[0]
    residual = y - x @ beta
    inverse = np.linalg.inv(x.T @ x)
    meat = np.zeros((k, k))
    for state in data["state"].unique():
        mask = data["state"].eq(state).to_numpy()
        score = x[mask].T @ residual[mask]
        meat += np.outer(score, score)
    groups = data["state"].nunique()
    correction = groups / (groups - 1) * (n - 1) / (n - k)
    covariance = correction * inverse @ meat @ inverse
    se = np.sqrt(np.maximum(np.diag(covariance), 0))
    critical = student_t.ppf(0.975, df=groups - 1)
    names = ["intercept", *core.columns, *dummies.columns]
    result = pd.DataFrame({"term": names, "estimate": beta, "se_cluster": se})
    result["ci_low"] = result["estimate"] - critical * result["se_cluster"]
    result["ci_high"] = result["estimate"] + critical * result["se_cluster"]
    return result[result["term"].isin(core.columns)].reset_index(drop=True)

"""Preparação da base estado-ano para a pergunta principal da AV2."""

import pandas as pd


YEARS = range(2019, 2025)


def _dates(table, prefix):
    parts = table[[f"{prefix} Year", f"{prefix} Month", f"{prefix} Day"]].copy()
    parts.columns = ["year", "month", "day"]
    return pd.to_datetime(parts, errors="coerce")


def count_rand_records(laws, states, years=YEARS):
    """Conta registros substantivos vigentes em 31/12, por estado e ano.

    Cada Law ID é um registro da RAND, não necessariamente uma lei distinta.
    Repeal e See note são eventos/notas, e não regras vigentes para esta medida.
    """
    required = {
        "Law ID", "State", "Type of Change", "Effect",
        "Effective Date Year", "Effective Date Month", "Effective Date Day",
        "Supersession Date Year", "Supersession Date Month", "Supersession Date Day",
    }
    missing = required - set(laws.columns)
    if missing:
        raise ValueError(f"Colunas RAND ausentes: {sorted(missing)}")
    if laws["Law ID"].duplicated().any():
        raise ValueError("Law ID duplicado na base RAND")

    selected = laws[laws["Type of Change"].isin(["Implement", "Modify"])].copy()
    selected = selected[selected["State"].isin(states)]
    if not selected["Effect"].isin(["Restrictive", "Permissive"]).all():
        raise ValueError("Há registros RAND sem classificação de efeito conhecida")
    selected["start"] = _dates(selected, "Effective Date")
    selected["end"] = _dates(selected, "Supersession Date")
    if selected["start"].isna().any():
        raise ValueError("Há registros RAND sem data inicial válida")
    if selected["Supersession Date Year"].notna().sum() != selected["end"].notna().sum():
        raise ValueError("Há registros RAND com data de substituição incompleta")

    rows = []
    for year in years:
        cutoff = pd.Timestamp(year=year, month=12, day=31)
        active = selected[(selected["start"] <= cutoff) &
                          (selected["end"].isna() | (selected["end"] > cutoff))]
        counts = active.groupby(["State", "Effect"])["Law ID"].nunique().unstack(fill_value=0)
        for state in sorted(states):
            restrictive = int(counts.loc[state, "Restrictive"]) if state in counts.index and "Restrictive" in counts else 0
            permissive = int(counts.loc[state, "Permissive"]) if state in counts.index and "Permissive" in counts else 0
            rows.append({"state": state, "year": year,
                         "restrictive_records": restrictive,
                         "permissive_records": permissive,
                         "total_law_records": restrictive + permissive})
    return pd.DataFrame(rows).sort_values(["state", "year"]).reset_index(drop=True)


def build_association_table(cdc, counts):
    """Une CDC e RAND pelo mesmo estado e ano; não cria alvo futuro."""
    homicide = cdc[cdc["name"] != "District of Columbia"].rename(
        columns={"name": "state", "period": "year", "rate": "homicide_rate",
                 "count_sup": "homicide_count"})
    homicide = homicide[["state", "year", "homicide_rate", "homicide_count"]].copy()
    homicide["year"] = homicide["year"].astype(int)
    result = homicide.merge(counts, on=["state", "year"], how="inner", validate="one_to_one")
    result = result.sort_values(["state", "year"]).reset_index(drop=True)
    if len(result) != 300 or result["state"].nunique() != 50:
        raise ValueError(f"Cobertura inesperada: {len(result)} linhas e {result['state'].nunique()} estados")
    if result.isna().any().any():
        raise ValueError("Há valores ausentes na base integrada")
    if not (result["total_law_records"] == result["restrictive_records"] + result["permissive_records"]).all():
        raise ValueError("Contagem RAND inconsistente")
    return result


def build_policy_panel(cdc, counts, ccw, background, unemployment, income):
    """Integra as quatro fontes do projeto por estado e mesmo ano."""
    result = build_association_table(cdc, counts)
    for other in (ccw, background, unemployment, income):
        result = result.merge(other, on=["state", "year"], how="inner", validate="one_to_one")
    result = result.sort_values(["state", "year"]).reset_index(drop=True)
    if len(result) != 300 or result["state"].nunique() != 50:
        raise ValueError("Cobertura incompleta após integrar as quatro fontes")
    if result.isna().any().any():
        raise ValueError("Há valores ausentes no painel completo")
    return result

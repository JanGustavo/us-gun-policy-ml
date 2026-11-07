import unittest

import numpy as np
import pandas as pd

from src.association_model import fit_within_state


class AssociationModelTests(unittest.TestCase):
    def test_current_year_law_count_does_not_enter_current_year_outcome(self):
        rng = np.random.default_rng(8)
        rows = []
        for state in range(50):
            for year in range(2019, 2025):
                rows.append({
                    "state": f"State {state}", "year": year,
                    "homicide_rate": 5 + state / 20 + (year - 2019) / 10 + rng.normal(0, 0.2),
                    "restrictive_records": state % 5 + (year - 2019) * (state % 3),
                    "permissive_records": state % 4 + ((year - 2019) // 2) * (state % 2),
                    "unemployment_rate": 3 + rng.normal(0, 0.5),
                    "income_per_capita": 40000 + 200 * state + 500 * (year - 2019) + rng.normal(0, 100),
                })
        panel = pd.DataFrame(rows)
        before = fit_within_state(panel)
        panel.loc[panel.year.eq(2024), "restrictive_records"] += 100
        after = fit_within_state(panel)
        np.testing.assert_allclose(before["estimate"], after["estimate"])


if __name__ == "__main__":
    unittest.main()

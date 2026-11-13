import unittest

import pandas as pd

from src.association_data import build_association_table, build_policy_panel, count_rand_records


class AssociationDataTests(unittest.TestCase):
    def test_count_uses_full_dates_and_excludes_repeals_and_notes(self):
        laws = pd.DataFrame([
            ["A", "Alabama", "Implement", "Restrictive", 2019, 1, 1, 2021, 12, 31],
            ["B", "Alabama", "Modify", "Permissive", 2021, 12, 31, None, None, None],
            ["C", "Alabama", "Repeal", "Restrictive", 2020, 1, 1, None, None, None],
            ["D", "Alabama", "See note", "Restrictive", 2019, 1, 1, None, None, None],
        ], columns=["Law ID", "State", "Type of Change", "Effect",
                    "Effective Date Year", "Effective Date Month", "Effective Date Day",
                    "Supersession Date Year", "Supersession Date Month", "Supersession Date Day"])
        result = count_rand_records(laws, {"Alabama"}, years=range(2020, 2023)).set_index("year")
        self.assertEqual(result.loc[2020, "total_law_records"], 1)
        self.assertEqual(result.loc[2021, "restrictive_records"], 0)
        self.assertEqual(result.loc[2021, "permissive_records"], 1)
        self.assertEqual(result.loc[2022, "total_law_records"], 1)

    def test_count_accepts_other_cutoff_day(self):
        laws = pd.DataFrame([
            ["A", "Alabama", "Implement", "Restrictive", 2020, 3, 1, 2020, 9, 1],
            ["B", "Alabama", "Modify", "Restrictive", 2020, 9, 1, None, None, None],
            ["C", "Alabama", "Implement", "Permissive", 2020, 8, 15, None, None, None],
        ], columns=["Law ID", "State", "Type of Change", "Effect",
                    "Effective Date Year", "Effective Date Month", "Effective Date Day",
                    "Supersession Date Year", "Supersession Date Month", "Supersession Date Day"])
        meio = count_rand_records(laws, {"Alabama"}, years=[2020], month=7, day=1).iloc[0]
        fim = count_rand_records(laws, {"Alabama"}, years=[2020]).iloc[0]
        self.assertEqual((meio["restrictive_records"], meio["permissive_records"]), (1, 0))
        self.assertEqual((fim["restrictive_records"], fim["permissive_records"]), (1, 1))

    def test_integration_rejects_lost_state_years(self):
        rows = [(f"State {i}", year) for i in range(50) for year in range(2019, 2025)]
        cdc = pd.DataFrame(rows, columns=["name", "period"])
        cdc["rate"] = 5.0
        cdc["count_sup"] = 100
        counts = cdc[["name", "period"]].rename(columns={"name": "state", "period": "year"})
        counts["restrictive_records"] = 1
        counts["permissive_records"] = 1
        counts["total_law_records"] = 2
        with self.assertRaisesRegex(ValueError, "Cobertura inesperada"):
            build_association_table(cdc, counts.iloc[:-1])

    def test_full_panel_rejects_missing_economic_row(self):
        rows = [(f"State {i}", year) for i in range(50) for year in range(2019, 2025)]
        cdc = pd.DataFrame(rows, columns=["name", "period"])
        cdc["rate"] = 5.0
        cdc["count_sup"] = 100
        keys = cdc[["name", "period"]].rename(columns={"name": "state", "period": "year"})
        counts = keys.copy()
        counts["restrictive_records"] = 1
        counts["permissive_records"] = 1
        counts["total_law_records"] = 2
        ccw = keys.copy()
        ccw["ccw_permitless"] = 0
        background = keys.copy()
        background["background_handgun"] = 0
        unemployment = keys.copy()
        unemployment["unemployment_rate"] = 3.0
        income = keys.iloc[:-1].copy()
        income["income_per_capita"] = 50000
        with self.assertRaisesRegex(ValueError, "Cobertura incompleta"):
            build_policy_panel(cdc, counts, ccw, background, unemployment, income)


if __name__ == "__main__":
    unittest.main()

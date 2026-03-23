from tech_test.app import (
    parse_csv_to_dataframe,
    find_duplicates,
    sum_values,
    cleanse_dates,
    rank_top_speed_mph,
)
import pytest
from datetime import datetime


def test_task_1_ingest_csv():
    filepath = "./fleet_data.csv"

    actual = parse_csv_to_dataframe(filepath)

    expected_columns = [
        "fleet_id",
        "family",
        "class",
        "type",
        "top_speed_mph",
        "top_speed_kmh",
        "number_in_fleet",
        "number_of_carriages",
        "build_date_range_start",
        "build_date_range_end",
    ]
    expected_row_count = 14

    assert list(actual) == expected_columns
    assert len(actual) == expected_row_count


@pytest.mark.skip
def test_task_2_find_multi_carriage_options():
    filepath = "./fleet_data.csv"

    actual = find_duplicates(filepath)

    expected_row_count = 3

    expected_trainsets = [
        {"family": "Sprinter", "class": "158 Express Sprinter"},
        {"family": "CAF Civity", "class": "195"},
        {"family": "CAF Civity", "class": "331"},
    ]

    assert len(actual) == expected_row_count
    assert actual[["family", "class"]].to_dict(orient="records") == expected_trainsets


@pytest.mark.skip
def test_task_3_sum_values():
    filepath = "./fleet_data.csv"

    actual = sum_values(filepath, "total_carriages_for_set_type")

    assert len(actual) == 1
    assert actual.iloc[0]["total_carriages"] == 134
    assert actual.iloc[0]["family"] == "Sprinter"
    assert actual.iloc[0]["class"] == "156 Super Sprinter"


@pytest.mark.skip
def test_task_4_format_dates():
    list_of_dates = [
        "23/02/2026",
        "25/06/2025",
        "04/01/2023",
        "30/02/2022",
        "12/12/2024",
    ]

    actual = cleanse_dates(list_of_dates)

    assert actual == [
        datetime(2026, 2, 23, 0, 0),
        datetime(2025, 6, 25, 0, 0),
        datetime(2023, 1, 4, 0, 0),
        None,
        datetime(2024, 12, 12, 0, 0),
    ]


@pytest.mark.skip
def test_task_5_rank_by_mph():
    filepath = "./fleet_data.csv"

    actual = rank_top_speed_mph(filepath)

    expected_speed_rankings = [
        1.0,
        1.0,
        1.0,
        1.0,
        0.75,
        0.75,
        1.0,
        0.75,
        0.75,
        1.0,
        0.75,
        0.75,
        1.0,
        1.0,
    ]

    assert actual["speed_rank_mph"].to_list() == expected_speed_rankings

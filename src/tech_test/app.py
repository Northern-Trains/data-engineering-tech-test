from datetime import datetime
import pandas as pd


# Task 1 - Ingest CSV
def parse_csv_to_dataframe(filepath: str) -> pd.DataFrame:
    """Task 1: Ingest CSV. Using Pandas, ingest the `fleet_data.csv` file into
    a DataFrame. Think about how you can make the method reusable, you may need
    it later on.

    Args:
        filepath (str): The path of the file to ingest.

    Returns:
        pd.DataFrame: The DataFrame.
    """
    pass


def find_duplicates(filepath: str) -> pd.DataFrame:
    """Task 2: Using the DataFrame you created in the last task, find all rows
    with the same value in the `family` and `class` columns.

    Args:
        filepath (str): The path to the CSV.

    Returns:
        pd.DataFrame: The DataFrame.
    """
    pass


# Task 3 - Calculate the class of train with the largest number of carriages in the fleet
def sum_values(filepath: str, agg_column: str) -> pd.DataFrame:
    """Task 3: Find the type of train that we have the most number of carriages
    for in the fleet.

    Args:
        filepath (str): The CSV data file.
        agg_column (str): The column to aggregate on.

    Returns:
        pd.DataFrame: The DataFrame.
    """
    pass


# Task 4 - Format Dates
def cleanse_dates(list_of_dates: list[str]) -> list[datetime]:
    """Task 4: Given a list of date strings, format them to datetime object. Be
    careful, there's one date that's not a date that you'll need to handle.

    Args:
        list_of_dates (list[str]): The list of date strings.

    Returns:
        list[datetime]: The list of datetime objects.
    """
    pass


# Task 5 Rank Train Family/Class by their top speed in MPH
def rank_top_speed_mph(filepath: str) -> pd.DataFrame:
    """Task 5: Percentage rank all of the train types by their top speed in MPH.

    Args:
        filepath (str): The CSV data file.

    Returns:
        pd.DataFrame: The DataFrame.
    """
    pass

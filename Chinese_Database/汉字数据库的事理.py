import json
import pandas as pd


class Database:
    def __init__(self):
        with open("Database_Files/汉字数据库.json", "r") as fp:
            self._data = json.loads(fp.read())

        self._DB_KEYS = {
            "entryCharacter": "charater",
            "entryPin1yin1": "pin1yin1",
            "entryEnglish": "definition",
            "entryPOSL": "entryPOSL",
        }
        self._database_normalized = pd.json_normalize(self._data, record_path=["汉字数据库"])

    def get_database(self) -> pd.DataFrame:
        """Get the normalized json database in a Pandas Dataframe

        Returns:
            pd.DataFrame: Normalized JSON DB
        """
        return self._database_normalized

    def search_database(self, searchEntries: dict[str, str]) -> dict[dict[str, str]]:
        """Query Database based on user search values

        Args:
            searchEntries (dict[str, str]): A dictionary of key value pairs containing the user's search values

        Returns:
            dict[dict[str, str]]: A collection of the queried results
        """
        searchValues = {
            self._DB_KEYS.get(key): searchEntries.pop(key)
            for key in searchEntries.copy().keys()
        }
        refinedDB = self._database_normalized.copy()

        for filter, value in searchValues.items():
            if filter == "entryPOSL":
                filter = "lesson" if value[0].isdigit() else "POS"

            refinedDB = refinedDB[refinedDB[filter].str.contains(value)]
        return refinedDB.to_dict('index')

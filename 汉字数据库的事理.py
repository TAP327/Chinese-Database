import json
import pandas as pd

class Database():
    def __init__(self):
        with open('汉字数据库.json' , 'r') as fp:
            self._data = json.loads(fp.read())

        self._database_normalized = pd.json_normalize(self._data, record_path = ['汉字数据库'])

    def get_database(self) -> pd.DataFrame:
        return self._database_normalized

    def search_database(self, valueDict) -> list[str]:
        pass

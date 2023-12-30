import json
import pandas as pd

class Database:
     def __init__(self):
          with open('Character_Database.json', 'r', encoding = 'utf-8') as file:
               self._data = json.load(file)
     
          self._DB_KEYS = {
               'entryCharacter': 'character',
               'entryPin1yin1': 'pin1yin1',
               'entryEnglish': 'definition',
               'entryPOSL': 'entryPOSL'
          }
          print(self._data)
          self._database_normalized = pd.json_normalize(self._data, record_path=["汉字数据库"])

     def _getDatabase(self) -> pd.DataFrame:
          return self._database_normalized

     def _seachDatabaseDB(self, searchEntries: dict[str,str]) -> dict[dict[str, str]]:
          searchValues = {
               self._DB_KEYS.get(key): searchEntries.pop(key)
               for key in searchEntries.copy().keys()
          }
          refinedDB = self._database_normalized.copy()

          for filter, value in searchValues.items:
               if filter == 'entryPOSL':
                    filter = 'lesson' if value[-1].isdigit() else 'POS'
                    refinedDB = refinedDB[refinedDB[filter].str.contains(value)]
               return refinedDB.to_dict('index')
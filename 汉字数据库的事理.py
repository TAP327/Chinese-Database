import json
import pandas as pd
import re


class Database:
     def __init__(self):
          with open('Character_Database.json', 'r', encoding = 'utf-8') as file:
               self._data = json.load(file)
     
          self._DB_KEYS = {
               'entryCharacter': 'character',
               'entryEnglish': 'definition',
               'entryPOSL': 'entryPOSL',
               'entryPin1yin1': 'pin1yin1'
          }
          self._database_normalized = pd.json_normalize(self._data, record_path=["汉字数据库"])

     def get_database(self) -> pd.DataFrame:
          return self._database_normalized

     def search_database_DB(self, searchEntries: dict[str,str]) -> dict[dict[str, str]]:
          searchValues = {
               self._DB_KEYS.get(key): searchEntries.pop(key)
               for key in searchEntries.copy().keys()
          }
          pinyinSeparated = searchValues.get('pin1yin1')
          if pinyinSeparated != None:
               pinyinSeparated = re.split(
                    pattern = r"([a-z][a-z]*[1-5])|([a-z][a-z]*$)|([a-z][a-z]*\s)|([1-5])", 
                    string = pinyinSeparated, 
                    flags = re.IGNORECASE
               )
          refinedDB = self._database_normalized.copy()
          for filter, value in searchValues.items():
               if filter == 'entryPOSL':
                    if value[0:3].lower() == 'hsk' or 'ban':
                         filter = 'HSK'
                         value = value.upper()
                    elif value[-1].isdigit() or value[-1] == '#':
                         filter = 'lesson'
                    else:
                         filter = 'POS'
               if filter != 'pin1yin1':
                    refinedDB = refinedDB[refinedDB[filter].str.contains(value)]
               else:
                    pinyin = 0
                    while pinyin < len(pinyinSeparated):
                         if pinyinSeparated[pinyin] != '' and pinyinSeparated[pinyin] != None:
                              pattern = f'((?:{pinyinSeparated[pinyin]})[1-5])|((?:{pinyinSeparated[pinyin]})$)|((?:{pinyinSeparated[pinyin]})\s)'
                              refinedDB = refinedDB[refinedDB[filter].str.contains(pat = pattern)]
                         pinyin += 1
          print(refinedDB.to_dict('index'))
          return refinedDB.to_dict('index')
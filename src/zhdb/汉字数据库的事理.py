import json
import pandas as pd
import re


class Database:
     def __init__(self):
          with open('src\zhdb\Character_Database.json', 'r', encoding = 'utf-8') as file:
               self._data = json.load(file)
          self._database_normalized = pd.json_normalize(self._data, record_path=["汉字数据库"])

     def get_database(self) -> pd.DataFrame:
          return self._database_normalized

     def search_database_DB(self, searchEntries: dict[str,str]) -> dict[dict[str, str]]:
          pinyinSeparated = searchEntries.get('pin1yin1')
          if pinyinSeparated != None:
               pinyinSeparated = re.split(
                    pattern = r"([a-z][a-z]*[1-5])|([a-z][a-z]*$)|([a-z][a-z]*\s)|([1-5])", 
                    string = pinyinSeparated, 
                    flags = re.IGNORECASE
               )
          refinedDB = self._database_normalized.copy()
          for filter, value in searchEntries.items():
               if filter != 'definition':
                    value = value.lower()
                    print('not definition: ' + value)
               else: 
                    print('definition')
               if filter == 'HSK':
                    if value[0:3] == 'hsk' or value[0:4] == 'band':
                         value = value.upper()
                         filter = 'HSK'
                    else:
                         filter = 'lesson'
               if filter != 'pin1yin1':
                    refinedDB = refinedDB[refinedDB[filter].str.contains(value)]
               else:
                    for pinyin in range(len(pinyinSeparated)):
                         if pinyinSeparated[pinyin] != '' and pinyinSeparated[pinyin] != None:
                              pattern = f'((?:{pinyinSeparated[pinyin]})[1-5])|((?:{pinyinSeparated[pinyin]})$)|((?:{pinyinSeparated[pinyin]})\s)'.lower()  
                                   #In the line above, .lower() is necessary to extract the groups
                              refinedDB = refinedDB[refinedDB[filter].str.contains(pat = pattern)]
          return refinedDB.to_dict('index')
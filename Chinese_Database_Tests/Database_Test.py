import unittest
import sys

sys.path.append("../Chinese-Database/")
from Chinese_Database.汉字数据库的事理 import Database


class Database_Tester(unittest.TestCase):
    def setUp(self):
        self.__ZH_DB = Database()

    def test_to_be_lookup(self):
        to_be_query = self.__ZH_DB.search_database({"entryEnglish": "to be"})
        mock_response = [
            {
                "character": "是",
                "pin1yin1": "shi4",
                "POS": "verb",
                "lesson": "1.1",
                "definition": "to be",
                "notes": "also 'yes' in affirmative answers",
            },
            {
                "character": "姓",
                "pin1yin1": "xing4",
                "POS": "verb",
                "lesson": "1.2",
                "definition": "to be surnamed",
                "notes": "also noun: surname",
            },
            {
                "character": "认识",
                "pin1yin1": "ren4shi5",
                "POS": "verb",
                "lesson": "1.5",
                "definition": "to know, to recognize, to be aquainted with, to be familiar with",
                "notes": "conocer",
            },
            {
                "character": "在",
                "pin1yin1": "zai4",
                "POS": "verb",
                "lesson": "1.6",
                "definition": "to be at, to be in",
                "notes": "also preposition: at, in",
            },
            {
                "character": "行",
                "pin1yin1": "xing2",
                "POS": "verb",
                "lesson": "1.8",
                "definition": "to be alright",
                "notes": "...",
            },
            {
                "character": "上网",
                "pin1yin1": "shang4wang3",
                "POS": "VO",
                "lesson": "1.9",
                "definition": "to be online",
                "notes": "...",
            },
            {
                "character": "能",
                "pin1yin1": "neng2",
                "POS": "auxiliary verb",
                "lesson": "1.12",
                "definition": "to be able to",
                "notes": "shows physical capacity",
            },
            {
                "character": "岁",
                "pin1yin1": "sui4",
                "POS": "verb",
                "lesson": "1.14",
                "definition": "to be # years old",
                "notes": "i.e. 我岁十八",
            },
            {
                "character": "离",
                "pin1yin1": "li2",
                "POS": "verb",
                "lesson": "1.18",
                "definition": "to be away from",
                "notes": "also used in 离开 (li2kai1: to leave)",
            },
            {
                "character": "小心",
                "pin1yin1": "xiao3xin1",
                "POS": "verb",
                "lesson": "2.1",
                "definition": "to be careful",
                "notes": "also adjective: cautious",
            },
            {
                "character": "负责",
                "pin1yin1": "fu4ze2",
                "POS": "verb",
                "lesson": "2.1",
                "definition": "to be responsible for",
                "notes": "...",
            },
            {
                "character": "变成",
                "pin1yin1": "bian4cheng2",
                "POS": "VC",
                "lesson": "2.3",
                "definition": "to become",
                "notes": "...",
            },
            {
                "character": "习惯",
                "pin1yin1": "xi2guan4",
                "POS": "verb",
                "lesson": "2.4",
                "definition": "to be used to",
                "notes": "similar: 适应 (shi4ying4)",
            },
            {
                "character": "相聚",
                "pin1yin1": "xiang1ju4",
                "POS": "verb",
                "lesson": "2.4",
                "definition": "to be together, get together",
                "notes": "...",
            },
            {
                "character": "找得到",
                "pin1yin1": "zhao3de5dao4",
                "POS": "phrase",
                "lesson": "2.7",
                "definition": "to be able to find",
                "notes": "example of a positive potential complement",
            },
            {
                "character": "四季如春",
                "pin1yin1": "si4ji4ru2chun1",
                "POS": "phrase",
                "lesson": "2.7",
                "definition": "to be like spring all year round",
                "notes": "four seasons like spring",
            },
            {
                "character": "不如",
                "pin1yin1": "bu4ru2",
                "POS": "verb",
                "lesson": "2.8",
                "definition": "to be inferior to, to be not as good as",
                "notes": "...",
            },
        ]
        self.assertEqual(
            list(to_be_query.values()),
            mock_response,
            f"Query should return: {mock_response}",
        )


if __name__ == "__main__":
    unittest.main()

import unittest
from 汉字数据库的事理 import Database


class Database_Test(unittest.TestCase):

    def setUp(self):
        self.__ZH_DB = Database()

    if __name__ == '__main__':
        unittest.main()

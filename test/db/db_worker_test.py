import unittest
import sys
import os
sys.path.append(os.path.join('..\..', 'src'))
from backend.db.db_obj import DBObject


class DBWorkerTest(unittest.TestCase):
    # maybe later...
    # check out https://github.com/vmalloc/mongomock
    pass

if __name__ == '__main__':
    unittest.main()

import unittest
import sys
import os
sys.path.append(os.path.join('..\..', 'src'))
from backend.db.db_obj import DBObject


class DBObjectTest(unittest.TestCase):

    def setUp(self):
        self.test_db_obj = DBObject()
        self.id_str = "1234"

    def test_id_not_set_on_init(self):
        self.assertFalse(self.test_db_obj.is_id_set())

    def test_set_id_str(self):
        self.test_db_obj.set_id(self.id_str)
        self.assertTrue(self.test_db_obj.is_id_set())
        self.assertEqual(self.test_db_obj.get_id(), self.id_str)

    def test_set_id_err(self):
        id_num = 1234
        with self.assertRaises(TypeError):
            self.test_db_obj.set_id(id_num)

    def test_get_as_dict_no_id(self):
        self.assertDictEqual(self.test_db_obj.get_as_dict(), {})

    def test_get_as_dict_with_id(self):
        self.test_db_obj.set_id(self.id_str)
        expected_dict = {"id": "1234"}
        self.assertDictEqual(
            self.test_db_obj.get_as_dict(), expected_dict)


if __name__ == '__main__':
    unittest.main()

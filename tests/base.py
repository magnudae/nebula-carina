import string
import unittest
import random
from nebula_model.ngql.schema.space import show_spaces, create_space, VidTypeEnum, drop_space, use_space


class TestWithNewSpace(unittest.TestCase):
    test_string_space_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    test_int_space_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

    @classmethod
    def setUpClass(cls):
        assert cls.test_string_space_name not in show_spaces()
        assert cls.test_int_space_name not in show_spaces()
        create_space(cls.test_string_space_name, (VidTypeEnum.FIXED_STRING, 20))
        create_space(cls.test_int_space_name, VidTypeEnum.INT64)

    @classmethod
    def tearDownClass(cls):
        drop_space(cls.test_string_space_name)
        drop_space(cls.test_int_space_name)
        assert cls.test_string_space_name not in show_spaces(), f'Spacee {cls.test_string_space_name} is not cleaned!'
        assert cls.test_int_space_name not in show_spaces(), f'Spacee {cls.test_int_space_name} is not cleaned!'

from unittest import TestCase
from unittest.mock import mock_open, patch

from models import users_file
from models.file import File


class TestUsersFileModelFields(TestCase):
    ttask_mock = 4
    umax_mock = 2
    values = [ttask_mock, umax_mock, 1,2,3,0,1,0,1]
    file_mock = '\n'.join([
        str(value) for value in values
    ])
    
    @patch("builtins.open", new_callable=mock_open, read_data=file_mock)
    def setUp(self, mock_file):
        self.users_file = users_file.UsersFile('teste')
 
    def test_users_file_model_exists(self):
        self.assertEqual(
            hasattr(users_file, "UsersFile"), True,
            "UsersFile doesn't exist"
        )
    
    def test_users_file_model_must_be_initializable(self):
        self.assertEqual(
            hasattr(users_file.UsersFile, "__init__"), True,
            "UsersFile must exist inside users_file's file"
        )

    def test_users_file_extends_file(self):
        self.assertEqual(
            issubclass(users_file.UsersFile, File),True
        )

    def test_users_file_class_fields(self):
        self.assertEqual(self.users_file.ttask, self.ttask_mock)   
        self.assertEqual(self.users_file.umax, self.umax_mock) 
        self.assertEqual(self.users_file.new_users_per_tick, self.values[2:]) 

    

    
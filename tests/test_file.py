from unittest import TestCase
from unittest.mock import mock_open, patch

from models import file


class TestFileModelFields(TestCase):
    ttask_mock = 4
    umax_mock = 2
    values = [ttask_mock, umax_mock, 1,2,3,0,1,0,1]
    file_mock = '\n'.join([
        str(value) for value in values
    ])
 
    def test_file_model_exists(self):
        self.assertEqual(
            hasattr(file, "File"), True,
            "File doesn't exist"
        )
    
    def test_file_model_must_be_initializable(self):
        self.assertEqual(
            hasattr(file.File, "__init__"), True,
            "File must exist inside file's file"
        )
    
    @patch("builtins.open", new_callable=mock_open, read_data=file_mock)
    def test_file_class_fields(self, mock_file):
        path_name = 'teste'
        instance = file.File(path_name)
        self.assertEqual(instance.path, path_name)   
        self.assertEqual(instance.data, self.values)
    

    
from unittest import TestCase

from models import user


class TestUserModel(TestCase):

    def test_user_model_exists(self):
        self.assertEqual(
            hasattr(user, "User"), True,
            "User doesn't exist"
        )
    
    def test_user_model_must_be_initializable(self):
        self.assertEqual(
            hasattr(user.User, "__init__"), True,
            "User must exist inside user's file"
        )
    
    def test_user_class_has_no_arguments(self):
        self.assertRaises(
            TypeError, user.User, 'teste'
        )   
    
    def test_user_fields(self):
        self.assertEqual(
            hasattr(user.User(), "tick"), True,
            "User must be initialized with a tick value"
        )
    
    def test_user_tick_starting_value(self):
        self.assertEqual(
            user.User().tick, 0,
            "tick value must be initialized as 0"
        )

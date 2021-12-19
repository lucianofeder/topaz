from unittest import TestCase

from models import server
from models.user import User


class TestServerModelFields(TestCase):

    def test_server_model_exists(self):
        self.assertEqual(
            hasattr(server, "Server"), True,
            "Server doesn't exist"
        )
    
    def test_server_model_must_be_initializable(self):
        self.assertEqual(
            hasattr(server.Server, "__init__"), True,
            "Server must exist inside server's file"
        )
    
    def test_server_class_fields(self):
        data = {
            "umax": 2,
            "ttask": 4
        }
        instance = server.Server(**data) 
        self.assertEqual(instance.umax, data["umax"])   
        self.assertEqual(instance.ttask, data["ttask"])
        self.assertEqual(instance.users, [])
    

    def test_server_user_field_starting_value(self):
        """
        users has to always start with an empty list
        """
        data = {
            "umax": 2,
            "ttask": 4,
            "users": [User()]
        }
        self.assertRaises(TypeError, server.Server, **data)


class TestServerModelDisconnectMethod(TestCase):

    def setUp(self):
        data = {
            "umax": 3,
            "ttask": 4
        }
        self.server = server.Server(**data)

    def test_disconnect_inactive_users_exists(self):
        self.assertEqual(
            hasattr(self.server, "disconnect_inactive_users"), True,
            "server instance must have disconnect_inactive_users method"
        )

    def test_disconnect_inactive_users_must_be_callable(self):
        self.assertEqual(
            hasattr(server.Server.disconnect_inactive_users, "__call__"), True,
            "disconnect_inactive_users must be callable"
        )

    def test_disconnect_inactive_users_with_active_users(self):
        users = [User(), User()]
        self.server.users = users
        self.server.disconnect_inactive_users()
        self.assertEqual(self.server.users, users)
    
    def test_disconnect_inactive_users_with_inactive_users(self):
        user_1 = User()
        user_1.tick = 4
        user_2 = User()
        user_2.tick = 4

        users = [user_1, user_2]

        self.server.users = users
        self.server.disconnect_inactive_users()
        self.assertEqual(self.server.users, [])
    
    def test_disconnect_inactive_users_with_active_and_inactive_users(self):
        user_1 = User()
        user_1.tick = 4
        user_2 = User()

        users = [user_1, user_2]

        self.server.users = users
        self.server.disconnect_inactive_users()
        self.assertEqual(self.server.users, [user_2])


class TestServerModelIsFullMethod(TestCase):

    def setUp(self):
        data = {
            "umax": 3,
            "ttask": 4
        }
        self.server = server.Server(**data)

    def test_is_full_exists(self):
        self.assertEqual(
            hasattr(self.server, "is_full"), True,
            "server instance must have is_full method"
        )

    def test_is_full_must_be_callable(self):
        self.assertEqual(
            hasattr(server.Server.is_full, "__call__"), True,
            "is_full must be callable"
        )

    def test_is_full_with_empty_list(self):
        self.assertEqual(self.server.is_full(), False)
    
    def test_is_full_with_full_list(self):
        self.server.users = [User(),User(),User()] 
        self.assertEqual(self.server.is_full(), True)
    
    def test_is_full_with_half_list(self):
        self.server.users = [User(),User()] 
        self.assertEqual(self.server.is_full(), False)


class TestServerModelIsEmptyMethod(TestCase):

    def setUp(self):
        data = {
            "umax": 3,
            "ttask": 4
        }
        self.server = server.Server(**data)

    def test_is_empty_exists(self):
        self.assertEqual(
            hasattr(self.server, "is_empty"), True,
            "server instance must have is_empty method"
        )

    def test_is_empty_must_be_callable(self):
        self.assertEqual(
            hasattr(server.Server.is_empty, "__call__"), True,
            "is_empty must be callable"
        )

    def test_is_empty_with_empty_list(self):
        self.assertEqual(self.server.is_empty(), True)
    
    def test_is_empty_with_full_list(self):
        self.server.users = [User(),User(),User()] 
        self.assertEqual(self.server.is_empty(), False)
    
    def test_is_empty_with_half_list(self):
        self.server.users = [User(),User()] 
        self.assertEqual(self.server.is_empty(), False)


class TestServerModelAddUserMethod(TestCase):

    def setUp(self):
        data = {
            "umax": 3,
            "ttask": 4
        }
        self.server = server.Server(**data)

    def test_add_user_exists(self):
        self.assertEqual(
            hasattr(self.server, "add_user"), True,
            "server instance must have add_user method"
        )

    def test_add_user_must_be_callable(self):
        self.assertEqual(
            hasattr(server.Server.add_user, "__call__"), True,
            "add_user must be callable"
        )

    def test_add_user_with_empty_list(self):
        self.server.add_user()
        self.assertEqual(len(self.server.users), 1)
        self.server.add_user()
        self.assertEqual(len(self.server.users), 2)
        
    
    def test_add_user_with_full_list(self):
        self.server.users = [User(),User(),User()] 
        self.server.add_user()
        self.assertEqual(len(self.server.users), 3)
    

class TestServerModelExecTickCycleMethod(TestCase):

    def setUp(self):
        data = {
            "umax": 3,
            "ttask": 4
        }
        self.server = server.Server(**data)

    def test_exec_a_tick_cycle_exists(self):
        self.assertEqual(
            hasattr(self.server, "exec_a_tick_cycle"), True,
            "server instance must have exec_a_tick_cycle method"
        )

    def test_exec_a_tick_cycle_must_be_callable(self):
        self.assertEqual(
            hasattr(server.Server.exec_a_tick_cycle, "__call__"), True,
            "exec_a_tick_cycle must be callable"
        )

    def test_exec_a_tick_cycle_increment_one_tick_on_each_user(self):
        user_1 = User()
        user_1.tick = 1
        user_2 = User()
        self.server.users = [user_1, user_2]
        
        self.server.exec_a_tick_cycle()
        self.assertEqual(self.server.users[0].tick, 2)
        self.assertEqual(self.server.users[1].tick, 1)
        
    


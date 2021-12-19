import pdb
from unittest import TestCase
from unittest.mock import mock_open, patch

from models import servers_manager as manager
from models.users_file import UsersFile
from models.server import Server


class TestServerManagerModelFields(TestCase):
    ttask_mock = 4
    umax_mock = 2
    values = [ttask_mock, umax_mock, 1,2,3,0,1,0,1]
    file_mock = '\n'.join([
        str(value) for value in values
    ])
    
    @patch("builtins.open", new_callable=mock_open, read_data=file_mock)
    def setUp(self, mock_file):
        self.servers_manager = manager.ServersManager('teste')

    def test_server_manager_model_exists(self):
        self.assertEqual(
            hasattr(manager, "ServersManager"), True,
            "ServersManager doesn't exist"
        )
    
    def test_servers_manager_model_must_be_initializable(self):
        self.assertEqual(
            hasattr(manager.ServersManager, "__init__"), True,
            "ServersManager must exist inside servers_manager's file"
        )

    def test_servers_manager_extends_users_file(self):
        self.assertEqual(
            issubclass(manager.ServersManager, UsersFile), True
        )
    
    def test_servers_manager_fields(self):
        self.assertEqual(hasattr(self.servers_manager, "servers"), True)
        self.assertIsInstance(self.servers_manager.servers, list)

        self.assertEqual(hasattr(self.servers_manager, "total_price"), True)
        self.assertIsInstance(self.servers_manager.total_price, int)

        self.assertEqual(hasattr(self.servers_manager, "history"), True)
        self.assertIsInstance(self.servers_manager.history, list)


class TestServerManagerDeactivateServersMethod(TestCase):
    ttask_mock = 4
    umax_mock = 2
    values = [ttask_mock, umax_mock, 1,2,3,0,1,0,1]
    file_mock = '\n'.join([
        str(value) for value in values
    ])
    
    @patch("builtins.open", new_callable=mock_open, read_data=file_mock)
    def setUp(self, mock_file):
        self.servers_manager = manager.ServersManager('teste')


    def test_deactivate_unused_servers_exists(self):
        self.assertEqual(
            hasattr(self.servers_manager, "deactivate_unused_servers"), True,
            "server instance must have deactivate_unused_servers method"
        )

    def test_deactivate_unused_servers_must_be_callable(self):
        self.assertEqual(
            hasattr(self.servers_manager.deactivate_unused_servers, "__call__"), True,
            "deactivate_unused_servers must be callable"
        )
    
    def test_deactivate_unused_servers_with_only_empty_servers(self):
        self.servers_manager.servers = [
            Server(umax=self.umax_mock, ttask=self.ttask_mock),
            Server(umax=self.umax_mock, ttask=self.ttask_mock)
        ]
        self.servers_manager.deactivate_unused_servers()
        
        self.assertEqual(self.servers_manager.servers, [])
    
    def test_deactivate_unused_servers_with_only_used_servers(self):
        server_1 = Server(umax=self.umax_mock, ttask=self.ttask_mock)
        server_1.add_user()
        server_2 = Server(umax=self.umax_mock, ttask=self.ttask_mock)
        server_2.add_user()

        self.servers_manager.servers = [server_1, server_2]
        self.servers_manager.deactivate_unused_servers()
        
        self.assertEqual(self.servers_manager.servers, [server_1, server_2])

    def test_deactivate_unused_servers_with_empty_and_used_servers(self):
        server_1 = Server(umax=self.umax_mock, ttask=self.ttask_mock)
        server_1.add_user()
        server_2 = Server(umax=self.umax_mock, ttask=self.ttask_mock)

        self.servers_manager.servers = [server_1, server_2]
        self.servers_manager.deactivate_unused_servers()
        
        self.assertEqual(self.servers_manager.servers, [server_1])


class TestServerManagerGetServersStateMethod(TestCase):
    ttask_mock = 4
    umax_mock = 2
    values = [ttask_mock, umax_mock, 1,2,3,0,1,0,1]
    file_mock = '\n'.join([
        str(value) for value in values
    ])
    
    @patch("builtins.open", new_callable=mock_open, read_data=file_mock)
    def setUp(self, mock_file):
        self.servers_manager = manager.ServersManager('teste')


    def test_get_servers_state_exists(self):
        self.assertEqual(
            hasattr(self.servers_manager, "get_servers_state"), True,
            "server instance must have get_servers_state method"
        )

    def test_get_servers_state_must_be_callable(self):
        self.assertEqual(
            hasattr(self.servers_manager.get_servers_state, "__call__"), True,
            "get_servers_state must be callable"
        )
    
    def test_get_servers_state_with_not_empty_list(self):
        server_1 = Server(umax=self.umax_mock, ttask=self.ttask_mock)
        server_1.add_user()
        server_1.add_user()
        server_2 = Server(umax=self.umax_mock, ttask=self.ttask_mock)
        server_2.add_user()

        self.servers_manager.servers = [server_1, server_2]

        self.assertEqual(self.servers_manager.get_servers_state(), ["2","1"])

    def test_get_servers_state_with_empty_list(self):
        self.assertEqual(self.servers_manager.get_servers_state(), ["0"])


class TestServerManagerExecTickCycleMethod(TestCase):
    ttask_mock = 4
    umax_mock = 2
    values = [ttask_mock, umax_mock, 1,2,3,0,1,0,1]
    file_mock = '\n'.join([
        str(value) for value in values
    ])
    
    @patch("builtins.open", new_callable=mock_open, read_data=file_mock)
    def setUp(self, mock_file):
        self.servers_manager = manager.ServersManager('teste')
        server_1 = Server(umax=self.umax_mock, ttask=self.ttask_mock)
        server_1.add_user()
        server_1.add_user()
        server_2 = Server(umax=self.umax_mock, ttask=self.ttask_mock)
        server_2.add_user()

        self.servers_manager.servers = [server_1, server_2]


    def test_exec_a_tick_cycle_exists(self):
        self.assertEqual(
            hasattr(self.servers_manager, "exec_a_tick_cycle"), True,
            "server instance must have exec_a_tick_cycle method"
        )

    def test_exec_a_tick_cycle_must_be_callable(self):
        self.assertEqual(
            hasattr(self.servers_manager.exec_a_tick_cycle, "__call__"), True,
            "exec_a_tick_cycle must be callable"
        )
    
    @patch("models.server.Server.exec_a_tick_cycle")
    def test_exec_a_tick_cycle_with_not_empty_list(self, mock):
        
        self.servers_manager.exec_a_tick_cycle()

        self.assertEqual(mock.call_count, 2)
    
    @patch("models.server.Server.exec_a_tick_cycle")
    def test_exec_a_tick_cycle_with_empty_list(self, mock):
        self.servers_manager.servers = []
        self.servers_manager.exec_a_tick_cycle()

        self.assertEqual(mock.call_count, 0)
    
    @patch("models.server.Server.exec_a_tick_cycle")
    def test_exec_a_tick_cycle_update_price(self, mock):
        """
        total price must increase by 1 for each Server
        """
        self.servers_manager.total_price = 0
        self.servers_manager.exec_a_tick_cycle()

        self.assertEqual(self.servers_manager.total_price, 2)

        self.servers_manager.servers = self.servers_manager.servers + [Server(umax=self.umax_mock, ttask=self.ttask_mock)]
        self.servers_manager.exec_a_tick_cycle()
        self.assertEqual(self.servers_manager.total_price, 5)

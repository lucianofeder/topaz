from .users_file import UsersFile
from .server import Server
import pdb


class ServersManager(UsersFile):
    def __init__(self, path):
        super().__init__(path)
        self.servers = []
        self.total_price = 0
        self.history = self.get_servers_history()


    def deactivate_unused_servers(self):
        self.servers = list(filter(lambda server: not server.is_empty(), self.servers))


    def populate_servers(self, amount_of_users):
        populated = 0
        server_index = 0

        while populated < amount_of_users:
            try:
                server = self.servers[server_index]
                while not server.is_full():
                    server.add_user()
                    populated += 1
                    if populated == amount_of_users:
                        break
                server_index += 1

            except IndexError as _:
                self.servers.append(Server(umax=self.umax, ttask=self.ttask))
        
        return self.get_servers_state()


    def get_servers_state(self):
        return [str(len(server.users)) for server in self.servers] or ['0']


    def exec_a_tick_cycle(self):
        for server in self.servers:
            server.exec_a_tick_cycle()

        self.total_price += len(self.servers)


    def get_servers_history(self):
        result = []
        for users in self.new_users_per_tick:
            self.deactivate_unused_servers()
            self.populate_servers(users)
            self.exec_a_tick_cycle()
            result.append(self.get_servers_state())
        
        while len(self.servers) != 0:
            self.deactivate_unused_servers()
            self.exec_a_tick_cycle()
            result.append(self.get_servers_state())
                    
        result.append([str(self.total_price)])
        self.history = result
        return result

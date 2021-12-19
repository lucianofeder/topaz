from .user import User


class Server:
    def __init__(self, umax, ttask):
        self.umax = int(umax)
        self.ttask = int(ttask)
        self.users = []

    def disconnect_inactive_users(self):
        self.users = list(filter(lambda user: user.tick != self.ttask, self.users))
    
    def is_full(self):
        self.disconnect_inactive_users()
        return len(self.users) == self.umax
    
    def is_empty(self):
        self.disconnect_inactive_users()
        return len(self.users) == 0
    
    def add_user(self):
        if not self.is_full():
            self.users.append(User())

    def exec_a_tick_cycle(self):
        for user in self.users:
            user.tick += 1
    
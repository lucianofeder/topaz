from .file import File


class UsersFile(File):
    def __init__(self, path):
        super().__init__(path)
        self.ttask = self.data[0]
        self.umax = self.data[1]
        self.new_users_per_tick = self.data[2:]
    
    
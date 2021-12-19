
class File:
    def __init__(self, path):
        self.path = path
        self.data = self.get_data()


    def get_data(self):
        data = []
        with open(self.path, "r") as f:
            for line in f:
                data.append(int(line))
            return data


    @classmethod
    def write_data_from_nested_list(cls, path, data):
        with open(path, "w") as f:
            for line in data:
                text = ','.join(line) + "\n"
                f.write(text)
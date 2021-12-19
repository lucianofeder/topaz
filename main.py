from models.servers_manager import ServersManager
from models.file import File


manager = ServersManager('input.txt')

output_file = "output.txt"

File.write_data_from_nested_list(output_file, manager.history)

print("-"*30)
print(f"File created at {output_file}")

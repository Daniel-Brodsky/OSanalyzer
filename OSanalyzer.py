import os

print_assistant = "this is"
print("This is an OS analyzer, designed by dbrodsky.")
print(f"{print_assistant} os.name = {os.name}")
print(f"{print_assistant} os.getenv('HOME') = {os.getenv('HOME')}")
print(f"{print_assistant} os.getenv('APPDATA') = {os.getenv('APPDATA')}")
print(f"{print_assistant} os.getenv('LOG_LEVEL') = {os.getenv('LOG_LEVEL')}")
print(f"{print_assistant} os.getcwd() = {os.getcwd()}")
print(f"{print_assistant} os.listdir() = {os.listdir()}")
print(f"{print_assistant} os.getpid() = {os.getpid()}")
print(f"{print_assistant} os.getppid() = {os.getppid()}")
print(f"{print_assistant} os.getlogin() = {os.getlogin()}")

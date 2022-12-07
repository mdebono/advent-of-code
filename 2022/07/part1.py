class File:
    def __init__(self, size, name):
        self.size = size
        self.name = name
    def __str__(self):
        return 'File: ' + self.name

class Directory:
    def __init__(self, name, parent=None):
        self.files = []
        self.dirs = []
        self.name = name
        self.parent = parent

    def add_dir_file(self, dir_file):
        if isinstance(dir_file, Directory):
            self.dirs.append(dir_file)
        elif isinstance(dir_file, File):
            self.files.append(dir_file)
    
    def get_dir(self, name):
        for dir in self.dirs:
            if dir.name == name:
                return dir
        return None

    def __str__(self):
        return 'Directory: ' + self.name + ' [' + ' '.join([dir.name for dir in self.dirs]) + '] [' + ' '.join([file.name for file in self.files]) + ']'

def get_command_arg(line):
    params = line.split(' ')
    if len(params) == 2:
        return params[1], None
    return params[1], params[2]

def get_dir_file(line, parent):
    params = line.split(' ')
    if params[0] == 'dir':
        return Directory(params[1], parent)
    else:
        return File(int(params[0]), params[1])

root = Directory('/')
current = root

f = open("2022/07/smallinput.txt")

def get_dir(name):
    if name == '/':
        return root
    elif name == '..':
        return current.parent
    else:
        return current.get_dir(name)

for line in f:
    line = line.strip()
    if line.startswith('$'):
        command, arg = get_command_arg(line)
        if command == 'cd':
            print("current: ", current)
            dir = get_dir(arg)
            if dir != None:
                current = dir
            else:
                raise ValueError("error!", dir, arg)
        print(command, arg)
    else:
        dir_file = get_dir_file(line, current)
        print(dir_file)
        current.add_dir_file(dir_file)
        print("current: ", current)

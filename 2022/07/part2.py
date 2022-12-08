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
        self.size = None

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

    def get_size(self):
        if self.size == None:
            files_size = sum([file.size for file in self.files])
            dirs_size = sum([dir.get_size() for dir in self.dirs])
            self.size = files_size + dirs_size
        return self.size

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

def get_dirs_size_at_most(dir, max, dirs):
    if dir.size <= max:
        dirs.append(dir)
    for dir in dir.dirs:
        get_dirs_size_at_most(dir, max, dirs)
    return dirs

def get_dirs_size_at_least(dir, min, dirs):
    if dir.size >= min:
        dirs.append(dir)
    for dir in dir.dirs:
        get_dirs_size_at_least(dir, min, dirs)
    return dirs

root = Directory('/')
current = root

f = open("2022/07/input.txt")

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
            #print("current: ", current)
            dir = get_dir(arg)
            if dir != None:
                current = dir
            else:
                raise ValueError("error!", dir, arg)
        #print(command, arg)
    else:
        dir_file = get_dir_file(line, current)
        #print(dir_file)
        current.add_dir_file(dir_file)
        #print("current: ", current)

root_size = root.get_size()
print(root, root_size)

total_disk_space = 70000000
current_unused_space = total_disk_space - root_size
print(current_unused_space)
required_unused_space = 30000000
required_size = required_unused_space - current_unused_space
print(required_size)

least_dirs = get_dirs_size_at_least(root, required_size, [])
print('\n'.join([str(dir) + ' ' + str(dir.size) for dir in least_dirs]))

total_size = sum([dir.size for dir in least_dirs])
min_size = min([dir.size for dir in least_dirs])
print('total', total_size)
print('min', min_size)
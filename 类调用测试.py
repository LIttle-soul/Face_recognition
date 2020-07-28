import os

path = './Information/'
name = input('please input you delete name: ')
path += name
def del_file(path):
    for i in os.listdir(path):
        path_file = os.path.join(path, i)
        if os.path.isfile(path_file):
            os.remove(path_file)
        else:
            del_file(path_file)
    os.rmdir(path)
del_file(path)
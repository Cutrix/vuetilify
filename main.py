import os;
from Utils.Retrieve import Parser


def init_cli(path, project_name):
    os.system("cd {} && vue create {}".format(path, project_name))


if __name__ == '__main__':
    #path = input("> Path: ")
    #project_name = input("Project name: ")
    #init_cli(path, project_name)
    Parser("http://grandu.ci").retrieve_index_items()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

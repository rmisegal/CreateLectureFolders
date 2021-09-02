# This is a sample Python script.
import os


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def genrateFolders(name):
    cwd = os.getcwd()
    print(cwd)

    # Join and split a path
    fp = os.path.join('temp', 'python')
    print(fp)  # temp\python (in Windows)
    pc = os.path.split(fp)
    print(pc)  # ('temp', 'python')

    # Test if a path is a directory
    path = os.path.join("C:\\", "0")
    if os.path.exists(path):
        print(path + ' : exists')
        if os.path.isdir(path):
            print(path + ' : is a directory')
    else:
        print(path + ' : is NOT a directory')

    # Create a directory
    mainFolder = "C:\\Users\\gal-t\\OneDrive - post.bgu.ac.il\\Ofer Hadar\\הוראה\\פייטון\\שנקר\\קורס 2020\\2020"
    for i in range(14):
        folderName = f'{i:02d}'
        dir = os.path.join(mainFolder, "הרצאה " + folderName)
        if not os.path.exists(dir):
            os.mkdir(dir)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    genrateFolders('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

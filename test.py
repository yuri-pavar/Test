import os

def CreateField(root_path):

    list_of_text = ['6 Wonderful text', '1 Some text', '5 Amazing text',
                    '2 Useless text', '4 Great text', '3 Useful text']

    list_of_dirs = ['dir1', 'dir2', 'dir3', 'dir4', 'dir5', 'dir6']

    list_of_files = ['textfile1.txt', 'textfile2.txt', 'textfile3.txt',
                     'textfile4.txt', 'textfile5.txt', 'textfile6.txt']

    if os.path.exists(os.path.join(root_path, list_of_dirs[0])):
        print("Can not create a field because it already exists")

    else:
        for i in range(len(list_of_text)):

            os.mkdir(os.path.join(root_path, list_of_dirs[i])) # create directories

            f = open(os.path.join(root_path, list_of_files[i]), 'w') # creating file and writing in it
            f.write(list_of_text[i])
            f.close()

            root_path = os.path.join(root_path, list_of_dirs[i])

        print("Field successfully created")

root_path = os.getcwd()
CreateField(root_path)






# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import zipfile
import os
from imutils import paths
def zip_file(path, filezip):
    with zipfile.ZipFile(os.path.join(path, filezip)) as data:
        data.extractall(path)
def file_txt(path_cat=None, path_dog=None):
    if path_cat == True:
        file_txt=list(paths.list_files(path_cat))
        #print(file_txt)
        name_file=set([s.split(os.path.sep)[-1].split('.')[0] for s in file_txt])
        #print(name_file)
        cat_txt= [os.path.join(path_cat, s+'.txt') for s in name_file]
        print(cat_txt)
        with open('train.txt', 'w') as v:
            for f in cat_txt:

                        with open(f) as ftxt:
                            read_line= ftxt.readline()
                            print(read_line)
                            v.write(read_line)
                               # v.write('\n')
    else:
        file_txt = list(paths.list_files(path_dog))
        # print(file_txt)
        name_file = set([s.split(os.path.sep)[-1].split('.')[0] for s in file_txt])
        # print(name_file)
        dog_txt = [os.path.join(path_dog, s + '.txt') for s in name_file]
        with open('train.txt', 'a+') as v:
            for f in dog_txt:
                with open(f) as ftxt:
                    read_line = ftxt.readline()
                    print(read_line)
                    v.write(read_line)
                    # v.write('\n')
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #zip_file(path=r'C:\Users\Admin\PycharmProjects\Second', filezip='dog_cat_new.zip')
    file_txt(path_cat=r'C:\Users\Admin\PycharmProjects\Second\dog_cat\train\cats',
             path_dog=r'C:\Users\Admin\PycharmProjects\Second\dog_cat\train\dogs')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

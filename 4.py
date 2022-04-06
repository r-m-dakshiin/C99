import shutil
import os

path = "D:/Dakshiin/Python/class99"
print("before copying files : ")
print(os.listdir(path))
source = "D:/Dakshiin/Python/class99/texttext.txt"
destination = "D:/Dakshiin/Python/class99/texttext(copy).txt"
dest = shutil.copy(source, destination)
print("after copying files : ")
print(os.listdir(path))
print(os.system("time"))

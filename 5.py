import shutil
import os

path = "D:/Dakshiin/Python/class99"
print("before copying files : ")
print(os.listdir(path))
source = "D:/Dakshiin/Python/class99/texttext(copy).txt"
destination = "D:/Dakshiin/Python/class99/texttext(move).txt"
dest = shutil.move(source, destination)
print("after copying files : ")
print(os.listdir(path))

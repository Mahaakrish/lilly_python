import os

#current dir
print(os.getcwd())

#running process id
print(os.getpid())

#create dir
os.mkdir(".\\mk")

#rename dir
os.rename(".\\mk",".\\mr")

#list directories
os.listdir()

#change dir
os.chdir(".\\mr")

#env vars
print(os.getenv())
#syslib/__init__.py
#Created by Jeremy in 2023 Oct 13
#Syslib mainly is about running shell/python script in python.
#Licencse: syslib/LICENSE
#To config delect the '#'
#Version 1.1

import os

#syscall command
def syscall(syscallin):
 #os.system("clear")
 os.system(str(syscallin))

#pycall
def pycall(pycallin):
 #os.system("clear)
 exec(str(pycallin))

#sysshell command
def sysshell():
 #os.system("clear")
 while True:
  sysshellin = input(">>")
  if sysshellin == "exit()":
    exit()
  os.system(str(sysshellin))

#pyshell command
def pyshell():
 #os.system("clear")
 while True:
  pyshellin = input(">>>")
  exec(str(pyshellin))

#help command
def help():
  #os.system("clear")
  print("Syslib Help")
  print("Basic Commamd: syscall, sysshell, pyshell, help.")

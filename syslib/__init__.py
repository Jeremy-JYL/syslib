#syslib/__init__.py
#Created by Jeremy in 2023 Oct 13
#Syslib mainly is about running shell/python script in python.
#Licencse: syslib/LICENSE
#Version 1.0

import os

def syscall(syscallin):
 os.system(str(syscallin))
 
def sysshell():
 while True:
  sysshellin = input(">>")
  if sysshellin == "exit()":
    exit()
  os.system(str(sysshellin))

def pyshell():
 while True:
  pyshellin = input(">>>")
  exec(str(pyshellin))

def help():
  os.system("Clear")
  print("Syslib Help")
  print("Basic Commamd: syscall, sysshell, pyshell, help.")

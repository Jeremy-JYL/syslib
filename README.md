# syslib Version 1.0
This is a python libary that running shell/python script in python.

# Before you start
Check you have installed python3, git, curl.
Optional: bash

If those not installed run this command (On debian base os)

``
sudo apt update && sudo apt install python3 git curl
``

yum

``
sudo yum install python3 git curl
``

dnf

``
sudo dnf install python3 git curl
``

Note: Because I don't use yum & dnf before so if yum & dnf command wrong please write in Issues, thank you.

# How to install
To install run this command: curl https://raw.githubusercontent.com/Jeremy823/syslib/main/install.sh | bash

This Shell script will remove the old version of syslib and it will download the syslib via github and it will copy the file the the syslib folder.

Not working?

Try manually install, please view INSTALL.md

# How To Use
To start first import syslib in python: import syslib
Then syslib include 3 command: syscall(), sysshell(), pyshell(), help(). Note syscall need a argument. E.g: htop, bash.

# Note
syslib did not release on pypi/pip.
syslib did not support Windows but if you want you can port to Windows.

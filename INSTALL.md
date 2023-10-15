# Automatic install

``
curl https://raw.githubusercontent.com/Jeremy823/syslib/main/install.sh | bash
``

# Manually install

``
rm -rf ./syslib && git clone https://github.com/Jeremy823/syslib && mv ./syslib/syslib/__init__.py ./__init__.py && mv ./syslib/LICENSE ./LICENSE && rm -rf ./syslib && mkdir syslib && mv ./__init__.py ./syslib/__init__.py && mv ./LICENSE ./syslib/LICENSE
``

# Note
Automactic install & Manually install need git, curl, bash, python3.

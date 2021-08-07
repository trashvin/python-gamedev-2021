# day 01 activity

## 01 install python
- go to www.python.org
- download the latest python installer
- install python and make sure to select theoption that will include PIP in the installation.
- after installation, verify the install by running the following command
```
python --version

pip --version
```
_this should print the version of python and pip_

## 02 install virtualenv
- install virtualenv from the command line via pip
```
pip install virtualenv

virtualenv --version
```
_this should print the version of virtualenv_

## 03 create a virtual environment
- create a working folder
```
mkdir work_folder
```
- change directory to the new directory
```
cd work_folder
```
- create a virtual environment using virtualenv. use the name .venv
```
virtualenv .venv
```
- activate the virtual environment
```
.venv\Scripts\activate
```
_you should notice the nameof the virtual environment being added on the command line_
- deactivate the virtual environment
```
.venv\Scripts\deactivate
```
### 04 fork the python-gamedev-2021 repo
- make sure you can loginto your github account.
- after login,search for the python-gamedev-2021 repo
- access the repo and clickthe fork button
- check your account,you should be able to see the forked repo

### 05 clobe your own python-gamedev-2021 repo




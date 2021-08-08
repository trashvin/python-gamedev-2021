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

### 05 clone your own python-gamedev-2021 repo
- go to your new repo
- click on the "code" button and copy the repo's url
- got to the folder in your local machine where your codes will reside.
- clone your repo using the [git clone] command
```
git clone https://github.com/trashvin/python-gamedev-2021.git
```
_git will create a new folder and download all files to your local machine_

### 06 make your first changes, commit , and push
- in the command line, go to the directory of the new repo
- start Visual Studio Code by typing the following command
```
code .
```
- go ahead and edit README.md, delete the last line and replace it with your name
- go back to the terminal and type the following
```
git status
```
_notice the modified file entry_
- go ahead and commit your changes
```
git commit -m "initial change"
```
- once commited, you can now push your changes to the main /remote repo
```
git push
```
```
!NOTE : if you have another location where your repo is cloned, make sure to run [git pull] before doing any changes
```





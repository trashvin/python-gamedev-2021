# how to setup your development environment

## install pip 

Pip is a python package manager. You will use this to install new packages needed by your project.

```
# check first if pip is already available by running the command below

pip --version

# if pip is not a recognized command , build and run get-pip.py from the main folder by running the
# command below

python get-pip.py

# verify by getting pip version

pip --version
```

## install virtualenv

Virtualenv will let you create a sandbox for your project. This is important especially if we want to make sure that we have an environment that was created only for the project. Also, this keeps your parent OS clean from unwanted python packages.

```
# check if virtualenv is installed

virtualenv --vesrion

# if virtualenv is not recognized, you need to install it

pip install virtualenv

# verify the install by checking the virtualenv version

virtualenv --version
```

## create a virtualenv in windows

Note: do this inside you project directory. All packages installed while the virtualenv is active will only be available inside that environment.

```
# create a virtualenv
# .venv is arbitrary, its a good practice to start a virtualenv directory with dot, this way it is easier to recognize and ignore during checkin to git (.gitignore)

virtualenv .venv

# activate

.venv\Scripts\activate 

# after running the command above, you will notice your virtualenv name preppended in your prompt

# to deactivate

.venv\Scripts\deactivate
```
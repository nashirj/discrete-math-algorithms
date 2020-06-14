# SETUP
## Mac (tested on Catalina 10.15.4):
- install [homebrew](https://brew.sh/)
- install python3:
	- open terminal
	- `$ brew install python3`
- test python (see windows instructions)
- install and test git (see windows instructions)
- download and run project:
	- open terminal
	- `$ cd Documents`
	- `$ git clone https://github.com/nashirj/discrete-math-algorithms`
	- `$ cd discrete-math-algorithms`
	- `$ pip3 install -r requirements.txt`
	- `$ python3 discretemath/view.py`



## Windows (tested on Windows 10):
- install python:
	- open powershell
	- `$ python`
	- install from the app store
- test python3:
	- `$ python3`
	- `C:\Users\\<username\>\>python`
	- `Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32                          Type "help", "copyright", "credits" or "license" for more information.`
	- `>>> print("hello :)")`
	- `hello :)`
	- `exit()`
	- if you can do the above, python is installed
- upgrade pip:
	- open powershell
	- `$ python3 -m pip install --upgrade pip`
- install git: https://git-scm.com/download/
	- open powershell
	- `$ git status`
	- `fatal: not a git repository (or any of the parent directories): .git`
	- if you see the above line, then git is installed
- download project:
	- `open powershell`
	- `$ cd Documents`
	- `$ git clone https://github.com/nashirj/discrete-math-algorithms`
	- `$ cd discrete-math-algorithms`
	- `$ pip3 install -r requirements.txt`
	- `$ python3 discretemath\view.py`


## Linux (tested on Ubuntu 18.04):
- test python3 (see windows instructions)
- install pip3 (note, it usually comes default with Python): `$ sudo apt-get install python3-pip`
- install tkinter (if needed): `$ sudo apt-get install python3-tk`
- download and run project:
	- open terminal
	- `$ cd Documents`
	- `$ git clone https://github.com/nashirj/discrete-math-algorithms`
	- `$ cd discrete-math-algorithms`
	- `$ pip3 install -r requirements.txt`
	- `$ python3 discretemath/view.py`



## General usage:
- Run the GUI from the top level directory with the command `python3 discretemath/view.py` (OSX/Linux) or `python3 discretemath\view.py` (Windows)
- Import specific packages from the `discretemath` module as follows:
	- `python3
	- `from discretemath.py import bell
	- `help(bell)
	- `bell.bell_dp(10)
	- `from discretemath.py import recurrence
	- `recurrence.solve_lin_recurrence_relation([1,1],[0,1]) # this is the fibonacci recurrence

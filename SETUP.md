Windows:
	install python:
		open powershell
		$ python
		install
		go back to powershell
		$ python3
		> C:\Users\Nashir>python
		Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32                          Type "help", "copyright", "credits" or "license" for more information.
		>>> print("hello :)")
		hello :)
		if you can do the above, python is installed
	upgrade pip:
		open powershell
		$ python3 -m pip install --upgrade pip
	install git: https://git-scm.com/download/
		open powershell
		$ git status
		fatal: not a git repository (or any of the parent directories): .git                                                                                                 Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32                          Type "help", "copyright", "credits" or "license" for more information.
		if you see the above line, then git is installed
	download project:
		open powershell
		$ cd Documents
		$ git clone https://github.com/nashirj/discrete-math-algorithms
		$ cd discrete-math-algorithms
		$ pip3 install -r requirements.txt
		$ python discretemath\view.py

OSX:
	install homebrew:
	install python3: `$ brew install python3`
	test python (see windows instructions)
	install and test git (see windows instructions)
	download and run project:
		open terminal
		$ cd Documents
		$ git clone https://github.com/nashirj/discrete-math-algorithms
		$ cd discrete-math-algorithms
		$ pip3 install -r requirements.txt
		$ python discretemath/view.py


Linux:
	test python3 (see windows instructions)
	install tkinter: `$ sudo apt-get install python3-tk`
	install pip3 (note, it usually comes default with Python): `$ sudo apt-get install python3-pip`
	download and run project:
		open terminal
		$ cd Documents
		$ git clone https://github.com/nashirj/discrete-math-algorithms
		$ cd discrete-math-algorithms
		$ pip3 install -r requirements.txt
		$ python discretemath/view.py



General usage:
	Run the GUI from the top level directory with the command `python3 discretemath/view.py` (OSX/Linux) or `python3 discretemath\view.py` (Windows)
	Import specific packages from the `discretemath` module as follows:
		python3
		from discretemath.py import bell
		help(bell)
		bell.bell_dp(10)
		from discretemath.py import recurrence
		recurrence.solve_lin_recurrence_relation([1,1],[0,1]) # this is the fibonacci recurrence
tkinter is needed to run the GUI. on linux, can install with the command `sudo apt-get install python3-tk`
After installing tkinter, install all dependencies with `pip3 install -r requirements.txt`
If pip3 is not yet installed, do so with the command `sudo apt-get install python3-pip` on linux, `brew install python3` on OSX (requires homebrew)
Run the GUI from the top level directory with the command `python3 discretemath/view.py`
Import specific packages from the `discretemath` module as follows:
	python3
	from discretemath.py import bell
	help(bell)
	bell.bell_dp(10)
	from discretemath.py import recurrence
	recurrence.solve_lin_recurrence_relation([1,1],[1,1]) # this is the fibonacci recurrence
	
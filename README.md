# discretemath

`discretemath` is a Python library that implements various algorithms and processes from discrete math.

## Installation

See the instructions in [SETUP.md](https://github.com/nashirj/discrete-math-algorithms/blob/master/SETUP.md) for installing discretemath.

## Usage

```python
from discretemath.py import sets
from discretemath.py import fib

pset = sets.generate_power_set([1, 'blah']) #  [[], [1], ['blah'], [1, 'blah']]

print(fib.fibonacci_dp(100)) # 354224848179261915075
```

The GUI can be run from the top level directory with the command `python discretemath/view.py` after the instructions in SETUP.md have been followed.

![GUI](https://github.com/nashirj/discrete-math-algorithms/blob/master/misc/gui.png)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/gpl-3.0/)
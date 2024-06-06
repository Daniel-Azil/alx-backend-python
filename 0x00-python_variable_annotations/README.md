# 0x00. Python - Variable Annotations

## Description
This project covers the use of type annotations in Python, including specifying function signatures and variable types, duck typing, and validating code with `mypy`. The goal is to improve code readability and reliability by using type hints.

## Files and Descriptions

### `0-add.py`
Defines a type-annotated function `add` that takes two floats as arguments and returns their sum as a float.

### `1-concat.py`
Defines a type-annotated function `concat` that takes two strings as arguments and returns their concatenated string.

### `2-floor.py`
Defines a type-annotated function `floor` which takes a float as an argument and returns the floor of the float as an integer.

### `3-to_str.py`
Defines a type-annotated function `to_str` that takes a float as an argument and returns the string representation of the float.

### `4-define_variables.py`
Defines and annotates the following variables:
- `a`: an integer with a value of 1
- `pi`: a float with a value of 3.14
- `i_understand_annotations`: a boolean with a value of True
- `school`: a string with a value of "Holberton"

### `5-sum_list.py`
Defines a type-annotated function `sum_list` which takes a list of floats and returns their sum as a float.

### `6-sum_mixed_list.py`
Defines a type-annotated function `sum_mixed_list` which takes a list of integers and floats and returns their sum as a float.

### `7-to_kv.py`
Defines a type-annotated function `to_kv` that takes a string and an int or float as arguments and returns a tuple. The first element is the string, and the second element is the square of the int/float annotated as a float.

### `8-make_multiplier.py`
Defines a type-annotated function `make_multiplier` that takes a float as an argument and returns a function that multiplies a float by the given float.

### `9-element_length.py`
Defines a function `element_length` that takes an iterable of sequences and returns a list of tuples, each containing a sequence and its length. The function's parameters and return values are annotated with appropriate types.

### `100-safe_first_element.py`
Augments a function `safe_first_element` with correct duck-typed annotations. The function returns the first element of a sequence if it exists, otherwise returns None.

### `101-safely_get_value.py`
Adds type annotations to a function `safely_get_value` that retrieves a value from a dictionary by key, returning a default value if the key is not present.

### `102-type_checking.py`
Uses `mypy` to validate a function `zoom_array` that takes a tuple of integers and an optional factor (default is 2), and returns a list of integers, with each element repeated by the factor.

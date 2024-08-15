# GCD Calculator

This project defines a simple command-line program to calculate the Greatest Common Divisor (GCD) of two integers. It utilizes a recursive approach based on the Euclidean algorithm, along with a helper function to swap the values of two integers.

## Features

- Computes the GCD of two integers
- Utilizes a recursive algorithm for efficiency.
- Includes a helper function to swap integers.

## Requirements

Python 3.5 or higher

## Usage

1. Clone the repository:

```SHELL
git clone https://github.com/Mahdishk/Algorithm_Arena_EX.git
cd gcd-calculator
```

2. Run the program:

```SHELL
python src/main.py
```

3. Follow the prompts to input two integers.

## Code Explanation

### Functions

- **swap(a: int, b: int) -> tuple[int, int]:**  Swaps two integers and returns them as a tuple in reversed order.

- **gcd(a: int, b: int) -> int:**

    - Takes two integers as input and computes their GCD using the Euclidean algorithm recursively.
    - The function first checks if ``a`` is less than ``b`` and swaps them if necessary.
    - If ``b`` is zero, it returns ``a`` as the GCD. Otherwise, it recursively calls itself with the parameters ``b`` and ``a % b``.

### Main Block

- The program prompts the user to input two integers and displays the GCD calculated by the ``gcd`` function.
- Error handling is included to ensure valid integer input.


## Example

```
Enter number: 48
Enter another number: 18
GCD using custom function: 6
GCD using built-in function: 6
```

## License

This project is licensed under the MIT License.
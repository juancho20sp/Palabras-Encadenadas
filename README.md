# Palabras Encadenadas!
# Let's operate complex numbers!

This is a repository for the game *Palabras Encadenadas*, a basic game done in Python.

## Getting Started

For running this game you need to have Python installed in your computer.

### Prerequisites
To run these files you need to have Python installed in your computer, at least the version 3.7. <br/>
You can check your Python version typing on cmd:

```
python --version
```

### Installing
- Clone this git repository into your computer.
- Open the [file]() in your code editor.
- Run it

```
# In your root folder:

git clone https://github.com/juancho20sp/Complex-Calculator

# In your python file:

from library import *
```
### How to implement it
- Paste the  [library.py](https://github.com/juancho20sp/Complex-Calculator/blob/master/Vectors%20and%20Arrays%20Library/library.py) file in the folder you´re currently working.
- On the Python file you want to use the library type: 
```python
from library import *
```
- Call the function you want as the example
```python
library.add(a, b) # Add two complex numbers: a and b
```
## Functions
```python
  from library import *
  
  library.add(a, b) # Add two complex numbers: a and b
  library.substract(a, b) # Substract two complex numbers: a and b
  library.multiply(a, b) # Multiply two complex numbers: a and b
  library.divide(a, b) # Divide two complex numbers: a and b
  library.conjugate(a) # Returns the conjugate of a given complex number
  library.module(a) # Returns the module of a given complex number
  library.polar(a) # Returns the given complex number in polar coordinates
  library.phase(a) # Returns the fase of a given complex
  
  library.add_arrays(m1, m2) # Add two multidimensional arrays, in case they have the same dimensions
  library.inverse_matrix(m1) # Returns a matrix where every item is the inverse of its corresponding in m1
  library.scalar_product(scalar, m1) # Returns the scalar product between 'scalar' and 'm1'. 'scalar' might be an integer or a complex number.
  library.transpose(m1) # Returns the given array BUT transposed
  library.conjugate_mx(m1) # Returns the given array conjugated, in case it has COMPLEX values
  library.adjoint(m1) # Returns the adjoint of the given array 
  library.multiply_mx(m1, m2) # Returns the product of (Array M1 x Array M2)
  library.trace(m1) # Returns the sum of the elements of the diagonal of the matrix
  library.inner_product(m1, m2) # Returns the inner product of <m1, m2>
  liibrary.norm(m1) # Returns the norm of the given array
  library.is_hermitian(m1) # Returns True if the given array is Hermitian, False otherwise
  library.inner(v1, v2) # Returns the inner product between two vectors
  library.norm_vector(v1) # Returns the norm of the given vector
  library.tensor(m1, m2) # Returns the tensor product between m1 and m2
  library.distance(v1, v2) # Returns the distance between two vectors
  library.action(m1, v2) # Returns the action between an array and a vector. IMPORTANT! If the array is a complex array (array of tuples), the vector must be written as a vector of complex numbers, even if it is real
  library.is_unitary(m1) # Returns 'True' if the given 2x2 array is unitary, 'False' otherwise
  
  ```
  
 ### Special Functions
   ```python
   library.prettyPrinting(tuple) # Basically prints the complex numbers (saved as tuples) in a *stylish* way: a + bi
   library.summable(m1, m2) # Checks if both multidimensional arrays have the same dimension
   library.substract_by_element(v1, v2) # Returns a vector whose each component are the substract V1 - V2 
   library.det(m1) # Returns the determinant of a 2x2 array
   ```

## Programming Drills (Chapter 3)!
The [Programming_drills.py](https://github.com/juancho20sp/Complex-Calculator/blob/master/Programming_drills.py) is a Python file that contains some exercises of the third chapter of the book "Quantum Computing for Computer Scientists" <br/>
You will find these functions:
- Boolean system.
- Probabilistic system.
- Three slits.
- Quantum slits.

### Functions of the programming drills!
```python
lets_graph(vector) # Graphs the given state vector asa bar chart. 
requirements(matrix) # Checks if the given matrix is doubly sthocastic, this function is used by all the programs of the file.
boolean_system(matrix, state, clicks) # Using the given adjacency matrix, the state (a vector) and clicks (time-stamps) returns the behaviour of the system as a vector.
probabilistic_system(matrix, state, clicks) # Using the given adjacency matrix, the state (a vector) and clicks (time-stamps) returns the behaviour of the system as a vector.
three_slits(matrix, state, clicks) # Using the given adjacency matrix, the state (a vector) and clicks (time-stamps) returns the behaviour of the three-slits system as a vector.
quantum_slits(matrix, state, clicks) # Using the given adjacency matrix (must be a matrix of tuples), the state (a vector of tuples) and clicks (time-stamps) returns the behaviour of the quantum system as a vector.
multiple_slits() # This is the function you need to call if you want to create your own slit experiment with your own probabilities.
multiple_quantum_slits() # This is the function you need to call if you want to create your own quantum-slit experiment with your own probabilities.
```

## Programming Drills (Chapter 4)!
The [Programming_drills.py](https://github.com/juancho20sp/Complex-Calculator/blob/master/Programming_drills_4.py) is a Python file that contains some exercises of the fourth chapter of the book "Quantum Computing for Computer Scientists" <br/>
You will find these exercises solved:
- Programming Drill 4.1.1
- Programming Drill 4.2.1
- Programming Drill 4.3.1
- Programming Drill 4.4.1

### Functions of the programming drills!
```python
mod_ket(ket) # Returns the norm of the given ket, where ket is a list of tuples. 
find_prob(value, mod) # Returns the probability of getting 'value' in a given ket, where 'mod' is the module of the ket.
normalize_ket(ket) # Returns the given ket, normalized.
transition(ket_1, ket_2) # Returns the probability of transitioning  from ket_1 to ket_2.
expected_value(ohm, ket) # Returns the expected value (or mean) of the observable 'ohm' (as list of tuples) in the state 'ket' (also as a list of tuples).
Variance(ohm, ket) # Returns the variance with the observable 'ohm' and the ket state vector 'ket'

```

## Let's run the tests!
- For running the automated tests of the [Complex Calculator](https://github.com/juancho20sp/Complex-Calculator/blob/master/library.py), just open the [testlib.py](https://github.com/juancho20sp/Complex-Calculator/blob/master/Vectors%20and%20Arrays%20Library/testLib.py) file in your favorite editor and run it.
- For running the automates tests of the [Programming drills](https://github.com/juancho20sp/Complex-Calculator/blob/master/Programming_drills.py), just open the [test_drills.py](https://github.com/juancho20sp/Complex-Calculator/blob/master/test_drills.py) file in your code editor and run it.

### Breaking down the tests
You will find a variety tests for each function, trying to get over all the possibilities. <br/>
An example will look like:

```
  A = [[1, 2, 3], [4, 5, 6]]
  B = [[1, 2, 3, 4], [5, 6, 7, 8]]
  C = [1, 2, 3]
  D = [[(101, 10), (1, 1), (1, 1)], [(2, 2), (2, 2), (2, 2)]]

  self.assertEqual(transpose(A), [[1, 4], [2, 5], [3, 6]])
  self.assertEqual(transpose(B), [[1, 5], [2, 6], [3, 7], [4, 8]])
  self.assertEqual(transpose(C), [[1], [2], [3]])
  self.assertEqual(transpose(D), [[(101, 10), (2, 2)], [(1, 1),(2, 2)], [(1, 1), (2, 2)]])
```

## Double slit challenge!
Simulations of this experiment can be found in the file [Programming_drills.py](https://github.com/juancho20sp/Complex-Calculator/blob/master/Programming_drills.py)

### How to run them?
```
# In your working directory:

git clone https://github.com/juancho20sp/Complex-Calculator
```
```python
# In your python file:

from Programming_drills import *

Programming_drills.probabilistic_system(matrix, state, clicks) # Matrix: the adjacency matrix, state: the initial state and clicks: time clicks
Programming_drills.three_slits(matrix, state, clicks) # Matrix: the adjacency matrix, state: the initial state and clicks: time clicks
Programming_drills.multiple_slits() # Calling this function will start the setup for the experiment.
```


## Built With

* [Python 3.8](https://www.python.org/) - As the main programming language.



## Author

* **Juan David Murillo** - *Main work* - [Github](https://github.com/juancho20sp) | [Twitter](https://twitter.com/juancho20sp)<br/>
Student at: [Escuela Colombiana de Ingeniería Julio Garavito](https://www.escuelaing.edu.co/es/) <br/>
2020 



## License

This is an *open source* project.

### Thanks for checking out!



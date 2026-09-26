
## Array Creation

- array -> Always creates a new copy of the object in memory (by default). 

- asarray -> Avoids copying if the input is already an ndarray with matching parameters.


## Multiplication

- inner -> Calculates the inner product.

- outer -> Calculates the outer product.


## Empty Arrays

- empty -> Creates an uninitialized array of specified shape and dtype.

## Triangular Lower

- tril -> Returns the lower triangular part of an array, setting elements above the k-th diagonal to zero.

## Useful Functions

- where -> Replaces elements based on a condition. It can be used to select elements from two arrays based on a boolean condition.

- x[mask] = mask_value -> This is a way to assign value to elements of an array `x` where the `mask` is True. The `mask_value` will be assigned to those positions in `x`.
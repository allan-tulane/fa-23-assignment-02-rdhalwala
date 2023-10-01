"""
CMPS 2200  Assignment 2.
See assignment-02.pdf for details.
"""
import time


class BinaryNumber:
  """ done """

  def __init__(self, n):
    self.decimal_val = n
    self.binary_vec = list('{0:b}'.format(n))

  def __repr__(self):
    return ('decimal=%d binary=%s' %
            (self.decimal_val, ''.join(self.binary_vec)))


## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.
def binary2int(binary_vec):
  if len(binary_vec) == 0:
    return BinaryNumber(0)
  return BinaryNumber(int(''.join(binary_vec), 2))


def split_number(vec):
  return (binary2int(vec[:len(vec) // 2]), binary2int(vec[len(vec) // 2:]))


def bit_shift(number, n):
  # append n 0s to this number's binary string
  return binary2int(number.binary_vec + ['0'] * n)


def pad(x, y):
  # pad with leading 0 if x/y have different number of bits
  # e.g., [1,0] vs [1]
  if len(x) < len(y):
    x = ['0'] * (len(y) - len(x)) + x
  elif len(y) < len(x):
    y = ['0'] * (len(x) - len(y)) + y
  # pad with leading 0 if not even number of bits
  if len(x) % 2 != 0:
    x = ['0'] + x
    y = ['0'] + y
  return x, y


def subquadratic_multiply(x, y):
  ### TODO
  #make both same length
  xvec = x.binary_vec
  yvec = y.binary_vec
  xvec, yvec = pad(xvec, yvec)
  n = len(xvec)
  n_h = len(xvec)

  #Base case
  if n == 0:
    return 0
  elif n == 1:
    return BinaryNumber(xvec.decimal_val * yvec.decimal_val)

  else:
    #find the first half and second half of strings.
    first_l, first_r = split_number(xvec)
    second_l, second_r = split_number(yvec)

    #Recursively call subquadratic
    #3 products wih n/2
    product_1 = subquadratic_multiply(first_l, second_l)
    product_2 = subquadratic_multiply(first_r, second_r)
    product_3 = subquadratic_multiply(
        bit_shift(first_l.decimal_val + first_r.decimal_val, 1),
        bit_shift(second_l.decimal_val + second_r.decimal_val, 1))

    result = product_1.decimal_val + (
        product_2.decimal_val - product_1.decimal_val - product_3.decimal_val
    ) * (2**n_h) + product_3.decimal_val * (2**(2 * n_h))

    return BinaryNumber(result)


def time_multiply(x, y, f):
  start = time.time()
  subquadratic_multiply(4878, 7234)
  # multiply two numbers x, y using function f
  return (time.time() - start) * 1000

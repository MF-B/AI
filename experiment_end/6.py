import numpy as np
class TestGet:
   def get_at(self, in_array, in_row, in_col):
      out_value = in_array[in_row, in_col]
      return out_value


get_obj = TestGet()
array_int8 = np.array([[1, 2], [3, 4]])
value_got = get_obj.get_at(array_int8, 1, 1)
print(array_int8)
print(value_got)

def get_at(in_array,in_row,in_col):
  out_value = in_array[in_row, in_col]
  return out_value


array_int8 = np.array([[1,2],[3,4]])
value_got = get_at(array_int8,1,1)
print(array_int8)
print(value_got)
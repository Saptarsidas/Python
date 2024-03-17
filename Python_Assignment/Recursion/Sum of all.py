# Write a recursive Python function to calculate the sum of all elements in a list.
def sum_recursive(n):
  if len(n) == 0:
    return 0
  else:
    return n[0] + sum_recursive(n[1:])
my_list = [1, 2, 3, 4, 5]
result = sum_recursive(my_list)
print(result)

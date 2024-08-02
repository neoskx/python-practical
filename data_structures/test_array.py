def test_array():
  arr = [1, 2, 3, 4, 5]
  assert len(arr) == 5

  # Create
  arr.append(6)
  assert arr[-1] == 6

  # Read
  assert arr[0] == 1

  # Update
  arr[0] = 10
  assert arr[0] == 10

  # Delete
  del arr[-1]
  assert arr == [10, 2, 3, 4, 5]
  arr.remove(3) # by value
  assert arr == [10, 2, 4, 5]
  assert arr.pop(0) == 10 # pop by index
  assert arr == [2, 4, 5]
  ## list comprehension 
  arr1 = [x for x in arr if x != 4]
  arr2 = [arr[x] for x in range(len(arr)) if x!=1]
  assert arr1 == [2, 5]
  assert arr1 == arr2
  assert arr == [2, 4, 5]

  # Insert
  arr.insert(1, 3)
  assert arr == [2, 3, 4, 5]
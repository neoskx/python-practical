def test_string():
  my_str = "abcdef"

  # Get
  assert len(my_str) == 6
  assert my_str[0] == 'a'
  assert my_str[0] == "a"
  assert ord(my_str[0]) == 97
  assert chr(97) == 'a'

  # Update
  try:
    my_str[0] = "A"
  except Exception as err:
    assert isinstance(err, TypeError)
  
  # Update specific index 
  my_str = my_str[:3]+"D"+my_str[4:]
  assert my_str == "abcDef"
  my_str = "".join([my_str[:3], 'd', my_str[4:]])
  assert my_str == "abcdef"
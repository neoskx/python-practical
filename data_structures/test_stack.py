def test_stack():
  stack = []
  stack.append(1)
  stack.append(2)
  stack.append(3)

  assert len(stack) == 3
  last_elm = stack.pop()
  assert last_elm == 3
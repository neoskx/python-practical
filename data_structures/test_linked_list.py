class Node:
  def  __init__(self, value):
        self.value = value
        self.next = None

def test_linked_list():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)

    assert head.value == 1
    assert isinstance(head.next, Node) == True
    assert head.next.next.value == 3
    assert head.next.next.next == None
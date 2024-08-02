def test_list():
    my_list = [1, 2, 3, 4, 5]
    assert len(my_list) == 5

    # Create
    my_list.append(6)
    assert my_list[-1] == 6

    # Read
    assert my_list[0] == 1

    # Update
    my_list[0] = 10
    assert my_list[0] == 10

    # Delete
    del my_list[-1]
    assert my_list == [10, 2, 3, 4, 5]
    my_list.remove(3)  # by value
    assert my_list == [10, 2, 4, 5]
    assert my_list.pop(0) == 10  # pop by index
    assert my_list == [2, 4, 5]
    # list comprehension
    my_list1 = [x for x in my_list if x != 4]
    my_list2 = [my_list[x] for x in range(len(my_list)) if x != 1]
    assert my_list1 == [2, 5]
    assert my_list1 == my_list2
    assert my_list == [2, 4, 5]

    # Insert
    my_list.insert(1, 3)
    assert my_list == [2, 3, 4, 5]


def test_tuple():
    my_tuple = (1, 2, 3, 4, 5)

    assert len(my_tuple) == 5

    # Get
    assert my_tuple[3] == 4

    # tuple is immutable
    try:
        my_tuple[0] = 10
    except TypeError as err:
        assert isinstance(err, TypeError) == True


def test_set():
    my_set = {1, 1, 3, 3, 2, 5, 4}

    assert my_set == {1, 2, 3, 4, 5}

    # create
    my_set.add(10)
    assert my_set == {1, 2, 3, 4, 5, 10}
    my_set.add(7)
    assert my_set == {1, 2, 3, 4, 5, 7, 10}

    # Get
    assert len(my_set) == 7
    
    assert (7 in my_set) == True
    assert (8 in my_set) == False

    # Update
    try:
        assert my_set[0] == 1
    except Exception as err:
        assert isinstance(err, TypeError)

    my_set.update([6, 8])
    assert my_set == {1, 2, 3, 4, 5, 6, 7, 8, 10}

    # Delete
    # Remove specific element
    my_set.remove(6)
    assert my_set == {1, 2, 3, 4, 5, 7, 8, 10}
    try:
        my_set.remove(6)
    except Exception as err:
        assert isinstance(err, KeyError)
    my_set.discard(7)
    assert my_set == {1, 2, 3, 4, 5, 8, 10}
    my_set.discard(7)
    assert my_set == {1, 2, 3, 4, 5, 8, 10}
    val = my_set.pop()
    assert val == 1
    assert my_set == {2, 3, 4, 5, 8, 10}
    my_set.clear()
    assert len(my_set) == 0
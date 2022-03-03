from sliding_window import highest_sum_list

def test_can_find_highest_consecutive_list_sum_in_a_list():
    result = highest_sum_list([1,2,3,4], 2)
    assert result == 7

def test_can_find_highest_consecutive_list_sum_in_a_list():
    result = highest_sum_list([3,5,3,4,6,7,4], 4)
    assert result == 21

def test_shuld_return_0_if_lis_is_empty():
    result = highest_sum_list([],5)
    assert result == 0
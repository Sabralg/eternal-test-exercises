def test_number_list():
    """test for reponse(question=xxx).

    Expected behavior:
    - when question is '*' (everything), the function must return the string '42'
    - when question is 'quoi', the function must return 'feur'
    - when question is anything else or is absent, the function must return 'non'
    """
    from number_list import convert_to_integer
    assert convert_to_integer([12,13,15]) == [12,13,15]
    assert convert_to_integer(["a","b","c"]) == []
    assert convert_to_integer([1,"1",1.1]) == [1,1,1]
    assert convert_to_integer(["1","a",1]) == [1,1]
    assert convert_to_integer([]) == []
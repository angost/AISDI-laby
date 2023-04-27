from pattern import find_naive, find_KMP, find_KR
import pytest

def test_naive_simple():
    text = "ALA MA MALEGO KOTA"
    pat = "MALEGO"
    assert find_naive(pat, text) == [7]

def test_naive_multiple():
    text = "ALA MA MALEGOMALEGO KOTA"
    pat = "MALEGO"
    assert find_naive(pat, text) == [7,13]

def test_naive_one_letter_pattern_spread():
    text = "ALA MA MALEGO KOTA"
    pat = "A"
    assert find_naive(pat, text) == [0, 2, 5, 8, 17]

def test_naive_one_letter_pattern_together():
    text = "AAAA"
    pat = "A"
    assert find_naive(pat, text) == [0, 1, 2, 3]

def test_naive_intersecting_one_letter():
    text = "AAAA"
    pat = "AA"
    assert find_naive(pat, text) == [0, 1, 2]

def test_naive_intersecting_more_letters():
    text = "AAAA"
    pat = "AAA"
    assert find_naive(pat, text) == [0, 1]

def test_naive_part_same():
    text = 'MMAMMANN'
    pat = 'MANN'
    assert find_naive(pat, text) == [4]

def test_naive_not_full():
    text = 'ABCDE'
    pat = 'CDEF'
    assert find_naive(pat, text) == []

def test_naive_pattern_longer():
    text = 'ABCD'
    pat = 'ABCDE'
    assert find_naive(pat, text) == []

    text = 'ABCDEF'
    pat = 'XYZXYZXYZ'
    assert find_naive(pat, text) == []

def test_naive_no_pattern_in_text():
    text = 'AABAABAAB'
    pat = 'AC'
    assert find_naive(pat, text) == []

def test_naive_text_empty():
    text = ''
    pat = 'AC'
    assert find_naive(pat, text) == []

def test_naive_pattern_empty():
    text = 'ABC'
    pat = ''
    assert find_naive(pat, text) == []

    text = ''
    pat = ''
    assert find_naive(pat, text) == []

def test_naive_pattern_last():
    text = "BCA"
    pat = "A"
    assert find_naive(pat, text) == [2]


def test_KMP_simple():
    text = "ALA MA MALEGO KOTA"
    pat = "MALEGO"
    assert find_KMP(pat, text) == [7]

def test_KMP_multiple():
    text = "ALA MA MALEGOMALEGO KOTA"
    pat = "MALEGO"
    assert find_KMP(pat, text) == [7,13]

def test_KMP_one_letter_pattern_spread():
    text = "ALA MA MALEGO KOTA"
    pat = "A"
    assert find_KMP(pat, text) == [0, 2, 5, 8, 17]

def test_KMP_one_letter_pattern_together():
    text = "AAAA"
    pat = "A"
    assert find_KMP(pat, text) == [0, 1, 2, 3]

def test_KMP_intersecting_one_letter():
    text = "AAAA"
    pat = "AA"
    assert find_KMP(pat, text) == [0, 1, 2]

def test_KMP_intersecting_more_letters():
    text = "AAAA"
    pat = "AAA"
    assert find_KMP(pat, text) == [0, 1]

def test_KMP_part_same():
    text = 'MMAMMANN'
    pat = 'MANN'
    assert find_KMP(pat, text) == [4]

def test_KMP_not_full():
    text = 'ABCDE'
    pat = 'CDEF'
    assert find_KMP(pat, text) == []

def test_KMP_pattern_longer():
    text = 'ABCD'
    pat = 'ABCDE'
    assert find_KMP(pat, text) == []

    text = 'ABCDEF'
    pat = 'XYZXYZXYZ'
    assert find_KMP(pat, text) == []

def test_KMP_no_pattern_in_text():
    text = 'AABAABAAB'
    pat = 'AC'
    assert find_KMP(pat, text) == []

def test_KMP_text_empty():
    text = ''
    pat = 'AC'
    assert find_KMP(pat, text) == []

def test_KMP_pattern_empty():
    text = 'ABC'
    pat = ''
    assert find_KMP(pat, text) == []

    text = ''
    pat = ''
    assert find_KMP(pat, text) == []


def test_KMP_pattern_last():
    text = "BCA"
    pat = "A"
    assert find_KMP(pat, text) == [2]
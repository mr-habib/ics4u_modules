from binary import *

def test_text2bin1():
    assert text2bin("Hello") == "0100100001100101011011000110110001101111"
def test_text2bin2():
    assert text2bin("") == ""

def test_bin2text1():
    assert bin2text("01100110011100100110010101110011011011100110010101101100") == "fresnel"
def test_bin2text2():
    assert bin2text("") == ""

def test_chr2bin1():
    assert chr2bin("q") == "01110001"
def test_chr2bin2():
    assert chr2bin("f") == "01100110"
def test_chr2bin3():
    assert chr2bin("") == ""

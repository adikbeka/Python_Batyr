import pytest


def get_extension(string):
    a = string.split(".")
    return a[-1]



@pytest.mark.parametrize("a, expected", [("hello.pdf","pdf"), ("write.docx", "docx"), ("world.mp4", "mp4"), ("world.world.pptx", "pptx"), (" ", " ")])
def test_sum(a, expected):

    actual = get_extension(a)

    assert expected == actual
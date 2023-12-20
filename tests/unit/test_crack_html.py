import pytest

from douban_crack.crack_html.crack_html import crack_html

from . import mock_html


def test_parse_search():
    result = crack_html(mock_html("book"))
    assert len(result) == 1
    assert len(result[0]) == 1
    assert len(result[0][0]) == 57

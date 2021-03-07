import pytest

from magic_list import MagicList


def test_skip_boundary_check_with_0():
    # Given a magic list
    # When accessing it with "valid"  boundary check
    # We wish to add the value to the list.
    a = MagicList()
    a[0] = 5
    assert a[0] == 5


if __name__ == '__main__':
    pytest.main()

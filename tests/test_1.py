# test_google.py

import pytest

class Test1(pytest.TestCase):

    def test_standard_date(self):
        print("Hello World")
        
        assert 2 + 2 == 4

if __name__ == '__main__':
    pytest.main()

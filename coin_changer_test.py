from coin_changer import *

class TestMakeChangeUsd:

    def test_one_cent(self):
        change = make_change_usd(1)
        assert change.__dict__ == ChangeUsd(0, 0, 0, 1).__dict__

    def test_seventy_three_cents(self):
        change = make_change_usd(73)
        assert change.__dict__ == ChangeUsd(2, 2, 0, 3).__dict__


class TestMakeChange:

    def test_one_cent(self):
        values = [1]
        amount = 1
        assert make_change(values, amount) == [1]

    def test_two_cents(self):
        values = [1]
        amount = 2
        assert make_change(values, amount) == [2]

    def test_five_cents(self):
        values = [5, 1]
        amount = 5
        assert make_change(values, amount) == [1, 0]

    def test_seven_cents(self):
        values = [5, 1]
        amount = 7
        assert make_change(values, amount) == [1, 2]

    def test_seven_cents_backwards(self):
        values = [1, 5]
        amount = 7
        assert make_change(values, amount) == [7, 0]

    def test_ninety_seven_cents(self):
        values = [25, 10, 5, 1]
        amount = 97
        assert make_change(values, amount) == [3, 2, 0, 2]

    def test_zero_cents(self):
        values = [25, 10, 5, 1]
        amount = 0
        assert make_change(values, amount) == [0, 0, 0, 0]

    def test_no_values(self):
        values = []
        amount = 23
        assert make_change(values, amount) == []


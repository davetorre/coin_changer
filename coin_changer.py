import pytest

def make_change_usd(amount):
    denominations = [25, 10, 5, 1]
    change = make_change(denominations, amount)
    return ChangeUsd(change[0], change[1], change[2], change[3])

def make_change(values, amount):
    change = []
    for value in values:
        if value <= amount:
            count = amount / value
            amount -= count * value
        else:
            count = 0
        change.append(count)
    return change


class ChangeUsd:
    def __init__(self, quarters, dimes, nickels, pennies):
        self.quarters = quarters
        self.dimes = dimes
        self.nickels = nickels
        self.pennies = pennies


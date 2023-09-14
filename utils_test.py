from utils import utils

def reversedTest(number, reversed):
    if (reversed == utils.reversed(number)):
        return (str(utils.reversed(number)) +  ", Result: Passed")
    else:
        return (str(utils.reversed(number)) +  ", Result: Failed")  

print("Value: 123, Reversed: ", reversedTest("123", 321)) # string
print("Value: 12.3, Reversed: ", reversedTest(12.3, 21)) # float
print("Value: 123, Reversed: ", reversedTest(123, 321)) # int

def formatterTest(number, formatted):
    if (formatted == utils.formatter(number)):
        return ((utils.formatter(number)) +  ", Result: Passed")
    else:
        return ((utils.formatter(number)) +  ", Result: Failed")  

print("Value: 25, Formatted: ", formatterTest("25", "0b11001 0o31")) # string
print("Value: 2.5, Formatted: ", formatterTest(2.5, "0b10 0o2")) # float
print("Value: 123, Formatted: ", formatterTest(25, "0b11001 0o31")) # int
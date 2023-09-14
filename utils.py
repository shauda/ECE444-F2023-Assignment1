
class utils:

    # function to reverse a number
    def reversed(num):
        return int(str(int(num))[::-1])
    
    # function to take a number and return binary and octal versions of it
    def formatter(num):
        binarynum = bin(int(num)) # convert to binary
        octalnum = oct(int(num))  # convert to octal
        return (binarynum + " " + octalnum)

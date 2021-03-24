class RangeExceedError(Exception):
    pass

class Negative_result(Exception):
    pass

class DivisionZeroError(Exception):
    pass

class Type_Error(Exception):
    pass
class Value_Error(Exception):
    pass
a=int(input())
b=int(input())
try:
    if a>10 or b>10:
        raise RangeExceedError
    elif self.a+self.b<0:
        raise Negative_resultError
    elif self.a<0 or self.b<0:
        raise DivisionZeroError
    elif type(self.a)!= int or type(self.b)!=int:
        raise Type_Error
    else:
        raise Value_Error
except RangeExceedError:
    print("Provide the value which is given range")
except Negative_resultError:
    print("Give the positive value")
except DivisionZeroError:
    print("Provide None negative Number")
except Type_Error:
    print("Provide integer data type")
except Value_Error:
    print("Alphabet not found")

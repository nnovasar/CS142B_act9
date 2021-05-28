# Part a

def put_int(i:int): pass

def factorial(i:int)->int:
    if i <= 1:
        return 1
    else:
        return factorial(i-1)*i

def main():
    put_int(factorial(5))


# Part b

def put_bool(s:bool): pass

def main():
    put_bool(True and True)
    put_bool(False or True)

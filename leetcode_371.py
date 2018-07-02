"""
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.
"""
def add_num(m:int,n:int):
    a = m
    b =  0
    while(a != 0):
        a = (m&n)<<1
        b = (m^n)
        m = a
        n = b
    return n
if __name__ == '__main__':
    print(add_num(1,2))
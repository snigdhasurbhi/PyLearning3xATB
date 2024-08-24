class clasi:
    def add(self, a,b):
        return a + b
    def sub(self, a, b):
        return a - b
    def mul(self, a, b):
        return a * b
    def div(self, a, b):
        return a / b
    def mod(self, a, b):
        return a % b
    def pow(self, a, b):
        return a ** b
    def floordiv(self, a, b):
        return a // b
    def and_(self, a, b):
        return a & b
    def or_(self, a, b):
        return a | b
    def xor(self, a, b):
        return a ^ b
    def lshift(self, a, b):
        return a << b
    def rshift(self, a, b):
        return a >> b
    def neg(self, a):
        return -a
    def pos(self, a):
        return +a
    def inv(self, a):
        return ~a
    def not_(self, a):
        return not a
    def bool(self, a):
        return bool(a)
    def int(self, a):
        return int(a)
    def float(self, a):
        return float(a)
    def complex(self, a):
        return complex(a)
    def str(self, a):
        return str(a)
    def repr(self, a):
        return repr(a)
    def ascii(self, a):
        return ascii(a)
    def ord(self, a):
        return ord(a)
    def hex(self, a):
        return hex(a)
    def oct(self, a):
        return oct(a)
    def bin(self, a):
        return bin(a)
    def bytes(self, a):
        return bytes(a)
    def bytearray(self, a):
        return bytearray(a)
    def callable(self, a):
        return callable(a)
    def divmod(self, a, b):
        return divmod(a, b)
    def enumerate(self, a):
        return enumerate(a)

    def filter(self, a, b):
        return filter(a, b)
    def map(self, a, b):
        return map(a, b)

    def zip(self, a, b):
        return zip(a, b)
    def iter(self, a):
        return iter(a)
    def next(self, a):
        return next(a)
    def slice(self, a, b, c):
        return slice(a, b, c)
    def hasattr(self, a, b):
        return hasattr(a, b)
    def getattr(self, a, b):
        return getattr(a, b)
    def setattr(self, a, b, c):
        return setattr(a, b, c)
    def delattr(self, a, b):
        return delattr(a, b)
    def globals(self):
        return globals()
    def locals(self):
        return locals()
    def repr(self, a):
        return repr(a)
    def str(self, a):
        return str(a)
    def hash(self, a):
        return hash(a)
    def type(self, a):
        return type(a)
    def id(self, a):
        return id(a)
    def isinstance(self, a, b):
        return isinstance(a, b)
    def issubclass(self, a, b):
        return issubclass(a, b)
    def callable(self, a):
        return callable(a)
    def getattr(self, a, b):
        return getattr(a, b)
    def setattr(self, a, b, c):
        return setattr(a, b, c)
    def delattr(self, a, b):
        return delattr(a, b)
    def globals(self):
        return globals()
    def locals(self):
        return locals()
    def repr(self, a):
        return repr(a)
    def str(self, a):
        return str(a)


object=clasi()
output=object.pow(2, 3)
print(output)
print(object.add(8, 2))
print(object.sub(10, 2))
print(object.mul(15, 2))
print(object.div(18, 2))
print(object.mod(20, 2))
print(object.floordiv(22, 2))
print(object.and_(23, 2))
print(object.or_(24, 2))
print(object.xor(25, 2))
print(object.lshift(26, 2))
print(object.rshift(27, 2))
print(object.neg(28))
print(object.pos(29))
print(object.inv(30))

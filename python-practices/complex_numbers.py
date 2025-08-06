# Create a Python class names `ComplexNumber` to represent complex numbers.
# A complex number is a number that comprises a real part and imaginary part. 
# It is written in the format of a + bi, where a is real part and b is imaginary part and i is the imaginary unit(sqrt(-1)).

# Operations:
# 1. Additions
# 2. Subtraction
# 3. Multiplication
# 4. Division
# 5. Comparison

class ComplexNumber:
    def __init__(self, real=0, imag=0) -> None:
        self.real = real
        self.imag = imag

    def __str__(self) -> str:
        if self.imag == 0:
            return "0j"
        elif self.imag < 0:
            return f"{self.real}{self.imag}i"
        else:
            return f"{self.real}+{self.imag}i"
    
    def conjugate(self):
        return ComplexNumber(self.real, self.imag * -1)

    def __add__(self, other):
        resultReal = 0
        resultImag = 0
        resultReal = self.real + other.real
        resultImag = self.imag + other.imag
        return ComplexNumber(resultReal, resultImag)

    def __sub__(self, other):
        resultReal = 0
        resultImag = 0
        resultReal = self.real - other.real
        resultImag = self.imag - other.imag
        return ComplexNumber(resultReal, resultImag)

    def __mul__(self, other):
        resultReal = 0
        resultImag = 0
        resultReal = self.real * other.real - self.imag * other.imag
        resultImag = self.real * other.imag + other.real * other.imag
        return ComplexNumber(resultReal, resultImag)

    def __truediv__(self, other):
        resultReal = 0
        resultImag = 0
        den = other.real**2 + other.imag**2
        return self * ComplexNumber(other.real/den, (-1*other.imag)/den)

    def __eq__(self, other):
        return (self.real == other.real) and (self.imag == other.imag)

    def __ne__(self, other):
        return (self.real != other.real) and (self.imag != other.imag)

if __name__ == "__main__":
    c1 = ComplexNumber(1, 2)
    c2 = ComplexNumber(3, 4)
    print(c1)
    print(c2)
    print(c1+c2)
    print(c1-c2)
    print(c1.conjugate())
    print(c1*c2)
    print(c1/c2)
    print(c1==c2)
    print(c1!=c2)

    


        
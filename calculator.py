class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        is_negative = False
        if a < 0 and b < 0:
            a = -a
            b = -b
        elif a < 0:
            a = -a
            is_negative = True
        elif b < 0:
            b = -b
            is_negative = True

        for i in range(b):
            result = self.add(result, a)
        if is_negative:
            result = -result
    
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        result = 0
        is_negative = False
        
        if (a < 0) != (b < 0):  # Check if signs of a and b are opposite
            is_negative = True
    
        a = -a if a < 0 else a
        b = -b if b < 0 else b
        
        while a >= b:
            a = self.subtract(a, b)
            result += 1
        return -result if is_negative else result
    
    def modulo(self, a, b):
        if b == 0:
            raise ValueError("Modulo by zero is not allowed.")
        while a >= b:
            a = a-b
        return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))
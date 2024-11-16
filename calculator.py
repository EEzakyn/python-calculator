class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        #ex return b - a
        return a - b

    def multiply(self, a, b):
        result = 0
        #ex for i in range(b+1)
        if b < 0:
            b = -b
            a = -a
        for i in range(b):
            result = self.add(result, a)
        return result

    def divide(self, a, b):
        if b == 0:
            return "Error divider must not == 0"
        multi = 1
        if a < 0 or b < 0:
            if a < 0 and b < 0:
                multi = 1
            else:
                multi = -1
            a = abs(a)
            b = abs(b)
            
        result = 0
        while a >= b:
            a = self.subtract(a, b)
            result += 1
        
        if multi == -1:
            result = self.multiply(result,multi)
        return result
    
    def modulo(self, a, b):
        if b == 0:
            return "Error divider must not == 0"
        num = self.divide(a,b)
        result = self.subtract(a,self.multiply(b,num))
        
        if self.multiply(a,b) < 0:
            result = result + b
        return result
        
# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(37, -10))
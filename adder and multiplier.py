def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def calculate(a, b, operation):
    if operation == "add":
        return add(a, b)
    elif operation == "multiply":
        return multiply(a, b)
    else: 
        raise ValueError("输入值错误")
    
if __name__ == "__main__":
     a = float(input("Enter the first number: "))
     b = float(input("Enter the second number: "))
     operation = input("Choose operation (add/multiply): ").strip().lower()
    
     
     try:
      result = calculate(a, b, operation)
      print(f"Result of {operation} between {a} and {b}: {result}")
     except ValueError as e:
      print(e)
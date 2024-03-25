from accessSpecifiers import Car

car = Car()
print(car.publicVar)
print(car._protectedVar)
#print(car.__privateVar)
print(car._Car__privateVar) # how we can access the private method

# cl
print(car.publicMethod())
print(car._protectedMethod())
print(car._Car__privateMethod())
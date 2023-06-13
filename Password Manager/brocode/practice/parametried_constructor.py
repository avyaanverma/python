class Addition:
	first = 0
	second = 0
	answer = 0

	# parameterized constructor
	def __init__(self, f, s):
		self.first = f
		self.second = s

	def display(self):
		print("First number = " + str(self.first))
		print("Second number = " + str(self.second))
		print("Addition of two numbers = " + str(self.answer))

	def calculate(self):
		self.answer = self.first + self.second


# creating object of the class
# this will invoke parameterized constructor
obj1 = Addition(1000, 2000)

# creating second object of same class
obj2 = Addition(10, 20)

# perform Addition on obj1
obj1.calculate()

# perform Addition on obj2
obj2.calculate()

# display result of obj1
obj1.display()

# display result of obj2
obj2.display()
'''
I Advantages of using constructors in Python:

1. Initialization of objects:
 Constructors are used to initialize the objects of a class. They allow you to set default values for attributes or properties, and also allow you to initialize the object with custom data.
2. Easy to implement: 
Constructors are easy to implement in Python, and can be defined using the __init__() method.
3. Better readability: Constructors improve the readability of the code by making it clear what values are being initialized and how they are being initialized.
4. Encapsulation: Constructors can be used to enforce encapsulation, by ensuring that the object’s attributes are initialized correctly and in a controlled manner.
II Disadvantages of using constructors in Python:
1. Overloading not supported: Unlike other object-oriented languages, Python does not support method overloading. This means that you cannot have multiple constructors with different parameters in a single class.
2. Limited functionality: Constructors in Python are limited in their functionality compared to constructors in other programming languages. For example, Python does not have constructors with access modifiers like public, private or protected.
3. Constructors may be unnecessary: In some cases, constructors may not be necessary, as the default values of attributes may be sufficient. In these cases, using a constructor may add unnecessary complexity to the code.
'''
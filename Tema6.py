#pylint:disable=W0621
'''
Implement a class that perform mathematical operations (+, -, *, /).

For division, validate to not divide by 0.

Functions must receive two parameters which are used to perform the operations.

The class must also contain two variables, and also have some functions that have no parameters, but further calls back the existing functions with the class variables.

Please test the code with input-output functions, like I said above.
'''
class mate():
	first = {}
	second = {}
	def adunare(self):
		rezultat = "%.2f" % (instance.first + instance.second)
		print(("{0} + {1} =".format(self.first , self.second)), rezultat)
	def scadere(self):
		rezultat = "%.2f" % (instance.first - instance.second)
		print(("{0} - {1} =".format(self.first , self.second)), rezultat)
	def inmultire(self):
		rezultat = "%.2f" % (instance.first * instance.second)
		print(("{0} * {1} =".format(self.first , self.second)), rezultat)
	def impartire(self):
		try:
			rezultat = "%.2f" % (instance.first / instance.second)
			print(("{0} / {1} =".format(self.first , self.second)), rezultat)
		except ZeroDivisionError:
			print("Nu se poate imparti la zero!")
instance = mate()
instance.first = 7
instance.second = 0
instance.adunare()
instance.scadere()
instance.inmultire()
instance.impartire()
		
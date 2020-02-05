class Animal:
 	def __init__(self, name, species):
 		self.name = name
 		self.species = species

 	def __repr__(self):
 		return f"{self.name} is a {self.genus}"

 	def make_noise(self, sound):
 		print(f"this animal says {sound}")

class Snake(Animal):
 	def __init__(self, name, genus, toy):
 		super().__init__(name, species = "snake")
 		self.genus = genus
 		self.toy = toy
 	
 	def play(self):
 		print(f"{self.name} eats the {self.toy}")

chewy = Snake("chewy", "Ball Python", "rat")


print(chewy)
chewy.play()
 


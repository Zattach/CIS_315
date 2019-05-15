import sys

# global variable for the dictionary file name
filename = "diction10k.txt"

# initializer
class HashSet:
	def __init__(self, dictionary : set, line : str):
		self.dictionary = dictionary
		self.line = line
		self.length = len(line)
		self.retArray = list(None for x in range(self.length))	
		self.strArray = []	

# recursive/iterative function
	def split(self, i : int) -> bool:
		if i < self.length:
			if self.retArray[i] is None:
				j = i
				var = False
				while j < self.length:
					word = str(self.line[i:j + 1] + '\n')
					if bool(word in self.dictionary and self.split(j + 1)):
						var = True
						# self.strArray.append(self.line[i:j + 1])
					j += 1
				self.retArray[i] = var
			return self.retArray[i]
		return True

# starts the iterative function
	def iterativeFunction(self) -> bool:
		self.retArray[0] = self.split(0)
		return self.retArray

# function to attempt to order the words
	def strPrep(self):
		i = 0
		while i < self.length:
			j = i
			while j < self.length:
				if self.retArray[i]:
					word = str(self.line[i:j + 1] + '\n')
					if word in self.dictionary:
						self.strArray.append(str(self.line[i:j + 1]))
						i = j + 1
						j = i
				j += 1
			i += 1

# takes in the dictionary and then takes in the number of sentences to make, then runs through sentences
def driver():
	f = open(filename, 'r')
	dictionary = f.readlines()
	f.close()

	sentences = int(input())
	for i in range(sentences):
		line = str(input())
		print("phrase number: " + str(i + 1))
		print(line + '\n')
		h = HashSet(dictionary, line)

		itArray = h.iterativeFunction()
		print("iterative attempt:")
		if itArray[0] is True:
			print("YES, can be split")
			h.strPrep()
			print(*h.strArray)
			print()
		else:
			print("NO, cannot be split\n")

# allows python3 code to run as python
if __name__ == "__main__":
	driver()

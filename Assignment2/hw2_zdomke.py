# Zach Domke
# CIS_315
# 4/22/18

import sys

class Graph:
	# initializes the matrix [out][in]
	def __init__(self, n):
		self.nodes = [0 for x in range(n)]
		self.matrix = [[0 for x in range(n)] for y in range(n)]
		self.shortest = self.longest = -1

	def populateMatrix(self, m):
		i = 0
		while i < m:
			inData = input().split()
			outNode = int(inData[0]) - 1
			inNode = int(inData[1]) - 1
			self.matrix[outNode][inNode] = 1
			i += 1

	def initArray(self, x):
		length = len(self.nodes)
		self.nodes[0] = 0
		i = 1
		while i < length:
			self.nodes[i] = x
			i += 1

	def getPaths(self):
		self.updatePaths()
		return self.nodes[-1]

	def updatePaths(self):
		length = len(self.nodes)
		self.initArray(0)
		self.nodes[0] = 1
		i = 0
		while i < (length - 1):
			j = i + 1
			while j < length:
				if self.matrix[i][j]:
					self.nodes[j] += self.nodes[i]
				j += 1
			i += 1

	def findExtremes(self):
		length = len(self.nodes)
		self.initArray(float('inf'))
		i = 0
		while i < length:
			j = i
			while j < length:
				if self.matrix[i][j]:
					self.relax(i, j)
				j += 1
			i += 1
		self.shortest = self.nodes[-1]
		self.initArray(0)
		i = 0
		while i < length:
			j = i
			while j < length:
				if self.matrix[i][j]:
					self.stress(i, j)
				j += 1
			i += 1
		self.longest = self.nodes[-1]

	def relax(self, i, j) -> int:
		u = self.nodes[i]
		v = self.nodes[j]
		if v > (u + 1):
			self.nodes[j] = u + 1

	def stress(self, i, j) -> int:
		u = self.nodes[i]
		v = self.nodes[j]
		if v < (u + 1):
			self.nodes[j] = u + 1

# takes in how many lines are tested and then adds and multiplies that many times
def driver():
	g = int(input())
	for i in range(g):
		n = int(input())
		m = int(input())
		graph = Graph(n)
		graph.populateMatrix(m)
		paths = graph.getPaths()
		graph.findExtremes()
		print("\ngraph number: " + repr(i + 1))
		print("Shortest path: " + repr(graph.shortest))
		print("Longest path: " + repr(graph.longest))
		print("Number of paths: " + repr(paths) + '\n')

# allows python3 code to run as python
if __name__ == "__main__":
	driver()

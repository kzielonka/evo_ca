import random


class Brut:
	def __init__(self, instance):
		self.instance = instance

	def run(self, iterations):
		n = self.instance.solution_size()
		x = range(n)
		best = 0
		for i in xrange(iterations):
			random.shuffle(x)
			result = self.instance.evaluate(x)
			best = max(best, result)
			#print i, best
		return best
			

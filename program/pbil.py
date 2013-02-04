import random
import sys
from problem import read_instance, evaluate
from plot import plot
from brut import Brut

def one_max(xs):
    return sum([1 for x in xs if x])

class PBIL(object):
    def __init__(self, d, iter):
        self.d = d
        self.iter = iter

    def run(self, f, n, pa, pb, pc):
        ps = self.initial_probability_vector()
        population = self.random_population(ps, n)
        trace = []

        for it in xrange(0, self.iter):
            x = self.best_individual(population, f)
            trace.append(x)
            ps = [ps[i] * (1. - pa) + x[i]*pa for i in xrange(0, self.d)]
            for i in xrange(0, self.d):
                ps[i] = ps[i] * (1. - pc) + self.binary_random(0.5) * pc if random.random() < pb else ps[i]
            population = self.random_population(ps, n)            

        trace.append(x)

        #print ps
        result = self.best_individual(population, f)
        return result, f.evaluate_bin(result), trace


    def best_individual(self, population, instance):
        best_score = None
        best_indiv = None
        for solution in population:
            score = instance.evaluate_bin(solution)
            if not best_score or score > best_score:
                best_score = score
                best_indiv = solution
        return best_indiv

    def binary_random(self, p):
        return random.random() < p

    def initial_probability_vector(self):
        return [0.5]*self.d

    def random_individual(self, ps):
        return [self.binary_random(ps[x]) for x in xrange(0, self.d)]

    def random_population(self, ps, n):
        return [self.random_individual(ps) for x in xrange(0, n)]


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "USAGE: python sga.py <input filename>"
        exit(1)
    else:
        instance = read_instance(sys.argv[1])
        pbil = PBIL(instance.bids_count, 100)
        best, best_score, trace = pbil.run(instance, 20, 0.2, 1./instance.bids_count, 0.1)
        brut = Brut(instance)
        brut_result = brut.run(100*20)
        print instance.evaluate_bin(trace[-1])
        print brut_result
        inst = sys.argv[1].split('/')[-1]
        results = []
        results.append( ([i for i in xrange(len(trace))], map((lambda x: instance.evaluate_bin(x)), trace) ) )
        results.append( ([1, len(trace)-1], [brut_result]*2) )
        plot(results, "PBIL", "%s_%s" % (inst, "pbil.png"))

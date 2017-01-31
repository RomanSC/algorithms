"""

    f(n) = 10n+0.1nlog(n) and g(n)=0.01n2.

"""
from matplotlib import pyplot
import math

vals = range(1, 100)

exp = [x**2 for x in vals]
print(exp)

fn = [10*x+0.1*x*math.log(x) for x in vals]
print(fn)

gn = [0.01*x**2 for x in vals]
print(gn)

pyplot.plot(exp)
pyplot.plot(fn)
pyplot.plot(gn)

pyplot.xlabel('F(n) = F(n - 1) + F(n - 2)')
pyplot.ylabel('Processing time')
pyplot.title("Exponentional vs. Logorithmic.")
pyplot.grid(False)
#pyplot.savefig("graph.png")
pyplot.show()

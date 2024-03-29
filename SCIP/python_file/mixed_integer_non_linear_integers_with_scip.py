# -*- coding: utf-8 -*-
"""mixed-integer non-linear integers with SCIP.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Rws-EACY4AuDO_Fwx92RzY-EaGicYbX-

#mixed-integer non-linear integers

Problem
Max: x+xy

Constraints:

-x+2xy <= 8

2x+y <= 14

2x-y <= 10

0 <= x<= 10

0 <= y<= 10

x integer

#Installation
"""

!pip install -q condacolab
import condacolab
condacolab.install()

!conda install pyscipopt

"""#mixed-integer non-linear integers

#Solution
"""

from pyscipopt import Model

model= Model('example')

#creating Variable

x=model.addVar('x', vtype='INTEGER')
y=model.addVar('y')
z=model.addVar('z')

#objective

model.setObjective(z, sense='maximize')

#Constraints
model.addCons(z==x+x*y)
model.addCons(-x+2*x*y <= 8)
model.addCons(2*x+y <= 14)
model.addCons(2*x-y <= 10)


model.optimize()

solution=model.getBestSol()

print('x:', solution[x])
print('y:', solution[y])
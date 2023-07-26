# -*- coding: utf-8 -*-
"""Non-Convex Problem using Pyomo.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_NEFQLoxIejvtzgpetfZmdn0QcybpB_G

Suppose that you have 3 machines to manufacture shoes and the cost of each machine is :

C1= 0.1*n1^2 +2*n1

C2= 6*n2*n1

c3=7*n3

where Ci is cost for production of machine i ,

ni is the number of shows manufactured in machine

each machine has a limit of production of 1000 shoes

for a total production of 2100 shoes, how many shoes should each machine made in order to minimize the total cost?
"""



"""#Solution

objective Function : min C1+C2+C3

Constraints:

n1+n2+n3= 2100

C1= 0.1n1^2 +2n1

C2= 6n2

c3=7n3

0 <= n1,n2,n3 <=1000

#installation of pyomo
"""

!pip install -q condacolab
import condacolab
condacolab.install()

!pip install pyomo

"""#installation of Solver"""

# Commented out IPython magic to ensure Python compatibility.
# %%capture
# import sys
# import os
# 
# if 'google.colab' in sys.modules:
#     !pip install idaes-pse --pre
#     !idaes get-extensions --to ./bin
#     os.environ['PATH'] += ':bin'

import pyomo.environ as pyo, numpy as np
from pyomo.environ import *
from pyomo.opt import SolverFactory

#creation of the model and variables
model = pyo.ConcreteModel()
model.C = pyo.Var(range(1,4)) #here C is the machine's cost
model.n = pyo.Var(range(1,4), within=Integers, bounds=(0,1000)) #n number of shoes #care about the sequence

C = model.C
n = model.n

#objective function
model.obj = pyo.Objective(expr = pyo.summation(C)) #or (expr= C[1]+C[2]+C[3])

#constraint
model.total = pyo.Constraint(expr = pyo.summation(n) == 2100) # (expr =  n[1]+n[2]+n[3]==2100)
model.C1 = pyo.Constraint(expr = C[1] == 0.01*n[1]*n[1] + 2*n[1])
model.C2 = pyo.Constraint(expr = C[2] == 6*n[2]*n[1])
model.C3 = pyo.Constraint(expr = C[3] == 7*n[3])

#solve
opt = SolverFactory('couenne', executable= '/content/bin/couenne') #gurobi is better,  glpk & cbc won't  work
# opt.options['NonConvex']=2  #this is a parameter of gurobi, gurobi guarentee that it will be a global solution,
opt.solve(model)

#print
print('n1', pyo.value(n[1]))
print('n2', pyo.value(n[2]))
print('n3', pyo.value(n[3]))
print('nTotal', pyo.value(pyo.summation(n)))

print('C1', pyo.value(C[1]))
print('C2', pyo.value(C[2]))
print('C3', pyo.value(C[3]))
print('CTotal', pyo.value(pyo.summation(C)))


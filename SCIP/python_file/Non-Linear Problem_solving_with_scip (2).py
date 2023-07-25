# -*- coding: utf-8 -*-
"""Integer Problem solving with SCIP.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Rws-EACY4AuDO_Fwx92RzY-EaGicYbX-

#Non-Linear Problem

In Pyomo for doing non-linear problem we need to us the solver : "IPOPT" ...this can also do linear but for linear 'Gurobi' 'glpk' ok....for Non-linear function gurobi and glpk will show error!

#Problem


Max: x+xy

Constraints:

-x+2xy <= 8

2x+y <= 14

2x-y <= 10

0 <= x<= 10

0 <= y<= 10

#Installation
"""

!pip install -q condacolab
import condacolab
condacolab.install()

!conda install pyscipopt

"""#Solution"""

from pyscipopt import Model

model= Model('example')

#creating Variable

x=model.addVar('x')
y=model.addVar('y')
z=model.addVar('z')
#objective

model.setObjective(z, sense='maximize') #scip care about objective function. We can use non-linear constraints but we can't use a non-linear
#function with same code as before, for this we can creeate a constrats idea with Z"

#Constraints
model.addCons(z==x+x*y) #for doing non-linear problem use z
model.addCons(-x+2*x*y <= 8)
model.addCons(2*x+y <= 14)
model.addCons(2*x-y <= 10)


model.optimize()

solution=model.getBestSol()

print('x:', solution[x])
print('y:', solution[y])
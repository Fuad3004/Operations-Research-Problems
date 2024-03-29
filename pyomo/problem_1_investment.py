# -*- coding: utf-8 -*-
"""Problem 1: Investment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KoSTUewSZIAC16qmlM3Zz1SEriwrSJt4

Problem:

Steve wish to define the best investments that he should make with his money. He has a total of 10,000 USD and the following options for investment.

* A. Low risk fund with historical gains of 5% per year.
* B. Medium risk fund with historical gains 10% per year.
* C. High risk fund with historical gains of 12% per year.

Steve wish to control the risk of his investments with maximum of

 10% of his money in the investment with high risk,

 20% in the investment with medium risk.

which is the decision of investments in A,B, and C that maximize the return of investment for steve?

#Indexes

A, B , C --> Fund

#Variables

Ra, Rb, Rc ---->>>> Return of investment A,B,C

Ca, Cb, Cc ---->>>> Invested capital in fund A,B,C

#Constraints

Ca+ Cb + Cc = 100,000

Ra= 0.05Ca

Rb= 0.10Cb

Rc= 0.12Cc

0 <= Cb <= 0.2*100,000

0 <= Cc <= 0.1*100,000

#Objective Function

max(Ra + Rb + Rc)

#Installation on Google Colab
"""

!pip install -q condacolab
import condacolab
condacolab.install()

!pip install pyomo

!conda install -c conda-forge glpk

"""#Code"""

import pyomo.environ as pyo

from pyomo.opt import SolverFactory

model= pyo.ConcreteModel()

#parameters and sets
model.setInv = pyo.Set(initialize=['A','B','C'])
model.capital =10000

#Variables
model.C= pyo.Var(model.setInv, bounds=(0,None))
model.R= pyo.Var(model.setInv, bounds=(0,None))

c= model.C
r= model.R

#objective function
model.obj = pyo.Objective(expr = pyo.summation(r), sense=pyo.maximize)

#Constraints

model.C1 = pyo.Constraint(expr = pyo.summation(c) == model.capital)


model.C2 = pyo.Constraint(expr = r['A'] == 0.05*c['A'])

model.C3 = pyo.Constraint(expr = r['B'] == 0.1*c['B'])

model.C4 = pyo.Constraint(expr = r['C'] == 0.12*c['C'])

model.C5 = pyo.Constraint(expr = c['B'] <= 0.2*model.capital)

model.C6 = pyo.Constraint(expr = c['C'] <= 0.1*model.capital)

#Solver

opt= SolverFactory(('glpk'))
model.results= opt.solve(model)

m.pprint()
print('\n\nOF:',pyo.value(model.obj))
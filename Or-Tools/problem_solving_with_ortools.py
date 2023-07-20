# -*- coding: utf-8 -*-
"""Problem solving with OrTools.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pAWgYuOsv7Iv92nnle-vB64EZzNj5tCO

https://developers.google.com/optimization

Note: Only for linear programming where as pyomo works both linear and non-linear programming

OR-Tools is open source software for combinatorial optimization, which seeks to find the best solution to a problem out of a very large set of possible solutions. Here are some examples of problems that OR-Tools solves:

Vehicle routing: Find optimal routes for vehicle fleets that pick up and deliver packages given constraints (e.g., "this truck can't hold more than 20,000 pounds" or "all deliveries must be made within a two-hour window").

Scheduling: Find the optimal schedule for a complex set of tasks, some of which need to be performed before others, on a fixed set of machines, or other resources.

Bin packing: Pack as many objects of various sizes as possible into a fixed number of bins with maximum capacities.

#Problem 1
Max: X+Y

Constraints:

-x+2y <= 8

2x+y <= 14

2x-y <= 10

0 <= x<= 10

0 <= y<= 10



#installation
"""

!pip install ortools

"""#SOlution"""

from ortools.linear_solver import pywraplp

solver = pywraplp.Solver.CreateSolver('GLOP') #which solver you are gonna use. Glop is the solver by google to solve linear programming... when you need to use Gurobi you just need to put the name 'Gurobi'


#Variables
x=solver.NumVar(0,10,'x') #lower bound , upper bound, string
y=solver.NumVar(0,10,'y')

#Constraints

solver.Add(-x+2*y <= 8)
solver.Add(2*x+y <= 14)
solver.Add(2*x-y <= 10)

#Obejective
solver.Maximize(x+y)


#Results:

results = solver.Solve()

#confirm optimal or not

if results==pywraplp.Solver.OPTIMAL: print('optimal found')

print('x:', x.solution_value())

print('y:', y.solution_value())



"""#Problem 2
Max: X+Y

Constraints:

-x+2y <= 7

2x+y <= 14

2x-y <= 10

0 <= x<= 10

0 <= y<= 10

x is an integer
"""

from ortools.linear_solver import pywraplp

solver = pywraplp.Solver.CreateSolver('CBC') #Change GLOP cause it does not work on integer problem

#Variables
x=solver.IntVar(0,10,'x') #lower bound , upper bound, string #For an integer output use IntVar instead of NumVar 
y=solver.NumVar(0,10,'y')

#Constraints

solver.Add(-x+2*y <= 7)
solver.Add(2*x+y <= 14)
solver.Add(2*x-y <= 10)

#Obejective
solver.Maximize(x+y)


#Results:

results = solver.Solve()

#confirm optimal or not

if results==pywraplp.Solver.OPTIMAL: print('optimal found')

print('x:', x.solution_value())

print('y:', y.solution_value())


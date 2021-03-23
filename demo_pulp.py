from pulp import GLPK
from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable


########## Résolution du PL TP2 ex 5 #######


# 1. Création du un modèle
model = LpProblem(name="Demo", sense=LpMaximize)


# 2. Déclaration les variables
x1 = LpVariable('x_1', lowBound=0)
x2 = LpVariable('x_2', lowBound=0, cat='Continuous')
x3 = LpVariable('x_3', lowBound=0)


# 3. Ajout des contraintes
model += (2*x1 + x2 + x3 <= 20 , 'Constraint 1')
model += (3*x1 + x2 + 2*x3 <=30, 'Constraint 2')


# 4. Déclaration de la fonction objective
model += 5*x1 + 3*x2 + 4*x3 , 'Objective Function'

status = model.solve(solver=GLPK(msg=True, keepFiles=True))



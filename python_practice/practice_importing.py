'''
here is a docstring
we will use this to see how we can import from another module
'''

import practice_script as ps

print ps.sample_int
myalg=ps.Algebra(1.5, 5.0)
myalg.multiply()
print myalg.multiply()

for x in [1,3,5]:
#loop over different values for the first argument in the algebra class
    myalg = ps.Algebra(x, 5.0)
    print myalg.add()
 


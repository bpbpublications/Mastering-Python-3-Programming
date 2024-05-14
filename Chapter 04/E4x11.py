# program E4x11.py
# Template
from string import Template
s = Template('${name} was born in ${country}')
print(s.substitute(name='Gandhi', country='India'))
s=Template('${name} plays ${sport}')
print(s.substitute(name='Dhoni', sport='Cricket'))
print(s.substitute(name='Viswanathan Anand', sport='Chess'))

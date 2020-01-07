""" Michael Reece
      177000762
      quad.py    used professors poly function
      6/5/2019  """

from poly import Polynomial

class Quadratic(Polynomial):
    def __init__(self, quad = 0, linear = 0, const = 0):
            Polynomial.__init__(self, (quad,2),(linear,1), (const,0))

            self._a = quad
            self._b = linear
            self._c = const
            
    def addterm(self, coeff, exp):
        ''' first check that the exponent of the term being added is legal'''
        if exp <= 2 and exp > -1:
            Polynomial.addterm(self, coeff, exp)
        else:
            raise Exception('The given exponent is not accepted for quadratic expressions')

        
    def __add__(self, other):
        ''' returns a added Quadratic'''
        add = super().__add__(other)
        coeffs = add.coeffs
        return Quadratic(coeffs[1], coeffs[1], coeffs[1])

    def __sub__(self, other):
        ''' returns a subtracted Quadratic '''
        sub = super().__sub__(other)
        coeffs = sub.coeffs
        return Quadratic(coeffs[1], coeffs[1], coeffs[1])

    def __mul__(self, other):
        ''' returns a Quadratic object if the degree of the result is at most 2'''
        mul = super().__mul__(other)
        if mul.degree() == 2:
            coeffs = added.coeffs
            return Quadratic(coeffs[1], coeffs[1], coeffs[1])
        else:
            return mul

    def scale(self, s):
        ''' returns a Quadratic'''
        scale = Polynomial.scale(self,s)
        coeffs = scale.coeffs
        return Quadratic(coeffs[2], coeffs[1], coeffs[0])

    def roots(self):
        ''' a list containing that single root is returned'''
        roots = []
        a = self._a
        b = self._b
        c = self._c
        if a != 0:
            if b * b > 4*a*c:
                disc = (b ** 2 - 4*a*c) ** .5
                num1 = -b + disc
                num2 = -b - disc
                root1 = num1 / (2*a)
                root2 = num2/ (2*a)
                roots.append(root1)
                roots.append(root2)
            elif b * b == 4*a*c:
                roots.append(-1*b/ (2* a))
        elif b != 0:
            roots.append(-1*c/b)
        elif c != 0:
            pass
        else:
            roots = [0 for x in range(3)]
        return roots

    

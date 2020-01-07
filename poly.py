""" Michael Reece
      177000762
      19/4/2019
      poly.py        """

import math

class Polynomial:
    def __init__(self, *termpairs):
        pairslist = list(termpairs)
        self.coeffs = [0]
        for pr in pairslist:
            coeff, exp = pr

            while len(self.coeffs) <= exp:  # if exp is not a valid index in the list self.coeffs,
                self.coeffs.append(0)       # make it valid by appending 0s.
            self.coeffs[exp] = coeff

    def __str__(self):
        polystr = ""

        # If the polynomial has degree 0, we handle it as a separate special case

        if self.degree() == 0:
            return(str(self.coeffs[0]))

        # The rest of the code handles a polynomial of degree greater than 0

        currentexp = self.degree()

        # First handle the term with highest exponent

        if self.coeffs[currentexp] != 1: # Include the coefficient only if it is not equal to 1
            polystr += str(self.coeffs[currentexp])

        if currentexp > 1:
            polystr += "x^%d"%(currentexp)
        elif currentexp == 1:
            polystr += "x"

        # Now handle all other terms with exponent greater than 1

        currentexp -= 1
        while currentexp > 1:
            if self.coeffs[currentexp] > 0:
                if self.coeffs[currentexp] != 1: # handle coefficient of 1 separately
                    polystr += " + " + str(self.coeffs[currentexp]) + "x^" + str(currentexp)
                else:
                    polystr += " + " + "x^" + str(currentexp)
            elif self.coeffs[currentexp] < 0:
                if abs(self.coeffs[currentexp]) != 1: # handle coefficient of -1 separately
                    polystr += " - " + str(abs(self.coeffs[currentexp])) + "x^" + str(currentexp)
                else:
                    polystr += " - " + "x^" + str(currentexp)
            currentexp -= 1

        # Now handle term with exponent 1
    
        if currentexp == 1:
            if self.coeffs[currentexp] > 0: 
                if self.coeffs[currentexp] != 1:
                    polystr += " + " + str(self.coeffs[currentexp]) + "x"
                else:
                    polystr += " + x"
            elif self.coeffs[currentexp] < 0:
                if abs(self.coeffs[currentexp]) != 1:
                    polystr += " - " + str(abs(self.coeffs[currentexp])) + "x"
                else:
                    polystr += " - x"

        # Now handle constant term (term with exponent 0)
        
        if self.coeffs[0] > 0: 
            polystr += " + " + str(self.coeffs[0])
        elif self.coeffs[0] < 0:
            polystr += " - " + str(abs(self.coeffs[0]))

        return polystr

    def __repr__(self):
        return str(self)

    def degree(self):
        if len(self.coeffs) == 0:
            raise Exception("Error Polynomial.degree: object does not have any terms")
        i = len(self.coeffs) - 1

        # Remove any trailing zeros in list self.coeffs
        while i > 0 and self.coeffs[i] == 0:
            self.coeffs.pop()
            i -= 1

        return len(self.coeffs) - 1 

    def evaluate(self, X):
        answer = 0
        for exp in range(self.degree() + 1):
            answer = answer + (self.coeffs[exp]) * (X**exp)
        return answer

    def addterm(self, coeff, exp):
        if coeff != 0:
            if exp <= self.degree():
                self.coeffs[exp] += coeff

                # if coefficient of highest degree term becomes 0,
                # remove all consecutive 0s at the end of list

                if exp == self.degree() and self.coeffs[exp] == 0:   
                    while self.coeffs[exp] == 0:                 
                        self.coeffs.pop()
                        exp -= 1
            else:
                # if exp is greater than the degree of the polynomial,
                # insert enough 0s at the end of the list
                deg = self.degree()
                for i in range(deg, exp):       
                    self.coeffs.append(0)                       
                self.coeffs[exp] = coeff

    def removeterm(self, exp):
        if exp <= self.degree(): 
            self.coeffs[exp] = 0
    
        if exp == self.degree() and self.coeffs[exp] == 0:    # if coefficient of highest degree term becomes 0,
            while self.coeffs[exp] == 0:                      # remove all consecutive 0s at the end of list
                self.coeffs.pop()
                exp -= 1

    def scale(self, s):
        scale_poly = Polynomial()
        deg = self.degree()
        for exp in range(deg + 1):
            scale_poly.addterm(self.coeffs[exp] * s, exp)
        return scale_poly

    def __add__(self, other):
        sum_poly = Polynomial()
        deg_self = self.degree()
        for exp in range(deg_self + 1):
            sum_poly.addterm(self.coeffs[exp], exp)
        deg_other = other.degree()
        for exp in range(deg_other + 1):
            sum_poly.addterm(other.coeffs[exp], exp)
        return sum_poly

    def __sub__(self, other):
        neg_poly = other.scale(-1)
        return self + neg_poly

    def __mul__(self, other):
        mul_poly = Polynomial()
        deg_self = self.degree()
        deg_other = other.degree()
        for exp_self in range(deg_self + 1):
            for exp_other in range(deg_other + 1):
                mul_poly.addterm(self.coeffs[exp_self] * other.coeffs[exp_other],
                                 exp_self + exp_other)
        return mul_poly

    def __getitem__(self, idx):
        if idx in range(self.degree() + 1):  # if idx is less than or equal to the degree of the polynomial
            return self.coeffs[idx]
        else:
            return 0

    def __setitem__(self, idx, value):
        if value == 0:   # if the new coefficient is 0, we're just removing the term
            self.removeterm(idx)
        elif idx <= self.degree(): 
            self.coeffs[idx] = value
        else: 
            self.addterm(value, idx)

def read_polynomial(polyfilename):
    pfile = open(polyfilename, 'r')
    P = Polynomial()
    for line in pfile:
        L = line.split()
        if len(L) != 0:
            P.addterm(float(L[0]), int(L[1]))
    pfile.close()
    return P

def arith_ops_polys(P, Q):
    print("The degree of the first polynomial is ", P.degree())
    print("The degree of the second polynomial is ", Q.degree())
    print("\nThe sum of the two polynomials:")
    print(P + Q)
    print("\nThe difference of the two polynomials:")
    print(P - Q)
    print("\nThe product of the two polynomials:")
    print(P * Q)
    print("\n")

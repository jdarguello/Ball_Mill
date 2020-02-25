from sympy import *

r, theta = symbols('r, \\theta', real=True, positive=True)

def Radio(pvol):
    """
        Tiene como objetivo proporcionar los límites radiales de la integral.
        pvol -> Porcentaje de volumen
    """
    y = m*x + c
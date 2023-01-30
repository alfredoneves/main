#!/usr/bin/python3

formula = "p(D|E) = p(D)*[p(E|D)/p(E)]"
p_D = float(input("1)probability of fact p(D):"))
p_E = float(input("2)probability of evidence p(E):"))
p_ED = float(input("3)probability of evidence given the fact p(E|D):"))
p_DE = p_D * (p_ED / p_E)
print(formula)
print(p_DE)


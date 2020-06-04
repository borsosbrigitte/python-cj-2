"""
    Scrieti o clasa Fraction(numarator si numitor)
    care sa implementeze urmatoarele metode:
        - __init__: instantiem numarator si numitor
        - __str__ : afisam "numarator/numitor"
        - __add__ : returnam o noua fractie care reprezinta adunarea dintre doua fractii
        - __sub__ : returnam o noua fractie care reprezinta scaderea - primesc other object
        - inverse : returneaza inversa - o noua frractie
"""


class Fraction(object):

    """ Implementare fractie
    """
    def __init__(self, numarator, numitor):
        assert type(numarator) == int and type(numitor) == int, "Folositi int va rog!"
        self.numarator = numarator
        self.numitor = numitor

    def __str__(self):
        """ Afisam numaratorul si numitorul """
        return "<" + str(self.numarator) + "," + str(self.numitor) + ">"

    def __add__(self, other):
        return Fraction(self.numarator*other.numitor + self.numitor*other.numarator, self.numitor*other.numitor)

    def __sub__(self, other):
        return Fraction(self.numarator*other.numitor - self.numitor*other.numitor, self.numitor*other.numitor)

    def __invert__(self):
        return


a = Fraction(1, 3)
b = Fraction(2, 3)

a.__add__(b)
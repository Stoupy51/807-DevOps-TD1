import datetime

class Transaction():

    def __init__(self, montant, date, devise: str = "euro", taux: float = 1, description: str = None):
        assert type(montant) == int or type(montant) == float, "montant doit être un nombre"
        assert type(date) == datetime.datetime, "date doit être un objet datetime"
        assert type(devise) == str, "devise doit être une chaine de caractères"
        assert type(taux) == int or type(taux) == float, "taux doit être un nombre"
        assert type(description) == str or description == None, "description doit être une chaine de caractères"
        self.montant = montant
        self.date = date
        self.devise = devise
        self.taux_conversion_euro = taux
        self.description = description

    def __str__(self):
        return f"Transaction \"{self.description}\" de {self.montant} {self.devise}"

    def getMontant(self):
        return self.montant

    def getDate(self):
        return self.date

    def getDevise(self):
        return self.devise

    def getTauxConversionEuro(self):
        return self.taux_conversion_euro

    def getDescription(self):
        return self.description

    def convertToEuro(self):
        return self.montant * self.taux_conversion_euro    


import unittest

class TestTransactionClass(unittest.TestCase):

    def test_init(self):
        t = Transaction(56, datetime.datetime.now(), "dollar", 1.07, "Donation en dollar")
        self.assertEqual(t.getMontant(), 56)
        self.assertEqual(t.getDevise(), "dollar")
        self.assertEqual(t.getTauxConversionEuro(), 1.07)
        self.assertEqual(t.getDescription(), "Donation en dollar")

    def test_init_error(self):
        with self.assertRaises(AssertionError):
            Transaction("abc", datetime.datetime.now(), "dollar", 1.07, "Donation en dollar")
            Transaction(56, "abc", "dollar", 1.07, "Donation en dollar")
            Transaction(56, datetime.datetime.now(), "abc", "Donation en dollar")

    def test_conversion(self):
        transac = Transaction(56, datetime.datetime.now(), "dollar", 1.07, "Donation en dollar")
        self.assertAlmostEqual(transac.convertToEuro(), 59.92)
        transac2 = Transaction(100, datetime.datetime.now(), "euro", 1, "Donation en euro")
        self.assertAlmostEqual(transac2.convertToEuro(), 100)
        transac3 = Transaction(100, datetime.datetime.now(), "yen", 0.007, "Donation en yen")
        self.assertAlmostEqual(transac3.convertToEuro(), 0.7)

    def test_print(self):
        transac = Transaction(56, datetime.datetime.now(), "dollar", 1.07, "Donation en dollar")
        self.assertEqual(str(transac), "Transaction \"Donation en dollar\" de 56 dollar")

if __name__ == '__main__':
    unittest.main(verbosity=2)
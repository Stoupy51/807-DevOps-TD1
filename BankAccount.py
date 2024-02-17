class BankAccount():
    __name = ""
    __number = 0

    def __init__(self, number, name):
        assert type(number) == int, "number doit être un entier"
        assert type(name) == str, "name doit être une chaine de caractères"
        self.__number = number
        self.__name = name
        self.l_transac = []
        self.solde = 0

    def getNum(self):
        return self.__number

    def getNom(self):
        return self.__name

    def setNom(self, nom):
        assert len(nom) >= 4
        self.__name = nom
 
    def __str__(self):
        return f"Compte {self.__number} de {self.__name}"

    def __len__(self):
        return len(self.l_transac)
  
    def transactionAfter(self, date):
        l = []
        for t in self.l_transac:
            if t.getDate() > date:
                l.append(t)
        return l

    def updateSolde(self):
        solde = 0
        for t in self.l_transac:
            solde += t.convertToEuro()
        self.solde = solde

    def allEuro(self):
        for t in self.l_transac:
            if not t.devise == "euro":
                return False
        return True

    def addTransaction(self, t):
        assert type(t) == Transaction, "t doit être une transaction"
        self.l_transac.append(t)
        self.updateSolde()

import datetime
import unittest
from Transaction import Transaction

class TestBankAccountClass(unittest.TestCase):

    def test_init(self):
        c = BankAccount(12, "Bobby")
        self.assertEqual(c.getNum(), 12)
        self.assertEqual(c.getNom(), "Bobby")
        self.assertEqual(len(c), 0)
        self.assertAlmostEqual(c.solde, 0)

    def test_init_error(self):
        with self.assertRaises(AssertionError):
            BankAccount("abc", "Bobby")
            BankAccount(12, 12)

    def test_add_transaction(self):
        c = BankAccount(12, "Bobby")
        transac = Transaction(56, datetime.datetime.now(), "dollar", 1.07, "Donation en dollar")
        transac.convertToEuro()
        c.addTransaction(transac)
        self.assertEqual(len(c), 1)
        self.assertAlmostEqual(c.solde, 59.92)
        transac2 = Transaction(100, datetime.datetime.now(), "euro", 1, "Donation en euro")
        transac2.convertToEuro()
        c.addTransaction(transac2)
        self.assertEqual(len(c), 2)
        self.assertAlmostEqual(c.solde, 159.92)

    def test_transaction_after(self):
        c = BankAccount(12, "Bobby")
        transac = Transaction(56, datetime.datetime.now(), "dollar", 1.07, "Donation en dollar")
        c.addTransaction(transac)
        transac2 = Transaction(100, datetime.datetime.now(), "euro", 1, "Donation en euro")
        c.addTransaction(transac2)

        self.assertEqual(len(c.transactionAfter(datetime.datetime.now())), 0)
        self.assertEqual(len(c.transactionAfter(datetime.datetime.now() - datetime.timedelta(days=1))), 2)

    def test_print(self):
        c = BankAccount(12, "Bobby")
        self.assertEqual(str(c), "Compte 12 de Bobby")

if __name__ == '__main__':
    unittest.main(verbosity=2)

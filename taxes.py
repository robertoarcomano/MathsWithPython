import numpy as np
import matplotlib.pyplot as plot
from matplotlib import style


def tax2rate(tax_item):
    return (100 - tax_item) / 100


def nz(x):
    tax = np.array([10.5, 17.5, 30, 33, 39])
    income = np.array([14000, 48000, 70000, 180000])
    net = []
    for i in range(len(tax)-1):
        prev_income = income[i-1] if i > 0 else 0
        prev_net = net[i-1] if i > 0 else 0
        net.append(tax2rate(tax[i])*(income[i] - prev_income) + prev_net)
    index = np.sum(np.where(income < x, 1, 0))
    m = tax2rate(tax[index])
    p = net[index-1] - m * income[index-1] if index > 0 else 0
    print("p fn:", p)
    y = m * x + p
    return x*m + p


class Tax:
    def __init__(self, taxes, gross_incomes):
        self.taxes = taxes
        self.gross_incomes = gross_incomes
        self.net_incomes = []
        self.calc_net_incomes()

    def calc_net_incomes(self):
        for i in range(len(self.taxes)-1):
            prev_gross = self.gross_incomes[i-1] if i > 0 else 0
            prev_net = self.net_incomes[i-1] if i > 0 else 0
            self.net_incomes.append(self.tax2rate(self.taxes[i])*(self.gross_incomes[i] - prev_gross) + prev_net)

    @staticmethod
    def tax2rate(tax_item):
        return (100-tax_item)/100

    def get_net_income(self, gross_income):
        index = np.sum(np.where(self.gross_incomes < gross_income, 1, 0))
        m = self.tax2rate(self.taxes[index])
        p = (self.net_incomes[index-1] - m * self.gross_incomes[index-1]) if index > 0 else 0
        return gross_income * m + p


nz_taxes = np.array([10.5, 17.5, 30, 33, 39])
nz_gross_incomes = np.array([14000, 48000, 70000, 180000])
tax_nz = Tax(nz_taxes, nz_gross_incomes)

MAX = 200000
N = 100
style.use("bmh")
x = np.array(np.linspace(0, MAX, N))
y = [tax_nz.get_net_income(t) for t in x]
plot.plot(x, y, label="NZ Net Income")
plot.xlabel("Gross Income")
plot.figlegend()
plot.show()

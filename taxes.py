import numpy as np
import matplotlib.pyplot as plot
from matplotlib import style


class Tax:
    def __init__(self, tax_data):
        self.taxes = np.array(tax_data["rates"])
        self.currency_factor = tax_data["currency_factor"]
        self.gross_incomes = np.array(tax_data["incomes"]) * self.currency_factor
        self.local_tax = tax_data["local_tax"] if "local_tax" in tax_data else 0
        self.cap_tax, self.cap_yearly = (
            tax_data["capping"]["tax"], tax_data["capping"]["yearly_cap"]) if "capping" in tax_data else (0, 0)
        self.net_incomes = []
        self.calc_net_incomes()

    def calc_net_incomes(self):
        for i in range(len(self.taxes) - 1):
            prev_gross = self.gross_incomes[i - 1] if i > 0 else 0
            prev_net = self.net_incomes[i - 1] if i > 0 else 0
            self.net_incomes.append(self.tax2rate(self.taxes[i]) * (self.gross_incomes[i] - prev_gross) + prev_net)

    @staticmethod
    def tax2rate(tax_item, tax_part=False):
        c = tax_item / 100
        return c if tax_part else 1 - c

    def get_net_income(self, gross_income):
        index = np.sum(np.where(self.gross_incomes < gross_income, 1, 0))
        m = self.tax2rate(self.taxes[index])
        p = (self.net_incomes[index - 1] - m * self.gross_incomes[index - 1]) if index > 0 else 0
        capping = min(gross_income * self.tax2rate(self.cap_tax, tax_part=True),
                      self.cap_yearly) if self.cap_tax != 0 else 0
        local_tax = gross_income * self.tax2rate(self.local_tax, tax_part=True)
        return gross_income * m + p - capping - local_tax

    def get_net_incomes(self, gross_incomes):
        return np.array([self.get_net_income(gross_income) for gross_income in gross_incomes])


nz_tax_data = {"rates": [10.5, 17.5, 30, 33, 39], "incomes": [14000, 48000, 70000, 180000], "currency_factor": 0.56}
malta_tax_data = {"rates": [0, 15, 25, 35], "incomes": [9100, 14500, 60000], "currency_factor": 1,
                  "capping": {"tax": 10, "yearly_cap": 2500}}
italy_tax_data = {"rates": [23, 25, 35, 43], "incomes": [15000, 28000, 50000], "currency_factor": 1, "local_tax": 0.5}
ireland_tax_data = {"rates": [20, 40], "incomes": [40000], "currency_factor": 1}

tax_nz = Tax(nz_tax_data)
tax_malta = Tax(malta_tax_data)
tax_italy = Tax(italy_tax_data)
tax_ireland = Tax(ireland_tax_data)

MIN = 1
MAX = 200000
N = 100
style.use("bmh")
x = np.array(np.linspace(MIN, MAX, N))

y_nz = tax_nz.get_net_incomes(x)
y_malta = tax_malta.get_net_incomes(x)
y_italy = tax_italy.get_net_incomes(x)
y_ireland = tax_ireland.get_net_incomes(x)

plot.subplot(221)
plot.plot(x, y_nz, label="NZ Net Income", color="red")
plot.plot(x, y_malta, label="Malta Net Income", color="green")
plot.plot(x, y_italy, label="Italy Net Income", color="cyan")
plot.plot(x, y_ireland, label="Ireland Net Income", color="brown")
plot.xlabel("Gross Income")
plot.ylabel("Net Income")
plot.figlegend()

plot.subplot(222)
plot.plot(x, 100 * y_nz / x, label="NZ Net Income", color="red")
plot.plot(x, 100 * y_malta / x, label="Malta Net Income", color="green")
plot.plot(x, 100 * y_italy / x, label="Italy Net Income", color="cyan")
plot.plot(x, 100 * y_ireland / x, label="Ireland Net Income", color="brown")
plot.xlabel("Gross Income")
plot.ylabel("% Net/Gross Income")

plot.subplot(223)
plot.plot(x, np.zeros(len(x)), label="Italy Net Income", color="cyan")
plot.plot(x, y_malta-y_italy, label="Malta Net Income", color="green")
plot.plot(x, y_ireland-y_italy, label="Ireland Net Income", color="brown")
plot.plot(x, y_nz - y_italy, label="NZ Net Income", color="red")
plot.xlabel("Gross Income")
plot.ylabel("Net Income compared to Italy")

plot.subplot(224)
plot.plot(x, 100*np.ones(len(x)), label="Italy Net Income", color="cyan")
plot.plot(x, 100*y_malta/y_italy, label="Malta Net Income", color="green")
plot.plot(x, 100*y_ireland/y_italy, label="Ireland Net Income", color="brown")
plot.plot(x, 100*y_nz/y_italy, label="NZ Net Income", color="red")
plot.xlabel("Gross Income")
plot.ylabel("% Net Income compared to Italy")

plot.show()

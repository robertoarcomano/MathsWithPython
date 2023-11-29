import numpy as np
import matplotlib.pyplot as plot
from matplotlib import style
import matplotlib


class Tax:
    def __init__(self, tax_data):
        self.name = tax_data["name"]
        self.color = tax_data["color"]
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

    def get_name(self):
        return self.name

    def get_color(self):
        return self.color

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
        return np.vectorize(self.get_net_income)(gross_incomes)


nz_tax_data = {"name": "NZ", "color": "red", "rates": [10.5, 17.5, 30, 33, 39],
               "incomes": [14000, 48000, 70000, 180000], "currency_factor": 0.56}
malta_tax_data = {"name": "Malta", "color": "orange", "rates": [0, 15, 25, 35], "incomes": [9100, 14500, 60000],
                  "currency_factor": 1,
                  "capping": {"tax": 10, "yearly_cap": 2500}}
italy_tax_data = {"name": "Italy", "color": "cyan", "rates": [23, 25, 35, 43], "incomes": [15000, 28000, 50000],
                  "currency_factor": 1, "local_tax": 0.5}
ireland_tax_data = {"name": "Ireland", "color": "yellow", "rates": [20, 40], "incomes": [40000], "currency_factor": 1}
uk_tax_data = {"name": "UK", "color": "blue", "rates": [0, 20, 40, 45], "incomes": [12570, 50270, 125140],
               "currency_factor": 1.15}
us_tax_data = {"name": "US", "color": "pink", "rates": [10, 12, 22, 24, 32, 35, 37],
               "incomes": [11000, 44725, 95375, 182100, 231250, 578125],
               "currency_factor": 0.91}

tax_nz = Tax(nz_tax_data)
tax_malta = Tax(malta_tax_data)
tax_italy = Tax(italy_tax_data)
tax_ireland = Tax(ireland_tax_data)
tax_uk = Tax(uk_tax_data)
tax_us = Tax(us_tax_data)
taxes = np.array([tax_nz, tax_malta, tax_italy, tax_ireland, tax_uk, tax_us])

MIN = 1
MAX = 200000
N = 100
XLABEL = "Gross Income [Euro]"
FONTSIZE = 4
BIG_FONTSIZE = 5
LINEWIDTH = 0.7
style.use("bmh")
x = np.array(np.linspace(MIN, MAX, N))
matplotlib.rc('xtick', labelsize=FONTSIZE)
matplotlib.rc('ytick', labelsize=FONTSIZE)
plot.rcParams.update({'font.size': BIG_FONTSIZE})
y = np.array([
    [lambda t: t.get_net_incomes(x), XLABEL, "Net Income [Euro]"],
    [lambda t: 100 * t.get_net_incomes(x) / x, XLABEL, "% Net/Gross Income [Euro]"],
    [lambda t: t.get_net_incomes(x) - tax_italy.get_net_incomes(x), XLABEL, "Net Income compared to Italy [Euro]"],
    [lambda t: 100 * t.get_net_incomes(x) / tax_italy.get_net_incomes(x), XLABEL,
     "% Net Income compared to Italy"],
])
for graph_i, (f, x_label, y_label) in enumerate(y):
    plot.subplot(221 + graph_i)
    for tax in taxes:
        plot.plot(x, f(tax), label=tax.get_name(), color=tax.get_color(), linewidth=LINEWIDTH)
        plot.xlabel(x_label)
        plot.ylabel(y_label)
    plot.figlegend() if not graph_i else ""
plot.tight_layout()
plot.savefig("taxes.png", dpi=300)
plot.show()

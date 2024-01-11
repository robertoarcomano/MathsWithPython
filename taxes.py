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

    def get_net_incomes_perc(self, gross_incomes):
        return 100 * self.get_net_incomes(gross_incomes) / gross_incomes

    def get_net_incomes_reference(self, gross_incomes, reference_tax):
        return self.get_net_incomes(gross_incomes) - reference_tax.get_net_incomes(gross_incomes)

    def get_net_incomes_reference_perc(self, gross_incomes, reference_tax):
        return 100 * self.get_net_incomes(gross_incomes) / reference_tax.get_net_incomes(gross_incomes)


tax_data = [
    {"name": "NZ", "color": "red", "rates": [10.5, 17.5, 30, 33, 39],
     "incomes": [14000, 48000, 70000, 180000], "currency_factor": 0.56},
    {"name": "AUS", "color": "green", "rates": [0, 19, 32.5, 37, 45],
     "incomes": [18200, 45000, 120000, 180000], "currency_factor": 0.61},
    {"name": "Malta", "color": "orange", "rates": [0, 15, 25, 35], "incomes": [9100, 14500, 60000],
     "currency_factor": 1,
     "capping": {"tax": 10, "yearly_cap": 2500}},
    {"name": "Italy", "color": "cyan", "rates": [23, 25, 35, 43], "incomes": [15000, 28000, 50000],
     "currency_factor": 1, "local_tax": 0.5},
    {"name": "Ireland", "color": "yellow", "rates": [20, 40], "incomes": [40000], "currency_factor": 1},
    {"name": "UK", "color": "blue", "rates": [0, 20, 40, 45], "incomes": [12570, 50270, 125140],
     "currency_factor": 1.15},
    {"name": "US", "color": "pink", "rates": [10, 12, 22, 24, 32, 35, 37],
     "incomes": [11000, 44725, 95375, 182100, 231250, 578125],
     "currency_factor": 0.91}
]
taxes = [Tax(tax_i) for tax_i in tax_data]
tax_reference = [tax_i for tax_i in taxes if tax_i.get_name() == "Italy"][0]

MIN = 1
MAX = 200000
N = 100
X_LABEL = "Gross Income [Euro]"
FONT_SIZE = 4
BIG_FONT_SIZE = 5
LINE_WIDTH = 0.7
style.use("bmh")
x = np.array(np.linspace(MIN, MAX, N))
matplotlib.rc('xtick', labelsize=FONT_SIZE)
matplotlib.rc('ytick', labelsize=FONT_SIZE)
plot.rcParams.update({'font.size': BIG_FONT_SIZE})

graphs = np.array([
    [lambda t: t.get_net_incomes(x), X_LABEL, "Net Income [Euro]"],
    [lambda t: t.get_net_incomes_perc(x), X_LABEL, "% Net/Gross Income [Euro]"],
    [lambda t: t.get_net_incomes_reference(x, tax_reference), X_LABEL, "Net Income compared to Italy [Euro]"],
    [lambda t: t.get_net_incomes_reference_perc(x, tax_reference), X_LABEL,
     "% Net Income compared to Italy"],
])
for graph_i, (f, x_label, y_label) in enumerate(graphs):
    plot.subplot(221 + graph_i)
    for tax in taxes:
        plot.plot(x, f(tax), label=tax.get_name(), color=tax.get_color(), linewidth=LINE_WIDTH)
        plot.xlabel(x_label)
        plot.ylabel(y_label)
    plot.figlegend() if not graph_i else ""
plot.tight_layout()
plot.savefig("taxes.png", dpi=300)
plot.show()

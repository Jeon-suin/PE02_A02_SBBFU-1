from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np
from lmfit import Model
from numpy import exp
import statsmodels.api as sm
import warnings
warnings.filterwarnings(action='ignore')

def IVfitting(filename):

    fp = open(filename, "r")

    soup = BeautifulSoup(fp,"html.parser")

    voltage = soup.findAll('voltage')[0].string.split(',')
    current = soup.findAll('current')[0].string.split(',')

    x = list(map(float, voltage))
    y = list(map(float, current))
    y = np.abs(y)

    # 2번째 그래프

    plt.title("IV raw dat & fitted dat", fontsize=15)
    plt.xlabel("Voltage [V]")
    plt.ylabel("Current [A]")

    plt.yscale("log")
    plt.plot(x, np.abs(y), 'ko')

    C = np.array(y[:10])
    V = np.array(x[:10])
    fit1 = np.polyfit(V, C, 11)
    fit1 = np.poly1d(fit1)

    # I = a(exp(bV-1)+alpha
    def IV_fit(x, a, b):
        return (a * (exp(x/b) - 1) + fit1(x))

    model = Model(IV_fit)
    result = model.fit(y, x=x, a=2.28 * 10 ** -15, b=0.0351)

    initial_list = []
    for i in x:
        x_value = IV_fit(i, 2.28 * 10 ** -15, 0.0351)
        initial_list.append(x_value)

    initial = sm.add_constant(np.abs(y))
    result1 = sm.OLS(initial_list, initial).fit()

    IVdic = {y: x for x, y in zip(result.best_fit, x)}
    plt.text(1.0, IVdic[1.0], IVdic[1.0], fontsize=8, horizontalalignment='right')
    plt.text(-1.0, IVdic[-1.0], IVdic[-1.0], fontsize=8)
    plt.plot(x, result.best_fit, 'r-', label='{} {}'.format('$R^{2}$ =', result1.rsquared))
    plt.legend(loc='center left')

    plt.suptitle(filename)
    fig = plt.gcf()
    fig.set_size_inches((27,15), forward=False)


    # plt.savefig(filename + '.png', bbox_inches = 'tight')
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from dateutil.parser import parse
from lmfit import Model
from numpy import exp
import statsmodels.api as sm
import os

def fitting(filename):

    fp = open(filename, "r")

    soup = BeautifulSoup(fp,"html.parser")

    # label
    wavelengthsweep = soup.findAll('wavelengthsweep')
    label = []
    for i in range(0, 7):
        label.append(wavelengthsweep[i]['dcbias'])  # append가 list에 뭔가를 추가

    voltage = soup.findAll('voltage')[0].string.split(',')
    current = soup.findAll('current')[0].string.split(',')

    grid = (12, 19)

    x = list(map(float, voltage))
    y = list(map(float, current))
    y = np.abs(y)

    # 2번째 그래프
    plt.subplot2grid(grid, (7, 0), rowspan=5, colspan=5)

    plt.title("IV raw data & fitted data", fontsize=15)
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
        return (a * (exp(b * x) - 1) + fit1(x))

    model = Model(IV_fit)
    result = model.fit(y, x=x, a=10e-16, b=1 / 0.026)

    initial_list = []
    for i in x:
        x_value = IV_fit(i, 10e-16, 1 / 0.026)
        initial_list.append(x_value)

    initial = sm.add_constant(np.abs(y))
    result1 = sm.OLS(initial_list, initial).fit()

    IVdic = {y: x for x, y in zip(result.best_fit, x)}
    plt.text(1.0, IVdic[1.0], IVdic[1.0], fontsize=8, horizontalalignment='right')
    plt.text(-1.0, IVdic[-1.0], IVdic[-1.0], fontsize=8)
    plt.plot(x, result.best_fit, 'r-', label='{} {}'.format('$R^{2}$ =', result1.rsquared))
    plt.legend(loc='center left')

    # 1번째 그래프
    plt.subplot2grid(grid, (0, 0), rowspan=5, colspan=5)

    for i in range(0, 7):
        wavelength = soup.findAll('wavelengthsweep')[i]('l')[0].string
        WL = wavelength.split(',')
        wl = list(map(float, WL))

        IL = soup.findAll('wavelengthsweep')[i]('il')[0].string
        Il = IL.split(',')
        il = list(map(float, Il))
        if i < 6:
            plt.scatter(wl, il, alpha=0.3, label=label[i] + 'V')
        else:
            plt.scatter(wl, il, alpha=0.3)

    plt.title("Transmission spectra - as measured", fontsize=15)
    plt.xlabel("Wavelength [nm]")
    plt.ylabel("Measured transmission [dB]")
    plt.legend(loc='lower center', ncol=3)

    refx = list(map(float, soup.findAll('l')[6].string.split(',')))
    refy = list(map(float, soup.findAll('il')[6].string.split(',')))

    # 3번째 그래프
    plt.subplot2grid(grid, (0, 7), rowspan=5, colspan=5)

    fitlabel = []

    for i in range(1, 8):
        fitlabel.append(i)  # append가 list에 뭔가를 추가

    for i in range(1, 8):
        z = np.polyfit(refx, refy, i)
        f = np.poly1d(z)
        y_new = f(refx)
        plt.plot(refx, y_new, label=fitlabel[i - 1])
    plt.scatter(refx, refy, facecolors='none', edgecolors='k', alpha=0.03)
    plt.legend(loc='lower center', ncol=4)
    plt.title("Ref.-Raw data & fitting data", fontsize=15)
    plt.xlabel("Wavelength [nm]")
    plt.ylabel("Measured transmission [dB]")

    # 4번째 그래프
    plt.subplot2grid(grid, (0, 14), rowspan=5, colspan=5)
    for i in range(0, 6):
        wavelength = soup.findAll('wavelengthsweep')[i]('l')[0].string
        WL = wavelength.split(',')
        wl = list(map(float, WL))

        IL = soup.findAll('wavelengthsweep')[i]('il')[0].string
        Il = IL.split(',')
        il = list(map(float, Il))

        x = wl
        y = il - f(wl)

        if i < 6:
            plt.scatter(x, y, alpha=0.3, label=label[i] + 'V')
    plt.legend(bbox_to_anchor=(0.25, 1.08, 0.5, 0.05), ncol=3, loc='lower center')

    plt.title("Transmission spectra except ref.data", fontsize=15)
    plt.xlabel("Wavelength [nm]")
    plt.ylabel("Measured transmission [dB]")

    plt.suptitle(filename)
    fig = plt.gcf()
    fig.set_size_inches((27,15), forward=False)
    plt.savefig(filename + '.png', bbox_inches = 'tight')


#######################################################################################################################
#######################################################################################################################

def csv_mod(filename):

    fp = open(filename, "r")
    soup = BeautifulSoup(fp, "html.parser")

    voltage = soup.findAll('voltage')[0].string.split(',')
    current = soup.findAll('current')[0].string.split(',')

    x = list(map(float, voltage))
    y = list(map(float, current))
    y = np.abs(y)

    # 2번째 그래프

    C = np.array(y[:10])
    V = np.array(x[:10])
    fit1 = np.polyfit(V, C, 11)
    fit1 = np.poly1d(fit1)

    # I = a(exp(bV-1)+alpha
    def IV_fit(x, a, b):
        return (a * (exp(b * x) - 1) + fit1(x))

    model = Model(IV_fit)
    result = model.fit(y, x=x, a=10e-16, b=1 / 0.026)

    initial_list = []
    for i in x:
        x_value = IV_fit(i, 10e-16, 1 / 0.026)
        initial_list.append(x_value)

    initial = sm.add_constant(np.abs(y))
    result1 = sm.OLS(initial_list, initial).fit()

    IVdic = {y: x for x, y in zip(result.best_fit, x)}

    refx = list(map(float, soup.findAll('l')[6].string.split(',')))
    refy = list(map(float, soup.findAll('il')[6].string.split(',')))

    # Calculate R-Squared
    def poly(x, y, degree):
        results = {}

        coeffs = np.polyfit(x, y, degree)

        # Polynomial Coefficients
        # results['polynomial'] = coeffs.tolist()

        # r-squared
        p = np.poly1d(coeffs)
        # fit values, and mean
        yhat = p(x)  # or [p(z) for z in x]
        ybar = np.sum(y) / len(y)  # or sum(y)/len(y)
        ssreg = np.sum((yhat - ybar) ** 2)  # or sum([ (yihat - ybar)**2 for yihat in yhat])
        sstot = np.sum((y - ybar) ** 2)  # or sum([ (yi - ybar)**2 for yi in y])
        results = ssreg / sstot

        return results

    Rsqref = poly(refx, refy, 6)

    Lot = soup.select('testsiteinfo')[0]['batch']
    Wafer = soup.select('testsiteinfo')[0]['wafer']
    Mask = soup.select('testsiteinfo')[0]['maskset']
    Column = soup.select('testsiteinfo')[0]['diecolumn']
    Row = soup.select('testsiteinfo')[0]['dierow']
    TestSite = soup.select('testsiteinfo')[0]['testsite']
    Name = soup.select("modulator")[0]['name']

    Date = soup.select('oiomeasurement')[0]['creationdate']
    Date = parse(Date).strftime("%Y%m%d_%H%M%S")

    error_flag_list = []
    error_description = []
    WL_list = []
    Rsq = result1.rsquared
    if Rsq < 0.95:
        error_flag_list.append(1)
        error_description.append('Rsq error')
    else:
        error_flag_list.append(0)
        error_description.append('No error')

    WL_analy = soup.findAll('designparameter')
    for k in range(0, len(WL_analy)):
        if WL_analy[k]['symbol'] == 'WL':
            WL_list.append(WL_analy[k].text)

    df = pd.DataFrame(columns=['Lot', 'Wafer', 'Mask', 'TestSite' , 'Name', 'Date', 'Script ID',
     'Script Version', 'Script Owner', 'Operator', 'Row','Column',
     'ErrorFlag', 'Error description','Analysis Wavelength', 'Rsq of Ref.spectrum (Nth)',
     'Max transmission of Ref. spec. (dB)', 'Rsq of IV', 'I at -1V [A]', 'I at 1V [A]'])

    df.loc[0] = [Lot, Wafer, Mask, TestSite, Name, Date,'process LMZ', '0.1', 'A02' ,'JoohanBae',Row, Column, error_flag_list[0],
                 error_description[0], WL_list[0], Rsqref, max(refy), Rsq, IVdic[-1.0],IVdic[1.0]]

    df.to_csv("C:\\ㅎMAIN FOLDER\\Pycharmproject\\pythonProject\\Result\\Test_Result.csv", mode='a',
              header = not os.path.exists("C:\\ㅎMAIN FOLDER\\Pycharmproject\\pythonProject\\Result\\Test_Result.csv"),
              index=False)
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np
import warnings
warnings.filterwarnings(action='ignore')

def Pro_spe(filename):

    fp = open(filename, "r")

    soup = BeautifulSoup(fp,"html.parser")


    # 4번째 그래프

    # label
    wavelengthsweep = soup.findAll('wavelengthsweep')
    label = []
    for i in range(0, 7):
        label.append(wavelengthsweep[i]['dcbias'])  # append가 list에 뭔가를 추가

    refx = list(map(float, soup.findAll('wavelengthsweep')[6]('l')[0].string.split(',')))
    refy = list(map(float, soup.findAll('wavelengthsweep')[6]('il')[0].string.split(',')))
    for i in range(1, 8):
        z = np.polyfit(refx, refy, i)
        f = np.poly1d(z)

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
            plt.scatter(x, y, s=1 , alpha=0.3, label=label[i] + 'V')
    plt.legend(bbox_to_anchor=(0.25, 1.08, 0.5, 0.05), ncol=3, loc='lower center')

    plt.title("Transmission spectra except ref.dat", fontsize=15)
    plt.xlabel("Wavelength [nm]")
    plt.ylabel("Measured transmission [dB]")

    plt.suptitle(filename)
    fig = plt.gcf()
    fig.set_size_inches((27,15), forward=False)


    # plt.savefig(filename + '.png', bbox_inches = 'tight')
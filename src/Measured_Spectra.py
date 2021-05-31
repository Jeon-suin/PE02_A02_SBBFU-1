from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings(action='ignore')

def Measured(filename):

    fp = open(filename, "r")

    soup = BeautifulSoup(fp,"html.parser")


    # label
    wavelengthsweep = soup.findAll('wavelengthsweep')
    label = []
    for i in range(0, 7):
        label.append(wavelengthsweep[i]['dcbias'])  # append가 list에 뭔가를 추가

    # Measured raw data

    for i in range(0, 7):
        wavelength = soup.findAll('wavelengthsweep')[i]('l')[0].string
        WL = wavelength.split(',')
        wl = list(map(float, WL))

        IL = soup.findAll('wavelengthsweep')[i]('il')[0].string
        Il = IL.split(',')
        il = list(map(float, Il))
        if i < 6:
            plt.scatter(wl, il, s = 1, alpha=0.3, label=label[i] + 'V')
        else:
            plt.scatter(wl, il, s = 1 ,alpha=0.3)

    plt.title("Transmission spectra - as measured", fontsize=15)
    plt.xlabel("Wavelength [nm]")
    plt.ylabel("Measured transmission [dB]")
    plt.legend(loc='lower center', ncol=3)

    plt.suptitle(filename)
    fig = plt.gcf()
    fig.set_size_inches((27, 15), forward=False)

    # plt.savefig(filename + '.png', bbox_inches='tight')


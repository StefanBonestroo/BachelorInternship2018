from matplotlib import pyplot as plt

def plotRawData(data, ROICount):

    plt.figure(1)

    for x in range(0, ROICount):

        plt.subplot(221 + x)
        plt.plot(data[x][0], data[x][1])
        plt.xlabel("time (s)")
        plt.ylabel("total of all pixel values")

    plt.subplots_adjust(top=0.90, bottom=0.10, left=0.15, right=0.95, hspace=0.35,
                        wspace=0.45)

    plt.show()

def makeSpectrogram(data, samplingRate, ROICount):

    plt.figure(2)

    for x in range(0, ROICount):

        plt.subplot(221 + x)
        plt.specgram(data[x][1], NFFT = 240, Fs = samplingRate, noverlap=230, cmap= 'jet')
        plt.xlabel("time (s)")
        plt.ylabel("frequency (Hz)")
        plt.colorbar()

    plt.subplots_adjust(top=0.90, bottom=0.10, left=0.15, right=0.95, hspace=0.35,
                        wspace=0.45)

    plt.show()

def plotPowerSpectrum(data, samplingRate, ROICount):

    plt.figure(3)

    for x in range(0, ROICount):

        plt.subplot(221 + x)
        plt.psd(data[x][1], NFFT = 240, Fs = samplingRate, noverlap=230)
        plt.xlabel("frequency (Hz)")
        plt.ylabel("Power (Pxx)")

    plt.subplots_adjust(top=0.90, bottom=0.10, left=0.15, right=0.95, hspace=0.35,
                        wspace=0.45)

    plt.show()

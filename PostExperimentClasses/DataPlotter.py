from matplotlib import pyplot as plt

def plotRawData(data):

    plt.figure(1)

    plt.subplot(221)
    plt.plot(data[0][0], data[0][1])
    plt.xlabel("time (s)")
    plt.ylabel("total of all pixel values")

    plt.subplot(222)
    plt.plot(data[1][0], data[1][1])
    plt.xlabel("time (s)")
    plt.ylabel("total of all pixel values")

    plt.subplot(223)
    plt.plot(data[2][0], data[2][1])
    plt.xlabel("time (s)")
    plt.ylabel("total of all pixel values")

    plt.subplots_adjust(top=0.90, bottom=0.10, left=0.15, right=0.95, hspace=0.35,
                        wspace=0.45)

    plt.show()

def makeSpectrogram(data, samplingRate):

    plt.figure(1)

    plt.subplot(221)
    plt.specgram(data[0][1], NFFT = 240, Fs = samplingRate, noverlap=230, cmap= 'jet')
    plt.xlabel("time (s)")
    plt.ylabel("frequency (Hz)")

    plt.subplot(222)
    plt.specgram(data[1][1], NFFT = 240, Fs = samplingRate, noverlap=230, cmap= 'jet')
    plt.xlabel("time (s)")
    plt.ylabel("frequency (Hz)")

    plt.subplot(223)
    plt.specgram(data[2][1], NFFT = 240, Fs = samplingRate, noverlap=230, cmap= 'jet')
    plt.xlabel("time (s)")
    plt.ylabel("frequency (Hz)")

    plt.subplots_adjust(top=0.90, bottom=0.10, left=0.15, right=0.95, hspace=0.35,
                        wspace=0.45)

    plt.show()

def plotPowerSpectrum(data):

    print("powah")

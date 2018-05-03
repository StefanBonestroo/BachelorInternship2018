def plotRawData(data):

    from matplotlib import pyplot as plt

    plt.figure(1)

    plt.subplot(221)
    plt.plot(data[0][0], data[0][1])

    plt.subplot(222)
    plt.plot(data[1][0], data[1][1])

    plt.subplot(223)
    plt.plot(data[2][0], data[2][1])

    plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
                        wspace=0.35)

    plt.show()

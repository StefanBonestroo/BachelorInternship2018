import scipy.signal
import matplotlib.pyplot as plt
import time
import numpy as np

#*******************************************************************************

def getPower(pre, post):

    fs = 120
    output = []

    preFreqs, prePowers = scipy.signal.welch(pre, fs, nperseg = fs * 2, noverlap = fs * 2 - 10)
    postFreqs, postPowers = scipy.signal.welch(post, fs, nperseg = fs * 2, noverlap = fs * 2 - 10)

    weightedMedianPreFreqs = []
    weightedMedianPostFreqs = []

    for n in range(2,len(preFreqs)):
        m = [preFreqs[n]] * int(prePowers[n])

        for f in m:
            weightedMedianPreFreqs.append(f)

    for n in range(2,len(postFreqs)):
        m = [postFreqs[n]] * int(postPowers[n])

        for f in m:
            weightedMedianPostFreqs.append(f)

    try:
        preMedian = np.nanmedian(weightedMedianPreFreqs)
    except:
        preMedian = 0

    if len(weightedMedianPreFreqs) == 0:
        preMedian = 0

    try:
        postMedian = np.nanmedian(weightedMedianPostFreqs)
    except:
        postMedian = 0

    if len(weightedMedianPostFreqs) == 0:
        postMedian = 0

    deltaMedian = postMedian - preMedian
    output.append(deltaMedian)

    try:
        preMean = np.average(preFreqs[2:], weights = prePowers[2:])
    except:
        preMean = 0

    try:
        postMean = np.average(postFreqs[2:], weights = postPowers[2:])
    except:
        postMean = 0

    deltaMean = postMean - preMean

    output.append(deltaMean)

    preLow = bandpower(preFreqs, prePowers, 1, 5)
    postLow = bandpower(postFreqs, postPowers, 1, 5)
    deltaLow = postLow - preLow

    preMid = bandpower(preFreqs, prePowers, 5, 20)
    postMid = bandpower(postFreqs, postPowers, 5, 20)
    deltaMid = postMid - preMid

    preHigh = bandpower(preFreqs, prePowers, 20, 59.5)
    postHigh = bandpower(postFreqs, postPowers, 20, 59.5)
    deltaHigh = postHigh - preHigh

    output.extend((deltaLow,deltaMid,deltaHigh))

    return output

#*******************************************************************************

def bandpower(freqs, powers, fmin, fmax):

    min = scipy.argmax(freqs > fmin) - 1
    max = scipy.argmax(freqs > fmax) - 1

    return scipy.trapz(powers[min:max], freqs[min:max])

#*******************************************************************************

def getMovement(pre, post):

    preSum = 0
    postSum = 0

    for i in pre:
        preSum += i

    for i in post:
        postSum += i

    return (postSum - preSum)

#*******************************************************************************

def dataCutter(data, start, stimulusLength, timeframe):

    y = data[1]
    fs = 120

    begin = fs * (start - timeframe)
    start = fs * start
    preY = y[begin:start]

    begin = start + stimulusLength
    end = begin + (timeframe * fs)
    postY = y[begin:end]

    return preY, postY

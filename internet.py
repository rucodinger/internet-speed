import speedtest


def speed_test():
    test = speedtest.Speedtest()

    return {
        'download': test.download(),
        'upload': test.upload()
    }
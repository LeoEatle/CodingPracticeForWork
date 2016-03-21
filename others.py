while True:
    try:
        (n, l) = (int(x) for x in input().split())
        locationList = list((int(x) for x in input().split()))

        if n == 1:
            if locationList[0] == 0 or locationList[0] == l:
                print ("{0:.2f}".format(l))
            else:
                print ("{0:.2f}".format(max(l - locationList[0], locationList[0])))
        else:
            locationList = list(set(locationList))
            locationList.sort()
            distanceList = list((locationList[i + 1] - locationList[i] for i in range(len(locationList) - 1)))
            distanceList.sort(reverse=True)
            d = float(distanceList[0]) / 2

            d = max(d, l - locationList[len(locationList) - 1], locationList[0])
            print ("{0:.2f}".format(d))
    except EOFError:
        break
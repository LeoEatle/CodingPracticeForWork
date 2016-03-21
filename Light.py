def getludeng():
        n, l = input().split(" ")
        n = int(n)
        l = int(l)

        locationList = list((int(x) for x in input().split(" ")))
        if n == 1:
            if locationList[0] == 0 or locationList[0] == l:
                print ("{0:.2f}".format(l))
                return
            else:
                print( "{0:.2f}".format(max(l - locationList[0], locationList[0])))
                return
        locationList.sort()

        #find the longest distance between the lights
        longest = 0
        for i in range(len(locationList) - 1):
            distance = abs(locationList[i] - locationList[i + 1])
            if distance > longest:
                longest = distance
        d = float(longest)/2
        d = max(d, l - locationList[len(locationList) - 1], locationList[0])
        print(d)

while True:
    try:
        getludeng()
    except EOFError:
        break

def kphToMph(x):
    mph = round((x / 1.609), 2)
    print(mph, 'mph')
kphToMph(float(input('Enter kph')))

def mphToKph(x):
    kph = round((x * 1.609), 2)
    print(kph, 'kph')
mphToKph(float(input('Enter mph')))

def kgTolb (x):
    lb = round((x * 2.205), 2)
    print(lb, 'lb\'s')
kgTolb(float(input('Enter kg\'s')))

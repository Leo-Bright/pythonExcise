p = 1 - 1.0/1963.0
def lottery(year):
    sum = 0
    for i in range(year):
        sum += i
    print(year,"years",1 - pow(p, sum))

lottery(20)
import math

# Running times
SECOND = 1000000
MINUTE = SECOND * 60
HOUR = MINUTE * 60
DAY = HOUR * 24
MONTH = DAY * 32
YEAR = MONTH * 12
CENTURY = YEAR * 100

units = {"second": SECOND, "minute": MINUTE, "hour": HOUR,
         "day": DAY, "month": MONTH, "year": YEAR, "century": CENTURY}

# Function to determine number of steps (1 millisecond per step)


def function(x):
    return math.factorial(math.floor(x))


# Find maximum n for each given time constraint
for unit in units:
    # Instantiate variables
    count = 0
    lower = 0
    upper = 0
    n = 50000
    goal = units[unit]

    # Find a reasonable search space to start in
    while (function(n)) < goal:
        lower = n
        n += 50000

    upper = n
    print("Found a starting point.")
    print("Lower: %d Upper: %d" % (lower, upper))

    # Funnel down to correct answer
    while True:
        count += 1
        n = (lower + upper) / 2
        test = (function(n))
        if test > goal:
            upper = n
        elif test < goal-1:
            lower = n
        else:
            print("Largest possible n for 1 %s: %f" %
                  (str(unit).capitalize(), n))
            print("test = " + str(test))
            break

def divbyNumber(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print("divided by zero exception")

print(divbyNumber(0))

num1 = 11
num2 = num1


print("before the value was updated", num1)
print("before the value was updated", num2)


num1 = 22

print("After the value was updated", num1)
print("after the value was updated", num2)


dic1 = {
    'value':11
}

dic2= dic1

print("before the value was updated", dic1)
print("before the value was updated", dic2)

dic1['value'] = 35

print("after the value was updated", dic1['value'])
print("after the value was updated", dic2['value'])


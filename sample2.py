ovpay = 0
total = 0  

for i in range(1, 11):
    print("Enter Working Hours of Emp", i, ":")
    h = int(input())

    if h > 40:
        extra = h - 40
        ovpay = extra * 12
        print("Over time pay of emp", i, "is", ovpay)
        total = total + ovpay
    else:
        print("No Overtime Pay")

print("Total Overtime Pay of all employees:", total)

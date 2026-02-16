hours_worked = float(input("Enter total hours worked: "))
hourly_rate = float(input("Enter hourly rate: "))

if hours_worked <= 40:
    pay = hours_worked * hourly_rate
    print("Regular Pay:", pay)
else:
    overtime_hours = hours_worked - 40
    regular_pay = 40 * hourly_rate
    overtime_pay = overtime_hours * hourly_rate * 1.5
    total_pay = regular_pay + overtime_pay

    print("Regular Pay:", regular_pay)
    print("Overtime Hours:", overtime_hours)
    print("Overtime Pay:", overtime_pay)
    print("Total Pay:", total_pay)

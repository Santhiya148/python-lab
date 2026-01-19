emp = {
    'EmpID': 'E102',
    'EmpName': 'Ravi',
    'EmpAge': 28,
    'EmpCity': 'Hyderabad',
    'EmpDept': 'IT'
}

print("\nEmployee Dictionary is:", emp)

print("\nEmployee Name is:", emp['EmpName'])
print("\nEmployee City is:", emp['EmpCity'])

print("\nAll Keys in Dictionary")
for x in emp:
    print(x)

print("\nAll Values in Dictionary")
for x in emp:
    print(emp[x])

emp["EmpSalary"] = 45000
print("\nUpdated Dictionary is:", emp)

emp["EmpName"] = "Suresh"
print("\nUpdated Dictionary is:", emp)

emp.pop("EmpAge")
print("\nUpdated Dictionary is:", emp)

print("\nLength of Dictionary is:", len(emp))

emp2 = emp.copy()
print("\nNew Dictionary is:", emp2)

emp.clear()
print("\nUpdated Dictionary is:", emp)

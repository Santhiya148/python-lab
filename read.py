import pandas as pd

# Step 1: Create sample data (only for demo purpose)
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [25, 30, 35, 28, 32],
    "Department": ["HR", "IT", "Finance", "IT", "HR"],
    "Salary": [40000, 60000, 70000, 50000, 45000]
}

# Convert dictionary to DataFrame
df = pd.DataFrame(data)

# Save to CSV file
df.to_csv("employees.csv", index=False)

# Step 2: Read CSV file
df = pd.read_csv("employees.csv")

print("Original Data:")
print(df)

# Step 3: Filter Data
print("\nEmployees older than 30:")
filtered_data = df[df["Age"] > 30]
print(filtered_data)

print("\nEmployees from IT Department:")
print(df[df["Department"] == "IT"])

print("\nEmployees with Salary greater than 50000:")
print(df[df["Salary"] > 50000])

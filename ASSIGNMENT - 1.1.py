#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re

def validate_email(email):
    
    if email.count('@') != 1:
        return "Invalid: Email must contain exactly one '@' symbol"

    
    pattern = r'^[a-z0-9._]+@[a-z0-9]+\.[a-z]{2,}$'
    if not re.match(pattern, email):
        return "Invalid: Email contains invalid characters or format"

    return "Valid Email"


email_input = input("Enter an email to validate: ").strip()
print(validate_email(email_input))


# In[2]:


n = int(input("Enter rows: "))
num = 1
for i in range(1, n + 1):
    row = []
    for j in range(i):
        row.append(str(num))
        num += 1
    print(" * ".join(row))


# In[3]:


n = int(input("Enter rows: "))
# Top half
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)
# Bottom half
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "* " * i)


# In[4]:


n = int(input("Enter rows: "))
arr = []
num = 1
for i in range(1, n + 1):
    row = []
    for j in range(i):
        row.append(str(num))
        num += 1
    arr.append(" * ".join(row))

for row in arr:
    print(row)

for row in reversed(arr[:-1]):
    print(row)


# In[5]:


n = int(input("Enter rows (7 recommended): "))
for i in range(n):
    if i == 0:
        print(" *** ")
    elif i == 3:
        print(" * *** ")
    elif i == n - 1:
        print(" *** ")
    elif i > 3:
        print(" *   * ")
    else:
        print(" * ")


# In[6]:


n = int(input("Enter odd row count: "))
for i in range(n):
    row = []
    for j in range(n):
        if i == 0 or i == n - 1 or j == n // 2:
            row.append("1")
        else:
            row.append("0")
    print(" ".join(row))


# In[7]:


def cyclic_rotate(case_type, s, times):
    s = list(s)  
    for _ in range(times):
        if case_type == 1:  
            first = s.pop(0)
            s.append(first)
        elif case_type == 2: 
            last = s.pop()
            s.insert(0, last)
        print("".join(s))  

case = int(input("Enter case (1 for left, 2 for right): "))
string_input = input("Enter string (e.g., happy): ").strip().lower()
rotations = int(input("Enter number of rotations: "))

cyclic_rotate(case, string_input, rotations)


# In[8]:


healthy_data = {
    "Sugar level": 15,
    "Blood pressure": 32,
    "Heartbeat rate": 71,
    "weight": 65,
    "fat percentage": 10
}

patient_data = {}
print("Enter your pathology test values:")

# Collect patient data
for key in healthy_data:
    value = int(input(f"{key}: "))
    patient_data[key] = value

print("\n--- Patient Input ---")
for k, v in patient_data.items():
    print(f"{k}: {v}")

difference_report = {}
print("\n--- Differences and Warnings ---")

for key in healthy_data:
    diff = patient_data[key] - healthy_data[key]
    difference_report[key] = diff
    if diff != 0:
        print(f"WARNING: {key} differs from ideal value.")

print("\nDifference Report:")
print(difference_report)

print("\n--- Detailed Explanation ---")
for key, diff in difference_report.items():
    if diff < 0:
        print(f"{key} {diff}")
        print(f"The {key.lower()} is {-diff} less than the ideal value\n")
    elif diff > 0:
        print(f"{key} {diff}")
        print(f"The {key.lower()} is {diff} more than the ideal value\n")
    else:
        print(f"{key} is ideal.\n")


# In[9]:


def is_armstrong(number):
    num_str = str(number)  
    power = len(num_str)  
    total = sum(int(digit) ** power for digit in num_str)  
    return total == number

num = int(input("Enter a number: "))
if is_armstrong(num):
    print("Armstrong number")
else:
    print("Not an Armstrong number")


# In[11]:


def decimal_to_binary(n):
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary  
        n = n // 2
    return binary

num = int(input("Enter a decimal number: "))
binary_result = decimal_to_binary(num)
print(binary_result)


# In[12]:


def is_perfect_number(n):
    if n <= 1:
        return False
    sum_divisors = 0
    for i in range(1, n):
        if n % i == 0:
            sum_divisors += i
    return sum_divisors == n

num = int(input("Enter a number: "))
if is_perfect_number(num):
    print("Perfect number")
else:
    print("Not a perfect number")


# In[ ]:





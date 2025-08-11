#!/usr/bin/env python
# coding: utf-8

# In[1]:


row_num = int(input("Input number of rows: "))
col_num = int(input("Input number of columns: "))
multi_list = [[0 for col in range(col_num)] for row in range(row_num)]
for row in range(row_num):
        for col in range(col_num):
            multi_list[row][col] = row * col
print(multi_list)


# In[2]:


def sort_comma_separated_words(input_string):
    words = input_string.split(',')
    words.sort()
    return ','.join(words)
input_words = input("Enter comma-separated words: ")
sorted_words = sort_comma_separated_words(input_words)
print(sorted_words)


# In[3]:


def process_words():
    input_string = input("Enter words separated by spaces: ")
    words_list = input_string.split()
    unique_words = sorted(list(set(words_list)))
    print(" ".join(unique_words))
process_words()


# In[4]:


even_digit_numbers = []

for num in range(1000, 3001):
    num_str = str(num)
    if all(int(digit) % 2 == 0 for digit in num_str):
        even_digit_numbers.append(num_str)

print(",".join(even_digit_numbers))


# In[5]:


s = input()
letters = sum(c.isalpha() for c in s)
digits = sum(c.isdigit() for c in s)
print("LETTERS", letters)
print("DIGITS", digits)


# In[6]:


sentence = input("Enter a sentence: ")
upper_case = 0
lower_case = 0
for char in sentence:
    if char.isupper():
        upper_case += 1
    elif char.islower():
        lower_case += 1
print("UPPER CASE", upper_case)
print("LOWER CASE", lower_case)


# In[10]:


input_data = input("Enter transactions (comma separated, e.g., D 300, W 200): ")
transactions = input_data.split(',')
net_amount = 0

for txn in transactions:
    txn = txn.strip()
    if not txn:  
        continue
    type_, amount = txn.split()
    amount = int(amount)
    if type_.upper() == 'D':
        net_amount += amount
    elif type_.upper() == 'W':
        net_amount -= amount

print(net_amount)



# In[11]:


import re

input_data = input("Enter comma-separated passwords to validate: ")
passwords = input_data.split(',')
valid_passwords = []

for password in passwords:
    password = password.strip()  
    if 6 <= len(password) <= 12:
        if (re.search("[a-z]", password) and
            re.search("[A-Z]", password) and
            re.search("[0-9]", password) and
            re.search("[$#@]", password) and
            not re.search(r"\s", password)):  
            valid_passwords.append(password)

print(",".join(valid_passwords))


# In[14]:


records = []
print("Enter name, age, height tuples (type 'done' to finish):")

while True:
    line = input()
    if line.lower() == 'done':
        break
    parts = tuple(line.split(","))
    if len(parts) == 3:
        records.append(parts)

records.sort(key=lambda x: (x[0], int(x[1]), int(x[2])))

print(records)


# In[15]:


import math

input_data = input("Enter movement commands (e.g., UP 5,DOWN 3,LEFT 3,RIGHT 2): ")

commands = input_data.split(',')

x = 0
y = 0

for command in commands:
    command = command.strip()  
    if not command:
        continue
    direction, steps = command.split()
    steps = int(steps)

    if direction.upper() == "UP":
        y += steps
    elif direction.upper() == "DOWN":
        y -= steps
    elif direction.upper() == "LEFT":
        x -= steps
    elif direction.upper() == "RIGHT":
        x += steps

distance = math.sqrt(x**2 + y**2)

print(round(distance))


# In[16]:


input_str = input("Enter a string: ")
input_str = input_str.lower() 
result = ""
i = 0

while i < len(input_str):
    count = 1
    while i + 1 < len(input_str) and input_str[i] == input_str[i + 1]:
        count += 1
        i += 1
    result += input_str[i] + str(count)
    i += 1

print(result)


# In[17]:


import re

def find_pairs_with_sum_9(s):
    result = []
    i = 0
    while i < len(s):
        if s[i].isalpha():
            char1 = s[i]
            j = i + 1
            num_str = ""
            while j < len(s) and not s[j].isalpha():
                num_str += s[j]
                j += 1
            if j < len(s) and s[j].isalpha():
                char2 = s[j]
                if num_str and sum(int(d) for d in num_str) == 9:
                    result.append(f"{char1},{char2}")
            i = j  
        else:
            i += 1
    return result

input_str = input("Enter an alphanumeric string: ")
pairs = find_pairs_with_sum_9(input_str)

for pair in pairs:
    print(pair)


# In[18]:


binary_str = input("Enter a binary number: ")
count_ones = binary_str.count('1')  
pairs = count_ones * (count_ones - 1) // 2  
print(pairs)


# In[19]:


def find_minimum_denominations(valid_currency, money):
    valid_currency.sort(reverse=True)
    result = {}
    
    for denom in valid_currency:
        if money >= denom:
            count = money // denom
            result[denom] = count
            money -= denom * count
    
    for denom in result:
        print(f"{denom}-{result[denom]}")

valid_currency = list(map(int, input("Enter valid currency (comma-separated): ").split(',')))
money = int(input("Enter the money amount: "))

find_minimum_denominations(valid_currency, money)


# In[20]:


import math

def non_consecutive_stop_ways(n, m):
    if m > n:
        return 0
    return math.comb(n - m + 1, m)

n = int(input("Enter total number of stops (n): "))
m = int(input("Enter number of stops to make (m): "))

print("Output:", non_consecutive_stop_ways(n, m))


# In[ ]:


def determine_winner(a, b):
    a = a.lower()
    b = b.lower()
    if a == b:
        return "DRAW"
    elif (a == "stone" and b == "scissor") or \
         (a == "paper" and b == "stone") or \
         (a == "scissor" and b == "paper"):
        return "Player A wins"
    else:
        return "Player B wins"

score_a = 0
score_b = 0
round_num = 1

print("Game: Stone Paper Scissor")
print("Instructions: First to reach 5 points wins.\n")

while score_a < 5 and score_b < 5:
    print(f"Round {round_num}:")
    move_a = input("Player A: ").strip()
    move_b = input("Player B: ").strip()

    result = determine_winner(move_a, move_b)
    
    if result == "Player A wins":
        score_a += 1
    elif result == "Player B wins":
        score_b += 1

    print(f"Result: {result}")
    print(f"Score -> Player A: {score_a} | Player B: {score_b}")
    print("-" * 30)
    round_num += 1

if score_a == 5:
    print("Player A is the WINNER!")
else:
    print("Player B is the WINNER!")


# In[ ]:


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


# In[ ]:





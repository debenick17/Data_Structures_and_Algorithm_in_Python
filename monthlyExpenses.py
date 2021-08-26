# Monthly expenses
'''
i) January - 2200
ii) February - 2350
iii) March - 2600
iv) April - 2130
v) May - 2190
'''

list = [2200, 2350, 2600, 2130, 2190]

# 1. In Feb, how many dollars you spent extra compared to January
janFebExpDiff = list[1] - list[0]
print("I spent $" ,janFebExpDiff," extra in February")

# 2. Find out your total expense in the first quarter(first three months) of the year
firstQuarterExp = list[0]+list[1]+list[2]
print("Expense for first quater of the year is $", firstQuarterExp)

# 3. Find out of you spent exactly $2000 in any month
for exp in range(1, len(list)):
    if list[exp] == 2000:
        print("You spent $2000 in month number", exp)

# 4. June month just finished and your expenses is $1980. Add this item to our monthly expense list
juneExp = 1980
list.insert(len(list), juneExp)
print(list)

# 5. You returned an item that you bought in a month of April and got a refund of $200. Make a correction to your
# monthly expenses list based on this
aprilRefund = 200
aprilUpdate = list[3] - aprilRefund
list[3] = aprilUpdate
print(list)


# Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190


# 1. In Feb, how many dollars you spent extra compare to January?
expenses = [2200, 2350, 2600, 2130, 2190]

def E1(expenses):
    january = expenses[0]
    february = expenses[1]

    res = february - january

    return f'I spent extra {res} dollars.'

print(E1(expenses))



# 2. Find out your total expense in first quarter (first three months) of the year.
def E2(expenses):
    first_quarter = expenses[0:3]
    total_expense = 0

    for month in first_quarter:
        total_expense += month
    return f'total expense: {total_expense}'


print(E2(expenses))



# 3. Find out if you spent exactly 2000 dollars in any month
def E3(expenses):
    month = 2000

    if month in expenses:
        return 'I spent exactly 2000 dollars in a month.'
    return 'I didn\'t'

        
print(E3(expenses))



# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
def E4(expenses):
    expenses.append(1980)
    return expenses

print(E4(expenses))



# 5. You returned an item that you bought in a month of April and
    # got a refund of 200$. Make a correction to your monthly expense list
    # based on this

def E5(expenses):
    for i in range(len(expenses)):
        if i == 3:
            expenses[i] -= 200
    return expenses

print(E5(expenses))

        
    

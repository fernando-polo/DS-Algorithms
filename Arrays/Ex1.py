# Let us say your expenses for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190

expenses = [2000, 2350, 2600, 2130, 2190]


# 1. In Feb, how many dollars you spent extra compare to January?
def dollars_spent(month1, month2):
    return month1 - month2

print(dollars_spent(expenses[1], expenses[0]))


# 2. Find out your total expense in first quarter (first three months) of the year.
'''
Obtener los primeros 3 meses
Iterar sobre cada uno y acumular o sumar su valor en una variable
'''
first_three_months = expenses[0:3]
sum_frst_three_months = 0

for i in first_three_months:
    sum_frst_three_months += i
print(f'The total amount for the 1st trimester is ${sum_frst_three_months}')


# 3. Find out if you spent exactly 2000 dollars in any month
is_2000 = 2000 in expenses
print(f'We spent $2000? {is_2000}')
    


# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
expenses.append(1980)
print(expenses)


# 5. You returned an item that you bought in a month of April and
    # got a refund of 200$. Make a correction to your monthly expense list
    # based on this
expenses[3] = expenses[3] - 200
print(expenses)


heroes=['spider man','thor','hulk','iron man','captain america']


# 1. Length of the list
print(len(heroes))


# 2. Add 'black panther' at the end of this list
heroes.append('black panther')


# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
heroes.pop()
heroes.extend(['hulk', 'black panther'])
print(heroes)


# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
heroes[1:3] = ['doctor strange']
print(heroes)


# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
heroes.sort()
print(heroes)


# Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
def odds(minimum_number, max_number):
    if max_number <= minimum_number:
        return 'The input is invalid'
    return [i for i in range(minimum_number, max_number + 1) if i % 2 != 0]
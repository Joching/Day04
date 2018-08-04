
lst = {}

with open ('capitols.txt') as x:
    for i in x:
        (state, cap) = i.split(',')
        lst[state] = cap

print (lst[California])

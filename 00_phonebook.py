#!/usr/bin/env python3

#Joshua Ching; Um, this one is hard to under stand from looking at it. Good luck lol
#Type a first name or last name to search for them.
#By Joching


import sys

def firstname():#creates dictionary with first name as key if they look up first name
    global names
    names = {}
    with open("names.txt") as i:
        for x in i:
            (first, last) = x.split(',')  
            last = last.strip('\n')
            first = first.lower()#make formatting pretty
            last = last.lower()
            if (f'{first}' in names) == True and (f'{last}' in names[f'{first}']) == False:
                names[first] = names[first] + f', {last}'#if the same name appears more than once prevents duplicates
            else:
                names[first] = last
       
def lastname():#creates dictionary with last name as key if they look up last name
    global names
    names = {}
    with open("names.txt") as i:
        for x in i:
            (first, last) = x.split(',')  
            last = last.strip('\n')
            first = first.lower()#make formatting pretty
            last = last.lower()
            if (f'{last}' in names) == True and (f'{first}' in names[f'{last}']) == False:
                names[last] = names[last] + f', {first}'#if the same name appears more than once prevents duplicates
            else:
                names[last] = first
        
            
def main():
    in1 = input('Would you like to look up a first or last name? ')

    if in1.lower() == 'first' or in1.lower() == 'first name':
        firstname()#calls for first name dictionary
        inf = input('What first name would you like to look up? ')
        inf = inf.lower()
        if inf in names:#If name is in dictionary, it will print it
            sys.stdout.write('\033[32;1;40m** Shared\033[0m')
            sys.stdout.write('\033[36;1;40m First \033[0m')
            sys.stdout.write('\033[32;1;40mNames!**\033[0m')
            print('')
            final = names[inf]
            final = final.split(',')
            print(f'{inf.capitalize()} ({len(final)}): {names[inf].title()}')
        else:#gives error if name not in data base
            print(('\033[31mThat name is not in the database\033[0m'))
            main()
    elif in1.lower() == 'last' or in1.lower() == 'last name':
        lastname()#calls for the last name dictionary
        inf = input('What last name would you like to look up? ')
        inf = inf.lower()
        if inf in names:#prints if name in data base
            sys.stdout.write('\033[32;1;40m** Shared\033[0m')
            sys.stdout.write('\033[36;1;40m Last \033[0m')
            sys.stdout.write('\033[32;1;40mNames!**\033[0m')
            print('')
            final = names[inf]
            final = final.split(',')
            print(f'{inf.capitalize()} ({len(final)}): {names[inf].title()}')
        else:#if name not in data base, gives error
            print(('\033[31mThat name is not in the database\033[0m'))
            main()
    else:#if they dont specify what kind of name, first or last, then gives error message
        print('\033[31mSorry, please type "Last" or "First"\033[0m')
        main()

main()
    



























# import sys


# names = {}

# with open("names.txt") as i:
#     for x in i:
#         (first, last) = x.split(',')  
#         last = last.strip('\n')
#         first = first.lower()
#         last = last.lower()
#         if (f'{first}' in names) == True and (f'{last}' in names[f'{first}']) == False:
#             names[first] = names[first] + f', {last}'
#         else:
#             names[first] = last
       
            

# in1 = input('Would you like to look up a first or last name? ')

# if in1.lower() == 'first':
#     inf = input('What first name would you like to look up? ')
#     print(names[inf])
# elif in1.lower90 == 'last':
#     inl = input('What last name would you like to loom up? ')



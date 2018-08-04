

import sys



def firstname():
    global names
    names = {}
    with open("names.txt") as i:
        for x in i:
            (first, last) = x.split(',')  
            last = last.strip('\n')
            first = first.lower()
            last = last.lower()
            if (f'{first}' in names) == True and (f'{last}' in names[f'{first}']) == False:
                names[first] = names[first] + f', {last}'
            else:
                names[first] = last
       
def lastname():
    global names
    names = {}
    with open("names.txt") as i:
        for x in i:
            (first, last) = x.split(',')  
            last = last.strip('\n')
            first = first.lower()
            last = last.lower()
            if (f'{last}' in names) == True and (f'{first}' in names[f'{last}']) == False:
                names[last] = names[last] + f', {first}'
            else:
                names[last] = first
        
            
def main():
    in1 = input('Would you like to look up a first or last name? ')

    if in1.lower() == 'first' or in1.lower() == 'first name':
        firstname()
        inf = input('What first name would you like to look up? ')
        inf = inf.lower()
        sys.stdout.write('\033[32;1;40m** Shared\033[0m')
        sys.stdout.write('\033[36;1;40m First \033[0m')
        sys.stdout.write('\033[32;1;40mNames!**\033[0m')
        print('')
        final = names[inf]
        final = final.split(',')
        print(f'{inf.capitalize()} ({len(final)}): {names[inf].title()}')
    elif in1.lower() == 'last' or in1.lower() == 'last name':
        lastname()
        inf = input('What last name would you like to look up? ')
        inf = inf.lower()
        sys.stdout.write('\033[32;1;40m** Shared\033[0m')
        sys.stdout.write('\033[36;1;40m Last \033[0m')
        sys.stdout.write('\033[32;1;40mNames!**\033[0m')
        print('')
        final = names[inf]
        final = final.split(',')
        print(f'{inf.capitalize()} ({len(final)}): {names[inf].title()}')
    else:
        print('\033[31mSorry, please type "Last" or "First"\033[0m')
        main()

main()
    


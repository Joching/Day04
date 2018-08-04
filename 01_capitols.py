


#!/usr/bin/env python3

#Joshua Ching; find the easter egg
#write the name of a capital or state
#By Joching


def main():
    lst = {}
    lst2 = {}
    with open ('capitols.txt') as x:#open dic with state as key
        for i in x:
            (state, cap) = i.split(',')
            cap = cap.replace('\n','')
            lst[state] = cap

    with open ('capitols.txt') as y:#open dic with capital as key
        for i in y:
            (x1, y1) = i.split(',')
            y1 = y1.replace('\n','')#get rid of \n and then swap
            cap = y1
            state = x1
            lst2[cap] = state

    def ask():
        arg = input('Ready: ').capitalize()
        if arg == 'Done' or arg == 'Exit' or arg == 'Leave' or arg == 'Quit':#added extra phrases that make sense
            exit()
        elif arg == 'Let me out!':#Easter egg lol
            print("\033[31mI'm sorry dave, I can't do that.\033[0m")
            ask()
        elif arg in lst:#check if arg is key in state dic
            print(lst[arg])
            ask()
        elif arg in lst2:#check if arg is key in capital dic
            print(lst2[arg])
            ask()
        else:
            print('nil')
            ask()
    ask()

main()
#!/usr/bin/env python3

#Joshua Ching; Pick and number! Any number!
#Type a number in as cmd line arg
#By Joching

import sys

def main():
    arg = sys.argv[1]
    dec = int(arg) #make string => int
    orgnum = dec #save for final print out
    binlist = []

    while dec > .5:
        if dec % 2 == 1: #Test if even or odd. 1 = odd
            binlist.append(1)
        else:
            binlist.append(0)
        dec = dec/2
        dec = int(dec)#remove .5 if applicable

    binlist = str(binlist).strip('[').strip(']').replace(',','').replace(' ', '')#format nicely

    print ('')
    print ('#'.center(83,'#'))
    print('#',''.center(79,' '),'#')
    print('#',f'{orgnum} in Binary is:'.center(79,' '),'#')  #print nicely
    print('#',binlist[::-1].center(79,' '),'#')
    print('#',''.center(79,' '),'#')  
    print ('#'.center(83,'#'))
    print('')
main()
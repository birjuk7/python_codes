#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    try:
        x= 20/5
    except ValueError:
        print('found a value error')
    except :
        print('unknown error')
    else:
        print('program executed successfully i.e no error--"good job"')    
        print(x)
if __name__ == '__main__': main()

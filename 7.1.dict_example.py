#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    animals = dict( cat = 'meow', puppy = 'kutte ka bachcha', lion= 'den',
        giraffe= 'the tallest animal', dragon= 'can fly' )
    '''for v in animals.values(): print(v)'''
    print_dict(animals)
def print_dict(o):
    for k,v in o.items(): print(f'{k}: {v}')

if __name__ == '__main__': main()

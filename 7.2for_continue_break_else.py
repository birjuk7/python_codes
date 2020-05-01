#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

animals = ( 'bear','cat', 'bunny', 'dog', 'horse', 'velociraptor' )

for pet in animals:
    if pet == 'dog':continue
    if pet == 'horse':break
    print(pet)
else:
    print('list completed now')

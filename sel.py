# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 13:15:26 2021

@author: f1cki

Here is how we make our selections of the given options.
"""

import random as rnd
import options as opt



def toddlertrait():
    trait0 = rnd.choices(opt.toddler_traits, weights=[4, 4, 6, 5, 4, 6, 5, 6], k=1)
    return trait0
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          

  
ttrait = str(toddlertrait())


def childts(ttrait):
    while opt.toddler_traits[0] in ttrait:
        ctrait = set((rnd.choices(opt.child_traits, weights=[5, 5, 5, 5, 4, 5, 5, 5, 6, 4, 6, 5, 5, 5, 5, 4, 5, 4, 5, 5, 6, 5, 5, 6, 5, 5, 5, 5, 5, 5, 5, 4, 4, 5, 6, 5, 5, 5, 5, 5, 5, 5], k=2)))
        if len(ctrait) < 2:
            childts(ttrait)
            childts(ttrait)
        else:
            return list(ctrait)
    while opt.toddler_traits[1] in ttrait:
        ctrait = set((rnd.choices(opt.child_traits, weights=[5, 6, 5, 6, 5, 5, 4, 5, 4, 5, 5, 6, 5, 5, 5, 5, 5, 5, 6, 5, 5, 5, 6, 5, 5, 5, 5, 4, 4, 5, 5, 4, 4, 4, 6, 5, 5, 5, 5, 5, 5, 5], k=2)))
        if len(ctrait) < 2:
            childts(ttrait)
        else:
            return list(ctrait)
    while opt.toddler_traits[2] in ttrait:
        ctrait = set((rnd.choices(opt.child_traits, weights=[5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 5, 5, 6, 6, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 5, 5, 6, 5, 5, 5, 6, 4, 6, 6, 5, 5, 5, 5, 4, 5], k=2)))
        if len(ctrait) < 2:
            childts(ttrait)
        else:
            return list(ctrait)
    while opt.toddler_traits[3] in ttrait:
        ctrait = set((rnd.choices(opt.child_traits, weights=[5, 5, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 6, 5, 5, 5, 5, 4, 6, 6, 5, 4, 4, 5, 5, 4, 5, 6, 5, 5], k=2)))
        if len(ctrait) < 2:
            childts(ttrait)
        else:
            return list(ctrait)
    while opt.toddler_traits[4] in ttrait:
        ctrait = set((rnd.choices(opt.child_traits, weights=[5, 4, 6, 5, 5, 5, 5, 4, 5, 5, 5, 5, 5, 5, 5, 4, 5, 4, 6, 5, 5, 5, 5, 5, 5, 5, 4, 5, 6, 5, 5, 5, 4, 4, 6, 5, 5, 5, 6, 5, 5, 6], k=2)))
        if len(ctrait) < 2:
            childts(ttrait)
        else:
            return list(ctrait)
    while opt.toddler_traits[5] in ttrait:
        ctrait = set((rnd.choices(opt.child_traits, weights=[6, 5, 5, 5, 6, 6, 5, 5, 5, 5, 5, 5, 4, 5, 6, 5, 5, 5, 4, 5, 5, 5, 5, 5, 5, 6, 5, 5, 5, 5, 4, 5, 5, 5, 5, 4, 5, 5, 4, 5, 5, 5], k=2)))
        if len(ctrait) < 2:
            childts(ttrait)
        else:
            return list(ctrait)
    while opt.toddler_traits[6] in ttrait:
        ctrait = set((rnd.choices(opt.child_traits, weights=[5, 5, 6, 5, 5, 4, 5, 6, 5, 5, 5, 5, 5, 4, 5, 5, 5, 5, 5, 4, 5, 4, 5, 5, 5, 5, 5, 5, 5, 6, 5, 5, 6, 5, 4, 5, 6, 6, 5, 5, 4, 5], k=2)))
        if len(ctrait) < 2:
            childts(ttrait)
        else:
            return list(ctrait)
    while opt.toddler_traits[7] in ttrait:
        ctrait = set((rnd.choices(opt.child_traits, weights=[4, 5, 5, 5, 5, 5, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 6, 5, 5, 5, 5, 5, 4, 5, 5, 6, 6, 5, 4, 5, 5, 5, 4, 4, 5, 4, 5, 6, 5, 5, 5], k=2)))
        if len(ctrait) < 2:
            childts(ttrait)
        else:
            return list(ctrait)


ctrait = childts(ttrait)  
childt1 = ctrait[1:2]
childt2 = ctrait[0:1]


def adult_traits(ctrait):
    while any(x in opt.evilT for x in ctrait):
        atraits = rnd.choices(opt.adult_traits, weights=[5, 5, 5, 5, 5, 5, 6, 6, 6, 5, 4, 6, 6, 6, 6, 5, 4, 6, 4, 5, 6, 5, 5], k=1)
        print("evilT")
        return atraits
    while any(x in opt.musicT for x in ctrait):
        atraits = rnd.choices(opt.adult_traits, weights=[5, 6, 6, 5, 5, 5, 4, 5, 6, 6, 5, 5, 4, 4, 5, 5, 4, 5, 5, 5, 5, 5, 6], k=1)
        print("musicT")
        return atraits
    while any(x in opt.artT for x in ctrait):
        atraits = rnd.choices(opt.adult_traits, weights=[4, 5, 5, 6, 5, 5, 6, 5, 6, 5, 5, 5, 4, 4, 5, 6, 4, 5, 6, 5, 5, 6, 4], k=1)
        print("artT")
        return atraits
    while any(x in opt.smartT for x in ctrait):
        atraits = rnd.choices(opt.adult_traits, weights=[4, 4, 4, 5, 6, 6, 5, 5, 4, 6, 5, 5, 4, 4, 4, 5, 6, 6, 6, 6, 5, 5, 6], k=1)
        print("smartT")
        return atraits
    while any(x in opt.fitnessT or opt.outdoorT for x in ctrait):
        atraits = rnd.choices(opt.adult_traits, weights=[6, 5, 6, 4, 6, 5, 5, 6, 4, 4, 5, 5, 6, 6, 5, 5, 6, 5, 5, 4, 5, 4, 4], k=1)
        print("fitnessT")
        return atraits
    while any(x in opt.beautyT for x in ctrait):
        atraits = rnd.choices(opt.adult_traits, weights=[4, 6, 6, 5, 6, 5, 6, 5, 6, 5, 4, 6, 6, 6, 5, 6, 4, 4, 4, 4, 5, 5, 4], k=1)
        print("beautyT")
        return atraits
    while any(x in opt.goodT or opt.socialT for x in ctrait):
        atraits = rnd.choices(opt.adult_traits, weights=[4, 5, 5, 6, 6, 6, 4, 6, 5, 5, 6, 4, 4, 4, 4, 6, 6, 4, 6, 5, 4, 5, 5], k=1)
        print("goodT")
        return atraits
    while any(x in opt.otherT for x in ctrait):
        atraits = rnd.choices(opt.adult_traits, k=1)
        print("other")
        return atraits


 



adults = str(adult_traits(ctrait))

print(ttrait)
print(ctrait)
print(childt1)
print(childt2)
print(adults)
if __name__ == '__main__':
    pass

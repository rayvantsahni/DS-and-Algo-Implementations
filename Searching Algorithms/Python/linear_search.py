# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 04:31:05 2020

@author: Rayvant Sahni
"""

def linear_search(list_to_search, value_to_find):
    
    for index in range(len(list_to_search)):
        if list_to_search[index] == value_to_find:
            return "Found at index " + str(index)
    return "Not Found!"



def main():
    import random
    
    random_list = [random.randint(1, 50) for _ in range(30)]
    search_value = 10
    
    print(random_list, end = "\n\n")    
    print(linear_search(random_list, search_value))
    
main()

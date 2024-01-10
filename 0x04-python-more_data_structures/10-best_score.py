#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    highest_score = 0
    highest_score_person = ''
    for key, value in a_dictionary.items():
        if value > highest_score:
            highest_score = value
            highest_score_person = key
    return highest_score_person

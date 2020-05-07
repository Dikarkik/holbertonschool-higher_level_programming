#!/usr/bin/python3
# function that returns a key with the biggest integer value


def best_score(a_dictionary):
    if a_dictionary:
        all_keys = sorted(a_dictionary)
        best_key = all_keys[0]
        value = a_dictionary.get(all_keys[0])
        for key in all_keys:
            if a_dictionary.get(key) > value:
                best_key = key
                value = a_dictionary.get(key)
        return best_key
    else:
        return None

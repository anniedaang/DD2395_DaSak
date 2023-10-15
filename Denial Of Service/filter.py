#!/usr/bin/env python3

def filter_text(text):
    # empty dictionary
    law = {}

    # Iterate over each line in the provided text
    for n in text.split("\n"):
        if n.startswith("#"):
            (key, value) = map(str.strip, n[1:].split("="))
            law[key] = value
            continue

    # Iterate over each key in the 'law' dictionary.        
    for key in law.keys():
        for value in law.values() :
            if (key in value):
                return False

    # If no key was found in any value, return True
    return True
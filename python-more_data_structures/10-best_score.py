#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    value = 0
    m_key = ""
    for key in a_dictionary:
        if value < a_dictionary[key]:
            value = a_dictionary[key]
            m_key = key
    return m_key

from collections import Counter
import json

with open('pokemon.json', 'r') as file:
    pokemon_list = json.loads(file.read())

# There are 1041 Pokemon so far.
print(f"There are currently {len(pokemon_list)} Pokemon.")

"""
Don't touch the source code above.

=========================

This exam tests your knowledge in Python knowledge in concepts such as 
keywords, data types, lists, tuples, dicts, sets, and loops.

You may use Google or any of the provided references for this exam.

The plural of Pokemon is Pokemon.

Good luck!
"""

# 1. How many legendary Pokemon are there? What are their names?
# TODO: automate the answer through code.


def text_formatter(item):
    return ', '.join(map(str, item))


def pokemon_result1(pokemon):
    is_legendary = filter(lambda n: n['legendary'], pokemon)
    what_name = list(map(lambda n: n['name'], is_legendary))
    new_line = '\n'

    return (
        f'They are {len(what_name)} pokemon.{new_line}'
        f'There names are {text_formatter(what_name)}'
    )


print(pokemon_result1(pokemon_list))
# 2. Which Pokemon have the highest defense (def) stat? What are their names?
# TODO: automate the answer through code.


def is_high_def(pokemon):
    return pokemon['def'] >= max(list(map(lambda n: n["def"], pokemon_list)))


def pokemon_result2(pokemon):
    high = filter(is_high_def, pokemon)
    what_name = list(map(lambda n: n['name'], high))

    return f'The pokemon that have highest defense are {text_formatter(what_name)}'


print(pokemon_result2(pokemon_list))
# 3. How many Pokemon are overweight? What are their names?
# A Pokemon is considered overweight if their weight value is more than 60x their height value.
# TODO: automate the answer through code.


def is_overweight(pokemon):
    return pokemon['weight'] > pokemon['height'] * 60


def pokemon_result3(pokemon):
    who_is_overweight = filter(is_overweight, pokemon)
    what_name = list(map(lambda n: n['name'], who_is_overweight))
    new_line = '\n'

    return (
        f'The count of overweight pokemon are {len(what_name)}.{new_line}'
        f'They are {text_formatter(what_name)}'
    )


print(pokemon_result3(pokemon_list))
# 4. How many Pokemon have two or more variations? What are their names?
# Some Pokemon numbers are duplicated to indicate that they have multiple variations.
# Each of these variations have different abilities and stats.
# TODO: automate the answer through code.


def is_var(pokemon):
    poke_list1 = []
    poke_list2 = []
    for p in pokemon_list:
        if p['code'] != 1:
            poke_list1.append(p['name'])
            poke_list2.append(p['name'])

    poke_set1 = set(poke_list1)
    poke_set2 = set(poke_list2)
    both = poke_set1.intersection(poke_set2)
    new_line = '\n'

    return (
        f'The count of pokemon that have two or more variations are {len(both)}{new_line}'
        f'They are {text_formatter(both)}'
    )


print(is_var(pokemon_list))
# 5. Which Pokemon Type is the most common? Least common? How many Pokemon are of each Pokemon type?
# Some Pokemon have two types. The type field may be just one string, or a list of strings.
# PRO TIP: You will need to check whether the Pokemon type is a list or not. Use isinstance()
# TODO: automate the answer through code.


def pokemon_result5(pokemon):
    poke_list = []
    for elem in pokemon:
        if isinstance(elem['type'], list):
            poke_list.extend(elem['type'])
        else:
            poke_list.append(elem['type'])
    poke_count = Counter(poke_list)
    new_line = '\n'
    return (
        f'The most pokemon type are {poke_count.most_common(1)[0][0]} and '
        f'the least common type are {poke_count.most_common()[-1][0]}.{new_line}'
        f'The count of types are {poke_count}'
    )


print(pokemon_result5(pokemon_list))



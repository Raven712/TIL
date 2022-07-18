from pprint import pprint

fruits = [
    "Soursop",
    "Grapefruit",
    "Apricot",
    "Juniper berry",
    "Feijoa",
    "Blackcurrant",
    "Cantaloupe",
    "Salal berry",
    "Feijoa"]

a = {}
for i in fruits:
    if i not in a:
        a[i] = 1
    else:
        a[i] += 1  
pprint(a)
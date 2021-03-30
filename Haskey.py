dico = { "clé" : "valeur"}
def hasKey(key, dico):
    for e in dico.keys():
        if e == key:
            return True
    return False
print(hasKey("clé", dico))
words = ("Bonjour", "monsieur", "Lurkin,", "ça", "va", "bien", "?")

def buildsentence(Words):
    L = ""
    for n in words:
        L += n +" "
    return L
sentence = buildsentence(words)
print(sentence)
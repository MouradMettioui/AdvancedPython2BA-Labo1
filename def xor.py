A = {1, 2, 3, 4, 8, 9, 7, 4, 5, 2, 3}
B = {1, 2, 5, 7, 8, 9, 4, 5, 6, 9, 8, 5, 7}
def xor(A, B):
    for elem in (A, B):
        S = set (A | B) - (A&B)
        return S
print("xor:", xor(A, B))

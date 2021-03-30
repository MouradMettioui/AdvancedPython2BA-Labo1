A = {1, 2, 3, 4, 8, 9, 7, 4, 5, 2, 3}
B = {1, 2, 5, 7, 8, 9, 4, 5, 9, 8, 5, 7}
def common(A,B):
    l = len(A&B)
    return l
print(common(A,B))

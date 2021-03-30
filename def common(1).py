A = {1, 2, 3, 4, 8, 9, 7, 4, 5, 2, 3}
B = {1, 2, 5, 7, 8, 9, 4, 5, 6, 9, 8, 5, 7}
def common(A,B):
    l = 0
    for elem in (A):
        if elem in B:
            l+=1
    return l
print(common (A,B))
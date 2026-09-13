def is_sorted(n):
    for i in range(len(n)-1):
        if n[i] > n[i+1]:
            return False
    return True

print(is_sorted([1,2.3,4,5]))
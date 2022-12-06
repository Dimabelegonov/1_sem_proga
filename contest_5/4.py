def dot_product(N, vector1, vector2):
    ans = 0
    for i in range(N):
        ans += vector1[i] * vector2[i]

    return ans


def OptimalBST(p, q, n):
    e = [[i for i in range(0, n+1)] for j in range(1, n+2)]
    w = [[i for i in range(0, n+1)] for j in range(1, n+2)]
    root = [[i for i in range(1, n+1)] for j in range(1, n+1)]

    for i in range(1, n+2):
        e[i-1][i-1] = q[i-1]
        w[i-1][i-1] = q[i-1]

    for l in range(1, n+1):
        for i in range(1, n-l+2):
            j = i + l - 1
            e[i-1][j] = float("inf")
            w[i-1][j] = w[i-1][j-1] + p[j-1] + q[j]
            for r in range(i, j+1):
                t = e[i-1][r-1] + e[r][j] + w[i-1][j]
                if t < e[i-1][j]:
                    e[i-1][j] = t
                    root[i-1][j-1] = r
    return e, root


p = [0.04, 0.06, 0.08, 0.02, 0.1, 0.12, 0.14]
q = [0.06, 0.06, 0.06, 0.06, 0.05, 0.05, 0.05, 0.05]
print(OptimalBST(p, q, 7))

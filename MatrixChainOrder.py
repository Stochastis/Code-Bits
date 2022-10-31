from asyncio.windows_events import NULL


def MatrixChainOrder(p):
    # Number of matrices
    n = len(p) - 1

    # Width and height equals number of matrices
    m = [[NULL for i in range(1, n + 1)] for j in range(1, n + 1)]

    s = [[NULL for i in range(1, n)] for j in range(2, n + 1)]

    # For every matrix
    for i in range(n):
        # Set the diagonal to zeroes
        m[i][i] = 0

    # "l is the chain length"
    for l in range(2, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            m[i - 1][j - 1] = float("inf")
            for k in range(i, j):
                q = m[i - 1][k - 1] + m[k][j - 1] + p[i - 1] * p[k] * p[j]
                if q < m[i - 1][j - 1]:
                    m[i - 1][j - 1] = q
                    s[i - 1][j - 2] = k
    return m, s


def PrintOptimalParens(s, i, j):
    if i == j:
        return "A%d" % (i)
    else:
        return "(%s%s)" % (
            PrintOptimalParens(s, i, s[i - 1][j - 2]),
            PrintOptimalParens(s, s[i - 1][j - 2] + 1, j),
        )


m, s = MatrixChainOrder([5, 10, 3, 12, 5, 50, 6])

print(PrintOptimalParens(s, 1, 6))
print(s)

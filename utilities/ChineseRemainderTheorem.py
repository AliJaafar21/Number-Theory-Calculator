def chineseRemainderTheoremScenario1(m, A):
    a = []

    for i in range(len(m)):
        a.append(A % m[i])
    
    return a


def chineseRemainderTheoremScenario2(m, a):

    if (len(m) != len(a)):
        return "Mismatched list lengths"

    M = 1
    for i in range(len(m)):
        M *= m[i]

    Ms = []
    for i in range(len(m)):
        Ms.append(M//m[i])

    Minv = []
    for i in range(len(m)):
        try:
            inverse = pow(Ms[i], -1, m[i])
        except:
            return f"{Ms[i]} is not invertible for modulus {m[i]}"
        Minv.append(inverse)

    A = 0
    for i in range(len(m)):
        A += a[i] * Ms[i] * Minv[i]
    A = A % M

    return A

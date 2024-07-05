"""
免责声明：
本脚本中的参数和题目来源于网络，仅用于个人学习和研究目的。如若侵权，请联系删除。
我们不对因使用此脚本而导致的任何直接或间接损害承担责任。
脚本由 ChatGPT 辅助编写
"""

import math
import hashlib

# 给定的N和e
N = 101991809777553253470276751399264740131157682329252673501792154507006158434432009141995367241962525705950046253400188884658262496534706438791515071885860897552736656899566915731297225817250639873643376310103992170646906557242832893914902053581087502512787303322747780420210884852166586717636559058152544979471
e = 46731919563265721307105180410302518676676135509737992912625092976849075262192092549323082367518264378630543338219025744820916471913696072050291990620486581719410354385121760761374229374847695148230596005409978383369740305816082770283909611956355972181848077519920922059268376958811713365106925235218265173085

"""
连分数展开（Continued Fraction Expansion）：对于RSA公钥中的指数e和模数N，Wiener的攻击利用了e/N的连分数展开。
连分数展开是一种将一个有理数表示为整数加上一个有限个互为倒数的正整数的和的过程。

收敛分数（Convergents）：在连分数展开中，连分数的每个收敛分数（Convergent）都是e/N的一个良好的有理逼近。
如果在连分数的过程中，我们找到一个收敛分数，可以通过该分数恢复出私钥d。
"""

# 连分数展开
def continued_fraction_expansion(n, d):
    cf = []
    while d:
        q = n // d
        cf.append(q)
        n, d = d, n - q * d
    return cf

# 收敛
def convergents(cf):
    n, d = 0, 1
    n1, d1 = 1, 0
    for q in cf:
        n2, d2 = q * n1 + n, q * d1 + d
        yield n2, d2
        n, d = n1, d1
        n1, d1 = n2, d2

# 执行Wiener攻击
cf = continued_fraction_expansion(e, N)
for k, d in convergents(cf):
    if k == 0:
        continue
    phi = (e * d - 1) // k
    if (e * d - 1) % k == 0 and phi < N:
        b = N - phi + 1
        discriminant = b * b - 4 * N
        if discriminant >= 0:
            sqrt_discriminant = math.isqrt(discriminant)  # 使用math.isqrt
            if sqrt_discriminant * sqrt_discriminant == discriminant:
                x1 = (b + sqrt_discriminant) // 2
                x2 = (b - sqrt_discriminant) // 2
                if x1 * x2 == N:
                    print(f"找到d: {d}")
                    break


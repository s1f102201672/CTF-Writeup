c = 15516472635516552190199
p = 997
q = 17797338969816560423
e = 65537

N = p * q

phi = (p-1) * (q-1)
d = pow(e, -1, phi)

m = pow(c, d, N)
print(f"m = {m}")

from Crypto.Util.number import *
m_str = long_to_bytes(m)
print(f"m_ str = {m_str}")
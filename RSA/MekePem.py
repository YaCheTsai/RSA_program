import pyasn1.codec.der.encoder
import pyasn1.type.univ
import base64

p= 18177862711867466423
q= 18218475976724972063
d =268477640199541599809669755610592213833
e = 65537
n = p*q

def pempriv(n, e, d, p, q, dP, dQ, qInv):
    template = '-----BEGIN RSA PRIVATE KEY-----\n{}-----END RSA PRIVATE KEY-----\n'
    seq = pyasn1.type.univ.Sequence()
    for x in [0, n, e, d, p, q, dP, dQ, qInv]:
        seq.setComponentByPosition(len(seq), pyasn1.type.univ.Integer(x))
    der = pyasn1.codec.der.encoder.encode(seq)
    return template.format(base64.encodestring(der).decode('ascii'))
    
    
dP = d % p
dQ = d % q
qInv = pow(q, p - 2, p)

print pempriv(n, e, d, p, q, dP, dQ, qInv)
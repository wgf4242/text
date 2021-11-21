from __future__ import print_function
import time
from Crypto.Util.number import long_to_bytes


debug = True


strict = False


helpful_only = True
dimension_min = 7  # stop removing if lattice reaches that dimension
def helpful_vectors(BB, modulus):
    nothelpful = 0
    for ii in range(BB.dimensions()[0]):
        if BB[ii, ii] >= modulus:
            nothelpful += 1

    print(nothelpful, "/", BB.dimensions()[0], " vectors are not helpful")
def matrix_overview(BB, bound):
    for ii in range(BB.dimensions()[0]):
        a = ('%02d ' % ii)
        for jj in range(BB.dimensions()[1]):
            a += '0' if BB[ii, jj] == 0 else 'X'
            if BB.dimensions()[0] < 60:
                a += ' '
        if BB[ii, ii] >= bound:
            a += '~'
        print(a)
def remove_unhelpful(BB, monomials, bound, current):
    if current == -1 or BB.dimensions()[0] <= dimension_min:
        return BB
    for ii in range(current, -1, -1):
        if BB[ii, ii] >= bound:
            affected_vectors = 0
            affected_vector_index = 0
            for jj in range(ii + 1, BB.dimensions()[0]):
                if BB[jj, ii] != 0:
                    affected_vectors += 1
                    affected_vector_index = jj
            if affected_vectors == 0:
                print("* removing unhelpful vector", ii)
                BB = BB.delete_columns([ii])
                BB = BB.delete_rows([ii])
                monomials.pop(ii)
                BB = remove_unhelpful(BB, monomials, bound, ii - 1)
                return BB
            elif affected_vectors == 1:
                affected_deeper = True
                for kk in range(affected_vector_index + 1, BB.dimensions()[0]):
                    if BB[kk, affected_vector_index] != 0:
                        affected_deeper = False
                if affected_deeper and abs(bound - BB[affected_vector_index, affected_vector_index]) < abs(bound - BB[ii, ii]):
                    print("* removing unhelpful vectors", ii, "and", affected_vector_index)
                    BB = BB.delete_columns([affected_vector_index, ii])
                    BB = BB.delete_rows([affected_vector_index, ii])
                    monomials.pop(affected_vector_index)
                    monomials.pop(ii)
                    BB = remove_unhelpful(BB, monomials, bound, ii - 1)
                    return BB
    return BB





def boneh_durfee(pol, modulus, mm, tt, XX, YY):
    
    PR.< u, x, y > = PolynomialRing(ZZ)
    Q = PR.quotient(x * y + 1 - u)  # u = xy + 1
    polZ = Q(pol).lift()

    UU = XX * YY + 1
    gg = []
    for kk in range(mm + 1):
        for ii in range(mm - kk + 1):
            xshift = x ^ ii * modulus ^ (mm - kk) * polZ(u, x, y) ^ kk
            gg.append(xshift)
    gg.sort()
    monomials = []
    for polynomial in gg:
        for monomial in polynomial.monomials():
            if monomial not in monomials:
                monomials.append(monomial)
    monomials.sort()
    for jj in range(1, tt + 1):
        for kk in range(floor(mm / tt) * jj, mm + 1):
            yshift = y ^ jj * polZ(u, x, y) ^ kk * modulus ^ (mm - kk)
            yshift = Q(yshift).lift()
            gg.append(yshift)  # substitution
    for jj in range(1, tt + 1):
        for kk in range(floor(mm / tt) * jj, mm + 1):
            monomials.append(u ^ kk * y ^ jj)
    nn = len(monomials)
    BB = Matrix(ZZ, nn)
    for ii in range(nn):
        BB[ii, 0] = gg[ii](0, 0, 0)
        for jj in range(1, ii + 1):
            if monomials[jj] in gg[ii].monomials():
                BB[ii, jj] = gg[ii].monomial_coefficient(monomials[jj]) * monomials[jj](UU, XX, YY)
    if helpful_only:
        BB = remove_unhelpful(BB, monomials, modulus ^ mm, nn - 1)
        nn = BB.dimensions()[0]
        if nn == 0:
            print("failure")
            return 0, 0
    if debug:
        helpful_vectors(BB, modulus ^ mm)
    det = BB.det()
    bound = modulus ^ (mm * nn)
    if det >= bound:
        print("We do not have det < bound. Solutions might not be found.")
        print("Try with highers m and t.")
        if debug:
            diff = (log(det) - log(bound)) / log(2)
            print("size det(L) - size e^(m*n) = ", floor(diff))
        if strict:
            return -1, -1
    else:
        print("det(L) < e^(m*n) (good! If a solution exists < N^delta, it will be found)")
    if debug:
        matrix_overview(BB, modulus ^ mm)
    if debug:
        print("optimizing basis of the lattice via LLL, this can take a long time")

    BB = BB.LLL()

    if debug:
        print("LLL is done!")
    if debug:
        print("looking for independent vectors in the lattice")
    found_polynomials = False

    for pol1_idx in range(nn - 1):
        for pol2_idx in range(pol1_idx + 1, nn):
            PR.< w, z > = PolynomialRing(ZZ)
            pol1 = pol2 = 0
            for jj in range(nn):
                pol1 += monomials[jj](w * z + 1, w, z) * BB[pol1_idx, jj] / monomials[jj](UU, XX, YY)
                pol2 += monomials[jj](w * z + 1, w, z) * BB[pol2_idx, jj] / monomials[jj](UU, XX, YY)
            PR.< q > = PolynomialRing(ZZ)
            rr = pol1.resultant(pol2)
            if rr.is_zero() or rr.monomials() == [1]:
                continue
            else:
                print("found them, using vectors", pol1_idx, "and", pol2_idx)
                found_polynomials = True
                break
        if found_polynomials:
            break

    if not found_polynomials:
        print("no independant vectors could be found. This should very rarely happen...")
        return 0, 0

    rr = rr(q, q)
    soly = rr.roots()

    if len(soly) == 0:
        print("Your prediction (delta) is too small")
        return 0, 0

    soly = soly[0][0]
    ss = pol1(q, soly)
    solx = ss.roots()[0][0]
    return solx, soly


def example():
    N = 0xbadd260d14ea665b62e7d2e634f20a6382ac369cd44017305b69cf3a2694667ee651acded7085e0757d169b090f29f3f86fec255746674ffa8a6a3e1c9e1861003eb39f82cf74d84cc18e345f60865f998b33fc182a1a4ffa71f5ae48a1b5cb4c5f154b0997dc9b001e441815ce59c6c825f064fdca678858758dc2cebbc4d27
    e = 0x11722b54dd6f3ad9ce81da6f6ecb0acaf2cbc3885841d08b32abc0672d1a7293f9856db8f9407dc05f6f373a2d9246752a7cc7b1b6923f1827adfaeefc811e6e5989cce9f00897cfc1fc57987cce4862b5343bc8e91ddf2bd9e23aea9316a69f28f407cfe324d546a7dde13eb0bd052f694aefe8ec0f5298800277dbab4a33bb
    c = 0xe3505f41ec936cf6bd8ae344bfec85746dc7d87a5943b3a7136482dd7b980f68f52c887585d1c7ca099310c4da2f70d4d5345d3641428797030177da6cc0d41e7b28d0abce694157c611697df8d0add3d900c00f778ac3428f341f47ecc4d868c6c5de0724b0c3403296d84f26736aa66f7905d498fa1862ca59e97f8f866c
    delta = .18  # this means that d < N^delta
    m = 4  # size of the lattice (bigger the better/slower)
    t = int((1 - 2 * delta) * m)  # optimization from Herrmann and May
    X = 2 * floor(N ^ delta)  # this _might_ be too much
    Y = floor(N ^ (1 / 2))  # correct if p, q are ~ same size
    P.< x, y > = PolynomialRing(ZZ)
    A = int((N + 1) / 2)
    pol = 1 + x * (A + y)
    if debug:
        print("=== checking values ===")
        print("* delta:", delta)
        print("* delta < 0.292", delta < 0.292)
        print("* size of e:", int(log(e) / log(2)))
        print("* size of N:", int(log(N) / log(2)))
        print("* m:", m, ", t:", t)
    if debug:
        print("=== running algorithm ===")
        start_time = time.time()

    solx, soly = boneh_durfee(pol, e, m, t, X, Y)
    if solx > 0:
        print("=== solution found ===")
        if False:
            print("x:", solx)
            print("y:", soly)

        d = int(pol(solx, soly) / e)
        m = pow(c, d, N)
        print("private key found:", d)
        print('m is {:x}'.format(int(m)))
    else:
        print("=== no solution was found ===")

    if debug:
        print(("=== %s seconds ===" % (time.time() - start_time)))


if __name__ == "__main__":
    example()

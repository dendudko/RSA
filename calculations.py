import sympy
import math

min_gen = 555
max_gen = 777


def get_prime_core(_min_gen=min_gen, _max_gen=max_gen):
    prime = sympy.randprime(2 ** _min_gen, 2 ** _max_gen)
    return prime


def get_prime(num=1, need_less=False, _min_gen=min_gen, _max_gen=max_gen, calculating_e=False):
    i = 0
    ready_prime = get_prime_core(_min_gen=_min_gen, _max_gen=_max_gen + i)
    while not check_primes(num, ready_prime, calculating_e=calculating_e):
        ready_prime = get_prime_core(_min_gen=_min_gen, _max_gen=_max_gen + i)
        if not need_less:
            i += 1
    return ready_prime


def check_primes(_p, _q, calculating_e=False):
    if (_p != _q) and (math.gcd(_p, _q) == 1) and (sympy.isprime(_p) or _p == 1 or calculating_e) \
            and sympy.isprime(_q) and (len(str(_p)) != len(str(_q))) and (_q != 1):
        return True
    else:
        return False


def calc_n(_p, _q):
    n = _p * _q
    return n


def calc_phi(_p, _q):
    _phi = (_p - 1) * (_q - 1)
    return _phi


def calc_e(_phi):
    _e = get_prime(num=_phi, need_less=True, _min_gen=round(math.log(_phi, 2) / 100),
                   _max_gen=round(math.log(_phi, 2)), calculating_e=True)
    while not (_e < _phi):
        _e = get_prime(num=_phi, need_less=True, _min_gen=round(math.log(_phi, 2) / 100),
                       _max_gen=round(math.log(_phi, 2)), calculating_e=True)
    return _e


def calc_d(_e, _phi):
    # pow - чудо-фунцкия (возведение в степень по модулю)
    # делает то же самое, что _e ** -1 % _phi, только быстро
    # это будет важно в шифровке/дешифровке))
    _d = pow(_e, -1, _phi)
    return _d


def encode(_public_key, _text=''):
    try:
        file_r = open('decoded_text.txt', 'r', encoding='utf-8-sig')
    except FileNotFoundError:
        print('Creating missing file...')
        file_r = open('decoded_text.txt', 'w', encoding='utf-8-sig')
        file_r.close()
    file_w = open('encoded_text.txt', 'w', encoding='utf-8-sig')
    if _text == '':
        _text = file_r.read()
    for i in range(len(_text)):
        utf8_value = ord(_text[i])
        encoded_symbol = pow(int(utf8_value), _public_key[0], _public_key[1])
        print(encoded_symbol, end='')
        file_w.write(str(encoded_symbol) + '\n')
    file_w.close()
    file_r.close()
    file_public_key = open('public_key.txt', 'w', encoding='utf-8-sig')
    file_public_key.write(str(_public_key[0]) + '\n' + str(_public_key[1]))
    file_public_key.close()
    print('\nPublic key length (bit): ', round(math.log(int(str(_public_key[0]) + str(_public_key[1])), 2)))


def decode(_private_key):
    try:
        file_r = open('encoded_text.txt', 'r', encoding='utf-8-sig')
    except FileNotFoundError:
        print('Creating missing file...')
        file_r = open('encoded_text.txt', 'w', encoding='utf-8-sig')
        file_r.close()
    file_w = open('decoded_text.txt', 'w', encoding='utf-8-sig')
    decoded_text = ''
    for line in file_r:
        decoded_symbol = (chr(pow(int(line.strip()), _private_key[0], _private_key[1])))
        decoded_text += decoded_symbol
        print(decoded_symbol, end='')
    file_w.write(decoded_text)
    file_r.close()
    file_w.close()
    file_private_key = open('private_key.txt', 'w', encoding='utf-8-sig')
    file_private_key.write(str(_private_key[0]) + '\n' + str(_private_key[1]))
    file_private_key.close()
    print('\nPrivate key length (bit): ', round(math.log(int(str(_private_key[0]) + str(_private_key[1])), 2)))

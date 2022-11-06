import calculations


def main(lazy=False, p=0, q=0, _text=''):
    if lazy:
        p = calculations.get_prime(_min_gen=round(calculations.min_gen*0.7),
                                   _max_gen=round((calculations.min_gen+calculations.max_gen)*0.7))
        print('p:   ', p)
        q = calculations.get_prime(num=p)
        print('q:   ', q)

    if calculations.check_primes(p, q):
        n = calculations.calc_n(p, q)
        print('n:   ', n)
        # print(len(str(n)))

        phi = calculations.calc_phi(p, q)
        print('phi: ', phi)

        e = calculations.calc_e(phi)
        print('e:   ', e)

        d = calculations.calc_d(e, phi)
        print('d:   ', d)

        public_key = (e, n)
        private_key = (d, n)

        if _text != '':
            output_encode_decode(public_key, private_key, _text)
        else:
            output_encode_decode(public_key, private_key)
    else:
        print('Invalid value of p or q!')


def output_encode_decode(_public_key, _private_key, _text=''):
    print()
    print('Encoded text: ', end='')
    calculations.encode(_public_key, _text=_text)

    print()
    print('Decoded text: ', end='')
    calculations.decode(_private_key)
    print()


def ui():
    try:
        print('1 -- Let the program work itself.\n'
              '2 -- Input p and q.\n'
              '3 -- Encode decoded_text.txt.\n'
              '4 -- Decode encoded_text.txt.\n'
              'Input a number and press Enter...\n'
              '> ', end='')
        choice = input()

        choice2 = ''
        match choice:
            case '1':
                print('1 -- LET the program work itself.\n'
                      '2 -- Input text.\n'
                      'Input a number and press Enter...\n'
                      '> ', end='')
                choice2 = input()

            case '2':
                print('p: ', end='')
                p = input()
                print('q: ', end='')
                q = input()
                print('Text: ', end='')
                text = input()
                main(p=int(p), q=int(q), _text=text)

            case '3':
                print('e: ', end='')
                e = input()
                print('n: ', end='')
                n = input()
                print('\nEncoded text: ')
                _public_key = (int(e), int(n))
                calculations.encode(_public_key)
                print()

            case '4':
                print('d: ', end='')
                d = input()
                print('n: ', end='')
                n = input()
                print('\nDecoded text: ')
                _private_key = (int(d), int(n))
                calculations.decode(_private_key)
                print()

        match choice2:
            case '1':
                main(lazy=True)
            case '2':
                print('Text: ', end='')
                text = input()
                main(lazy=True, _text=text)

    except ValueError:
        print('Invalid input!\n')

    print('\nRestart? y/n: ', end='')
    rst = input()
    match rst:
        case 'y':
            print()
            ui()


ui()

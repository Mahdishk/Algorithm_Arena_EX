def get_array_form_input():
    user_input = input('Enter a even number and a number seprate with space:')
    return list(map(int, user_input.split()))

def malevolent(p, d):
    if d % p <= p / 2:
        return d

    for i in range(2, p * d):
        var = i * d
        if var % p <= (p / 2):
            return var

if __name__ == '__main__':
    p, d = get_array_form_input()
    print(malevolent(p, d))
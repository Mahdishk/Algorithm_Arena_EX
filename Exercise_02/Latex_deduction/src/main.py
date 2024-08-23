def latex(num, n):
    if n == 1:
        return 1
    if num < 2 ** (n-1):
        return  f"{num}+\\frac{{{latex(2 *num, n)}}}{{{latex(2*num+1, n)}}}"
    return num


if __name__ == '__main__':
    num = 1
    n = int(input())
    print(latex(num, n))
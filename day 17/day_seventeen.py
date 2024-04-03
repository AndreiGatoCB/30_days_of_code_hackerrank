S = input()
try:
    print(abs(int(S)))
except ValueError:
    print('Bad String')

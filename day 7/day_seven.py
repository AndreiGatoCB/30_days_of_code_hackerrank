def odd_even_characters(word: str) -> str:
    odd = ''
    even = ''
    for i in range(len(word)):
        if i % 2 == 0:
            even += word[i]
        else:
            odd += word[i]
    return f'{even} {odd}'


T = int(input())
if T < 1:
    T = 1
elif T > 10:
    T = 10

for i in range(T):
    S = str(input())
    print(odd_even_characters(S))

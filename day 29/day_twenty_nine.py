import re


if __name__ == '__main__':
    N = int(input().strip())
    names = []
    mails = []
    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]
        names.append(firstName)
        emailID = first_multiple_input[1]
        mails.append(emailID)

    names_2 = []
    for _ in range(len(names)):
        if re.search(r'@gmail.com', mails[_]):
            names_2.append(names[_])
        names_2.sort()
    for name in names_2:
        print(name)

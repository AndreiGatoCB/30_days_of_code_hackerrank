class Person:
    def __init__(self, initial_age):
        if initial_age < 0:
            print('Age is not valid, setting age to 0.')
            self.i_age = 0
        else:
            self.i_age = initial_age

    def am_i_old(self):
        if self.i_age < 13:
            print('You are young.')
        elif 13 <= self.i_age < 18:
            print('You are a teenager.')
        else:
            print('You are old.')

    def year_passes(self):
        self.i_age += 1


t = int(input())
for i in range(0, t):
    age = int(input())
    p = Person(age)
    p.am_i_old()
    for j in range(0, 3):
        p.year_passes()
    p.am_i_old()
    print("")

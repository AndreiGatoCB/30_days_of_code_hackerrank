day1, month1, year1 = map(int, input().split())
day2, month2, year2 = map(int, input().split())


def date(day1, month1, year1, day2, month2, year2):
    if year1 > year2:
        return 10000
    if year1 == year2:
        if month1 > month2:
            return (month1-month2) * 500
        if month1 == month2 and day1 > day2:
            return (day1-day2)*15
    return 0


hackos = date(day1, month1, year1, day2, month2, year2)
print(hackos)

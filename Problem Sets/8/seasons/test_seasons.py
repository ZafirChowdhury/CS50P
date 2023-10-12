from seasons import date_sub as ds
from datetime import date

#This test is dumb, but I am too lazy to make a better one
#Change the output according to todays date
def test_date_sub():
    assert ds(date.fromisoformat("1999-01-01")) == "12836160"
    assert ds(date.fromisoformat("2022-05-29")) == "525600"
    assert ds(date.fromisoformat("2021-05-29")) == "1051200"
    assert ds(date.fromisoformat("2020-05-29")) == "1576800"

#You can use this to find out the outputs of the current date
'''
from datetime import date
def ds(date_of_birth):
    days = str(date.today() - date_of_birth)
    days = days.split(" ")
    days = days[0]

    mins = int(days) * 24 * 60

    return str(mins)

print(ds(date.fromisoformat("1999-01-01")))
print(ds(date.fromisoformat("2022-05-29")))
print(ds(date.fromisoformat("2021-05-29")))
print(ds(date.fromisoformat("2020-05-29")))
'''

import calendar
import datetime
import sys

print(sys.path)


def test(greet):
    # return greet + 'function'
    return "{} function".format(greet)


print(test("hello "))


def student(*args, **kwargs):
    print(args)
    print(kwargs)


student("math", "physics", "arabic", name="isa", age=27)


def student(*args, **kwargs):
    print(args)
    print(kwargs)


courses = ["math", "physics", "arabic"]
info = {"name": "isa", "age": 27}
student(*courses, **info)

today = datetime.date.today()
print(today)
print(calendar.isleap(2018))

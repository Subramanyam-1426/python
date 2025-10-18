try:
    num=int(input("enter num: "))
    den=int(input("enter den: "))
    r=(num/den)
    print(f"result: {r}")
except  ZeroDivisionError:
    print("cant divide by 0")
except ValueError:
    print("value error")
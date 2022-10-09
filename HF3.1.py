def h(i):
    value_a = input("Enter 'a' value:")
    value_a = int(value_a)
    value_b = input("Enter 'b' value:")
    value_b = int(value_b)
    print(value_a/value_b)

i=0
while i <=10:
    try:
        h(i)
    except ZeroDivisionError:
        print("Can't divide by zero")
    finally:
        print("Out of try except blocks")

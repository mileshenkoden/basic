import sys

filename = "Lidst.txt"

while True:

    try:
        print("Inside try")
        my_file = open(filename, mode="r", encoding="utf-8")
        print(my_file.read())
    except Exception:
        print("inside Except")
        print("Error")
        print(sys.exc_info())

        filename = input("enter correct file name")
    else:
        print("inside else")
        print(my_file.read())
        sys.exit() #закінчити програму
    finally:
        print("Inside finally")


print("-------------EOF------------")
if __name__ == "__main__":
    try:
        a = 10
        b = int(input("Enter the age"))
        if b < 18:
            raise ZeroDivisionError("Enter age greater than 18 ")
        c = a/b
    except ZeroDivisionError as e:
        print(f"Error is {e}")
        raise Exception("Random error")
    finally:
        print("Completed")

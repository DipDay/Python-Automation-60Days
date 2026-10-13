try:
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))

    result = num1 / num2
    print(f'{num1}/{num2} = {result}')

except ZeroDivisionError:
    print("You can not divide a number by zero!")
except ValueError:
    print("Give only number!")
except Exception:
    print("Someting Wrong!")

finally:
    print("***This line will always execute!***")
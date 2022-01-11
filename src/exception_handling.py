from typing import Union

from src.no_return import never_return


def handler() -> None:
    try:
        never_return()
        print("never executed")
    except Exception as ex:
        print(f"I caught an exception: {ex}")
    print("printed after the exception")


def funny_division(divisor: float) -> Union[str, float]:
    try:
        return 100 / divisor
    except ZeroDivisionError:
        return "zero is not a good idea!"


def funnier_division(divisor: int) -> Union[str, float]:
    try:
        if divisor == 13:
            raise ValueError("13 is an unlucky number!")
        return 100 / divisor
    except (ZeroDivisionError, TypeError):
        return "enter a number other than 0"


def funniest_division(division: int) -> Union[str, float]:
    try:
        if division == 13:
            raise ValueError("13 is an unlucky number")
        return 100 / division
    except ZeroDivisionError:
        return "Enter a number other than zero"
    except TypeError:
        return "Enter a numerical value"
    except ValueError:
        print("No,no,no, not 13!")
        raise


def exception_args():
    try:
        raise ValueError("This is an argument")
    except ValueError as e:
        print(f"The exception arguments were {e.args}")


some_exceptions = [ValueError,TypeError,IndexError,None]

for choice in some_exceptions:
    try:
        print(f"\nRaising {choice}")
        if choice:
            raise choice("An error")
        else:
            print("no exception raised")
    except ValueError:
        print("Caught a ValueError")
    except TypeError:
        print("Caught a TypeError")
    except Exception as e:
        print(f"caught some other exception: {e.__class__.__name__}")
    else:
        print("THis code called if there no exception")
    finally:
        print("This cleanup code is always called")


def divide_with_exception(dividend: int,
                          divisor: int) -> None:
    try:
        print(f"{dividend/ divisor=}")
    except ZeroDivisionError:
        print("You can't divide by zero")


def divide_with_if(dividend: int,
                          divisor: int) -> None:
    if divisor == 0:
        print("You can't divide by zero")
    else:
        print(f"{dividend/ divisor=}")
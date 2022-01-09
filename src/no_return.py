from typing import NoReturn

def never_return() -> NoReturn:
    print("I am about to raise an exception")
    raise Exception("This is always raised")
    print("This is not goint to be printed")
    return "I won't be returned"

def call_exceptor() -> None:
    print("call_exceptor starts here...")
    never_return()
    print("an exception was raised...")
    print("...so these lines don't line")

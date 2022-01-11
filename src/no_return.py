from typing import NoReturn


def never_return() -> NoReturn:
    print("I am about to raise an exception")
    raise Exception("This is always raised")


def call_exceptor() -> None:
    print("call_exceptor starts here...")
    never_return()
    print("an exception was raised...")
    print("...so these lines don't line")

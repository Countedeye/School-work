#!/usr/bin/env python3

# Module exports are defined in the global scope of the module
#   (left-most indentation level)

VERSION = "0.0.1"

foo_name = "Foo"
def foo_says(x):
    print(f"{foo_name}: {x}")


class Foo:
    def __init__(self):
        self.foo = "FOO"


# Test your code within the module here
if __name__ == "__main__":
    # Things defined in the scope will not be exported by the module
    print(f'Running tests for "{__file__}" (v{VERSION})...')

    foo_says("In future modules, these tests will be defined by you!")
    foo_name = "You"
    foo_says("Got it!")

    f1 = Foo()
    print(f1)
    print(hex(id(f1)))
    print(f1.foo)

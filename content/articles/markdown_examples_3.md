Title: Markdown Examles Part 3
Author: Markie Tee
Date: 2019-05-23 04:26
Category: testing
Tags: markdown, pygments

Code blocks are preceded by an indent, three : symbols and the name of the language.
All of the following code will be highlighted while the text is indented.

    :::python3
    def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        return func(*args, **kwargs).lower()
    return wrapper_do_twice

    @do_twice
    def say_whee(some_text):
        print(some_text)

    x = 'Whee!'
    say_whee(x)

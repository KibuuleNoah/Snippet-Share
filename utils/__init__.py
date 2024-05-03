from django.shortcuts import redirect


# authentication decorator
def is_authenticated(func):
    def inner(*args, **kwargs):
        if args[0].user.is_authenticated:
            return func(*args, **kwargs)
        return redirect("login")

    return inner

from django.shortcuts import redirect


def add_groups(registerFun):
    def wrapperFunc(request, *args, **kwargs):
        return redirect('login')
    return wrapperFunc    
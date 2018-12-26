from django.shortcuts import render, redirect

def validate(fun):
    def inner(request, *args, **kwargs):
        try:
            if request.session['username']:
                return fun(request, *args, **kwargs)
            else:
                return redirect('/login')
        except:
            return redirect('/login')
    return inner
from django.shortcuts import render


# Create your views here.
def about(request):
    return render(
        request=request,
        template_name='about.html',
    )


def rules(request):
    return render(
        request=request,
        template_name='rules.html',
    )
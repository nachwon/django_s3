from django.shortcuts import render, redirect

from practice.models import Image


def test(request):
    if request.method == 'POST':
        img = request.FILES.get('img-file')
        Image.objects.create(img=img)
        return redirect(test)
    else:
        img = Image.objects.first()
    context = {
        'object': img
    }
    return render(request, 'index.html', context)

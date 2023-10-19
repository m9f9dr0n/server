from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string

def index(request):
    HttpResponse('Это номер ')

def categories(request, cat_id):
    if cat_id == 1:
       return HttpResponse(f'Это номер {cat_id}')
    elif cat_id == 2:
       return HttpResponse('<img width="470" height="300" src= "https://avatars.mds.yandex.net/i?id=f65e7b89323756376f023b92bc61a0efd7b11653-10841731-images-thumbs&n=13"><h1>Это кошка<h1></img>')
    elif cat_id == 3:
       return HttpResponse('<img width="390" height="300" src= "https://avatars.mds.yandex.net/i?id=48ccb8ef3caecf4b3492b79d1ab912754f755456-10139465-images-thumbs&n=13"><h1>Это собака<h1></img>')
    elif cat_id == 4:
        return HttpResponse('<img width="390" height="300" src= "https://laplaya-rus.ru/wp-content/uploads/f/f/a/ffa5113fbfc14d952281b3f2e56eae58.jpeg"><h1>Это черепаха<h1></img>')
    elif cat_id == 5:
        return HttpResponse('<img width="390" height="300" src= "https://avatars.mds.yandex.net/i?id=847cc0b517a674927cc31688da2fa14e4fba63d9-9837140-images-thumbs&n=13"><h1>Это попугай<h1></img>')
    elif cat_id == 6:
        return HttpResponse('<img width="390" height="300" src= "https://avatars.mds.yandex.net/i?id=be8f8b8e39a96dd5e5cad41fe7d369de500e2d36-4519223-images-thumbs&n=13"><h1>Это хомяк<h1></img>')
    elif cat_id == 7:
        return HttpResponse('<img width="390" height="300" src= "https://avatars.mds.yandex.net/i?id=f058d276f426b3c3d4de707755998c7e09e64401-10414364-images-thumbs&n=13"><h1>Это морская свинка<h1></img>')
    elif cat_id == 8:
        return HttpResponse('<img width="390" height="300" src= "https://avatars.mds.yandex.net/i?id=34ba2778e69714c054b3d848f68c5230b8016dac-10637415-images-thumbs&n=13"><h1>Это шиншилла <h1></img>')
    elif cat_id == 9:
        return HttpResponse('<img width="390" height="300" src= "https://avatars.mds.yandex.net/i?id=1ba6a555cdb652c850f69570fff90556da6ec5ce-10597937-images-thumbs&n=13"><h1>Это золотая рыбка<h1></img>')
    elif cat_id == 10:
        return HttpResponse('<img width="390" height="300" src= "https://avatars.mds.yandex.net/i?id=f489d21cabd99d5b12ad93e487d9649c91bacf21-9181986-images-thumbs&n=13"><h1>Это мышь<h1></img>')
    elif cat_id == 11:
        return HttpResponse('<img width="390" height="300" src= "https://avatars.mds.yandex.net/i?id=6a6c9459b0c5483eefa093e7d63b5e314a475ab0-10636921-images-thumbs&n=13"><h1>Это кролик<h1></img>')
    else:
        return HttpResponse('<h1>Эту страницу я ещё не разработал<h1>')


def index(request):# HttpRequest
    t = render_to_string('women/index.html')
    return HttpResponse(t)


from django.http import HttpResponse


def hello(request):
     print(request.COOKIES)
     num_visits = request.session.get('num_visits', 0) + 1
     request.session['num_visits'] = num_visits
     if num_visits > 999999999 : del(request.session['num_visits'])
     resp = HttpResponse('Cookie for f5b2af70... and view count='+str(num_visits))
     resp.set_cookie('dj4e_cookie', 'f5b2af70', max_age=1000)
     return resp




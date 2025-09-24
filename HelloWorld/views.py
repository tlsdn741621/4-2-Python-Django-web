from http.client import HTTPResponse

# MVC에서 C의 역할은, 장고 MVT에서, V가 그 역할 함.
def django_view(request):
    return HTTPResponse("Django View")
from django.http import JsonResponse
# from django.shortcuts import render


# Create your views here.
def test_cors(request):
    return JsonResponse({'msg': 'CORS is ok'})

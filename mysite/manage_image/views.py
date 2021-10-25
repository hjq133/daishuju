from django.http import HttpResponse
from user_login.views import authentication
from django.http import JsonResponse, HttpResponse
from django.db.models import Q
from .models import Images


def index(request):
    return HttpResponse("Hello, world. You're at the manage image index.")


# 添加新的镜像
def create_image(request):
    print('create images')
    user = authentication(request)
    if user is None:
        return HttpResponse('Unauthorized', status=401)
    name = request.POST.get("name")
    port = request.POST.get("port")
    dir = request.POST.get("dir")
    cpu = request.POST.get("cpu")
    ram = request.POST.get("ram")
    disk = request.POST.get("disk")
    if not Images.objects.filter(Q(user=user) & Q(name=name)):
        image = Images.objects.create(user=user, name=name, port=port, dir=dir, cpu=cpu, ram=ram, disk=disk)
        data = {'status': "success", "message": None}
    else:
        data = {'status': "failed", "message": "name already exists"}
    return JsonResponse(data)


# 获取user的镜像列表
def get_image_list(request):
    print('get image list')
    user = authentication(request)
    if user is None:
        return HttpResponse('Unauthorized', status=401)
    images = Images.objects.filter(user=user)
    data = []
    for image in images:
        data.append({'name': image.name,
                     "port": image.port,
                     "dir": image.dir,
                     "ram": image.ram,
                     "cpu": image.cpu,
                     "disk": image.disk, })
    return JsonResponse({"my_images": data})


# 删除镜像
def delete_image(request):
    user = authentication(request)
    if user is None:
        return HttpResponse('Unauthorized', status=401)
    name = request.POST.get("name")
    try:
        image = Images.objects.get(user=user, name=name)
        print("image", image)
        image.delete()
        data = {"status": 'success', "message": None}
        print('success')
    except:
        data = {"status": 'failed', "message": "image not exists"}
        print('failed')
    return JsonResponse(data)

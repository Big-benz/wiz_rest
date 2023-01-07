from rest_framework.decorators import api_view
from rest_app.serializers import myStaffs
from rest_app.models import Staff
from rest_framework.response import Response


@api_view(['GET'])
def get(request):
    staffs = Staff.objects.all()
    serializers = myStaffs(staffs, many = True)
    return Response(serializers.data)


@api_view(['POST'])
def post(request):
    serializers = myStaffs(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data)
    else:
        return Response(serializers.error)
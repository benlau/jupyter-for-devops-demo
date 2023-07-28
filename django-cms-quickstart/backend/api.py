from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User
from django.core.serializers import serialize

def health(_request):
    return JsonResponse({'status': 'ok'})

@api_view(['GET'])
@permission_classes([IsAdminUser])
def list_user(_request):
    admin_users = User.objects.filter(is_staff=True)
    admin_users_json = serialize('json', admin_users, fields=('username', 'email'))

    return JsonResponse({'users': [
        {
            'username': admin_user.username,
            'email': admin_user.email,
        }
        for admin_user in
        admin_users]})


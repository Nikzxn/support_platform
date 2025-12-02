from django.conf import settings
from django.shortcuts import redirect

class AccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            current_url = request.path

            if current_url.startswith('/operator/'):
                is_operator = request.user.groups.filter(name='Operators').exists()
                if not (is_operator or request.user.is_superuser):
                    return redirect(settings.OPERATOR_LOGIN_URL)

            elif current_url.startswith('/admin/dashboard/'):
                if not request.user.is_superuser:
                    return redirect(settings.ADMIN_LOGIN_URL)

        response = self.get_response(request)
        return response

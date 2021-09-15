from django.contrib import auth
from django.utils.deprecation import MiddlewareMixin

# Função disponibilizada pelos engenheriso de segurança
def get_user(request):
    # Se a requisição tem um JWT Token use a função de JWT Token
    if request.headers.get('JWT') is True:
        return auth.get_user_with_jwt(request)

    # Se a requisição tem um Basic Auth use a função de Basic Auth
    if request.headers.get('Basic-Auth') is True:
        return auth.get_user_with_basic_auth(request)

    # Se a requisição tem um Cookie use a função de Cookie
    if request.headers.get('Cookie') is True:
        return auth.get_user_with_cookie(request)

    # Caso não tenha autenticação, retorne uma instância de um usuário anônimo
    return auth.AnonymousUser()


class AuthenticationMiddleware(MiddlewareMixin):
    # Middleare atua na entrada da requisição
    def process_request(self, request):
        request.user = get_user(request)

    # Middleare não faz nada na saída da response
    def process_response(self, request, response):
        pass
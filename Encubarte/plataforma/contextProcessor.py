from Encubarte.plataforma.parametros import parametros

def nombreOrganizacion(request):
    nombreOrganizacion=parametros["nombreOrganizacion"]
    return {
        'nombreOrganizacion': nombreOrganizacion,
    }
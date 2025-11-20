from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Mensaje, Empresa
import json

# Create your views here.

@csrf_exempt
def create_mensaje(request) -> HttpResponse:
    """View to create a new Mensaje.
    param request: HttpRequest object containing request data
    return: HttpResponse with the result of the operation
    """

    if request.method == 'GET':
        return HttpResponse("Render the form to create a new mensaje.")

    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            nombre = data.get('nombre')
            apellido = data.get('apellido')
            correo = data.get('correo')
            telefono = data.get('telefono')
            mensaje_text = data.get('mensaje')
            empresa_id = data.get('empresa_id')

            try:
                empresa = Empresa.objects.get(pk=empresa_id)
            except Empresa.DoesNotExist:
                return JsonResponse({
                    'error': f'Empresa with id {empresa_id} does not exist'
                }, status=404)

            mensaje = Mensaje.objects.create(
                nombre=nombre,
                apellido=apellido,
                correo=correo,
                telefono=telefono,
                mensaje=mensaje_text,
                empresa=empresa
            )

            return JsonResponse({
                'message': 'Mensaje created successfully',
                'id': mensaje.id,
                'nombre': mensaje.nombre,
                'apellido': mensaje.apellido,
                'correo': mensaje.correo
            }, status=201)

        except json.JSONDecodeError:
            return JsonResponse({
                'error': 'Invalid JSON format'
            }, status=400)
        except Exception as e:
            return JsonResponse({
                'error': str(e)
            }, status=500)

    return HttpResponse("Render the form to create a new mensaje.")


def get_mensajes_by_empresa(request, empresa_id) -> HttpResponse:
    """View to retrieve all Mensajes for a specific Empresa.
    param request: HttpRequest object
    param empresa_id: ID of the Empresa
    return: HttpResponse with the list of mensajes
    """
    mensajes = Mensaje.get_mensajes_by_empresa(empresa_id)
    mensajes_data = [{
        'id': mensaje.id,
        'nombre': mensaje.nombre,
        'apellido': mensaje.apellido,
        'correo': mensaje.correo,
        'telefono': mensaje.telefono,
        'mensaje': mensaje.mensaje,
        'empresa_id': mensaje.empresa.id
    } for mensaje in mensajes]

    return JsonResponse({'mensajes': mensajes_data}, status=200)
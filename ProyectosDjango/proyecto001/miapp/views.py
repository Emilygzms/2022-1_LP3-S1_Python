from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

layout = """
    <h1>Proyecto Web (LP3) | Emily Gomez </h1>
    <hr>
    <ul>
        <li>
            <a href= "/inicio"> Inicio </a>
        </li>
        <li>
            <a href= "/saludo"> Mensaje de saludo </a>
        </li>
        <li>
            <a href= "/rango"> Mostrar Número [10,20]</a>
        </li>
    </ul>  
    <hr>  
"""

def index(request):

    estudiantes = ['Luis Serna', 
                    'Antony Ccaccya', 
                    'Carlos Granados']

    return render(request, 'index.html', {
        'titulo': 'Inicio',
        'mensaje': 'Proyecto Web con Django (Desde el View)',
        'estudiantes': estudiantes
    })

def saludo(request):
    return render(request, 'saludo.html', {
        'titulo': 'Bienvenidos! *w*',
        'autor_saludo': 'Emily Gomez Marcos'
    })

def rango(request):

    a = 10
    b = 20

    rango_numeros = range(a, b+1)

    return render(request, 'rango.html',{
        'titulo': 'Rango [a,b]',
        'a': a,
        'b': b,
        'rango_numeros': rango_numeros

    })


def rango2(request, a, b):

    if a>b:
        return redirect('rango2', a=b, b=a)
    resultado = """
        <h2> Números de [{a}, {b}] </h2>
    """

    resultado = f"""
        <h2> Número de [{a},{b} ]</h2>
        Resultado: <br>
        <ul>
    """
    while a<=b:
        resultado += f"<li> {a} </li>"
        a+=1
    resultado += "</ul>"
    return HttpResponse(layout + resultado)
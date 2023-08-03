



# Create your views here.

from django.http import HttpResponse 
from django.shortcuts import render, redirect


layout = """
<h1> SITIO WEB CON DJANGO</h1>
<hr/>
<ul>
    <li> 
        <a href="/index"> Inicio </a>
    </li>   
    <li> 
        <a href="/pagina2"> Pagina 2 </a>
    </li>   
    <li> 
        <a href="/pagina3"> Pagina 3 </a>
    </li>      
 <li> 
        <a href="/contacto"> contacto </a>
    </li>   
</ul>

<HR/>

"""


def pagina2(request):
    
   return render(request, 'pagina2.html')
                  



def index(request):
    
    html = """"
        <h1>Inicio</h1>   
        <p>Años hasta 2050 </p>                 
        <ul>
    """
    year = 2021
    
    
    while year <= 2050:
    

        html += f"<li>{str(year)}</li>"
        year += 1
        
    html += "</ul>"
    return render(request, 'index.html', {
        
        'mi_variable':'soy un dato que está en la vista'
        
        }')



    #HttpResponse(layout+html)


def pagina3(request):
    return render(request,'pagina3.html') 
                    
       
   
def contacto(request, nombre="", apellidos=""):
    return render(request, 'contactos.html')

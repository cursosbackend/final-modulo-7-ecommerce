from django.urls import path
from . import views


# el requests  llega desde el router aca y cada ruta gatilla un funcion 
urlpatterns = [
    path("productos/",views.lista_productos, name="lista_productos"),
    path("crear/",views.crear_producto, name="crear_producto"),
    

]

crear carpetas

mkdir projecto
cd projecto
mkdir backend
cd backend

# Entorno virtual d epython

# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En Windows:
venv\Scripts\activate

# Installacion de dependencias de django
pip install django djangorestframework pillow django-cors-headers python-decouple

# Crear productos backend 
django-admin startproject productos_backend .

# cambiar carpeta
cd productos_backend

# Iniciar projecto
python manage.py startapp productos

# installar mysqlclient
pip install mysqlclient

# instalar pymysql en caso de tener problemas con mysqlclient
pip install PyMySQL

# verificaicon de errores
python manage.py check

# Crear superusuario
python manage.py createsuperuser

# Ejecutar servidor
python manage.py runserver

# installar angular
npm install -g @angular/cli@18

# isntallar depencias adicionales 
npm install @angular/common@18 @angular/forms@18

# iniciar fontend 
ng serve

# activar entorno virtual
venv\Scripts\activate
### Exportar nuestra aplicacion

    $ export FLASK_APP=src/app.py

    > SET FLASK_APP=src/app.py

### Generar migrations usando flask

    Inicializar migraciones:

    $ flask db init 

    Crear migraciones:

    $ flask db migrate

    Generar tablas o cambios en la base de datos:

    $ flask db upgrade
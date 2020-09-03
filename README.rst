django-formset
==============

Una aplicacion que proporciona clases genericas para utilizar en los
CBV's como un Mixin.
La finalidad de este es facilitar el manejo de los formset dentro del view,
lo mas reusable posible.

Además contiene un templatetag para renderizar de forma simple el formset en
en el template con estilos, y con funcionalidades como agregar y eliminar forms 
de forma dinamica con javascript.


Quick start
-----------

1. Download django-formset app. Passing a branch name, a commit hash, a tag name or a git ref is possible like so::

    pip install [opt]

    opt:
        git+https://github.com/chelobaeza/django-formset.git@master#egg=django-formset
        git+https://github.com/chelobaeza/django-formset.git@develop#egg=django-formset
        git+https://github.com/chelobaeza/django-formset.git@v1.0#egg=django-formset
        git+https://github.com/chelobaeza/django-formset.git@da39a3ee5e6b4b0d3255bfef95601890afd80709#egg=django-formset
        git+https://github.com/chelobaeza/django-formset.git@refs/pull/123/head#egg=django-formset


2. Add "formset" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'formset',
    ]


3. Include the formset URLconf in your project urls.py like this::

    path('formset/', include('formset.urls')),

4. Run ``python manage.py migrate`` to create the models.


Usando formset en template
--------------------------

Se necesita cargar el templatetag 'formset' y luego llamar al tag que
incluye el template.
Donde formset_object es la variable formset en el contexto::
    
    {% load formset %}
    ...
    {% formset formset_object %}
    

Archivos estaticos
------------------

Al utilizar el templatetag renderiza un template el cual carga automaticamente
los archivos estáticos necesarios.
En caso que se utilicen mas de un formset, se puede prevenir la carga de los
estaticos en cada formset::

    {% formset formset_object static=False %}

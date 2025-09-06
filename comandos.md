# Comandos Máquina Virtual:
* pip install virtualenv
* virtualenv (nome da env)
* source (nome da env)/Scripts/activate


# Comandos Django:
* pip install django

* django-admin startproject (nome do projeto) ## cria um novo projeto

* python manage.py runserver ## roda o servidor local django

* python manage.py startapp (nome do app) ## cria um novo app dentro do projeto.

* python manage.py makemigrations ## identifica as mudanças realizadas no projeto e as prepara para serem salvas, reconhecidas e se necessário, atualizadas no banco de dados.

* python manage.py migrate ## realiza tudo que foi organizado em makemigrations



# Estrutura do Django (MAIN):
* manage.py ## arquivo de comunicação com funções nativas do django

* settings.py ## arquivo de configurações do projeto, como um painel de controle (banco de dados, Apps instalados, Middlewares, idiomas, templates, fuso horário, etc)
OBS: Todos os novos Apps devem ser configurados aqui

* urls.py ## define as rotas do projeto, principalmente, qual rota chama qual view.

* asgi.py ## arquivo de configuração para rodar django com servidores assíncronos (Uvicorn, Hypercorn etc)

* wsgi.py ## arquivo de configuração para rodar django com servidores web comuns (Gunicorn, uWSGI, etc)



# Estrutura Django (APP):
* init.py  ## identifica a pasta como um módulo Python, permitindo que o Django e o Python reconheçam o app.  

* admin.py  ## arquivo usado para registrar os modelos do app no painel administrativo do Django.  
  Ex: `admin.site.register(MeuModelo)`  

* apps.py ## contém a configuração da aplicação, como nome do app e metadados.  
  É carregado pelo Django ao iniciar.  

* models.py  ## onde se definem os modelos (classes que representam tabelas do banco de dados). 

* views.py ## arquivo que contém as views.

* urls.py ## arquivo de URLs específicas sobre esse app

* tests.py ## arquivo de testes automatizados para verificar se o app funciona corretamente.



# Conceitos Django:
* View: Uma função ou classe responsável por lidar com requisições HTTP e devolver uma resposta. ## Fluxo de funcionamento: URL -> View (processa a lógica, BD, etc) -> resposta HTTP

* Server Síncrono: WSGI (Web Server Gateway Interface), server que atende uma requisição por vez. ##Apps pequenos e simples

* Server Assíncrono: ASGI (Asynchronous Server Gateway Interface), server que atende várias requisições por vez. ## Apps em tempo real ou muitas conexões.

* Apps: Componentes (módulo) que controlam algumas partes do nosso projeto.

* templates: Pasta com os arquivos html que serão utilizados.
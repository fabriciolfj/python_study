# python_study
- para executar os testes
```
python3 -m pytest
```
- montando um ambiente virtual, para isolar sua app ou módulo
```
python3 -m venv ll_env
```
- para ativar o ambiente virtual
```
source ll_env/bin/activate
```
- para desativar
```
deactivate
```
- com o ambiente ativo, execute
```
pip3 install --upgrade 
pip3 install django
```
- criando um projeto novo com o django
```
django-admin startproject ll_project . //sempre com esse ponto
```
- criando uma base de dados, utilizando sqllite
```
python3 manage.py migrate
```
- para iniciar o projeto, execute
```
python3 manage.py runserver
```
- criar estrutura  (package com classe model, view e controller do java por ex)
```
python3 manage.py startapp learning_logs
```
- para saber os tipos de campos que podemos utilizar do model: https://docs.djangoproject.com/en/4.1/ref/models/fields/
- depois de criar o model, para gerar o arquivo de migração, execute o comando no terminal:
```
python3 manage.py makemigrations learning_logs
```
-  para efetuar a migração, ou seja, modificar a base para atender o model, execute:
```
python3 manage.py migrate
```
- para testar nossa app, podemos acessar o shell do django
```
python3 manage.py shell
```
- por ele, podemos fazer consultas na nossa base, como recuperar todos os topics:
````
from learning_logs.models import Topic
t = Topic.objects.all() //todos os topics

t = Topic.objects.get(id=1) // pegando um topic específico
t.text //printando o texto

t.entry_set.all() //pegando as entradas do topic, lembrando que entry depende de topic, então para acessá-lo digite em letra minuscula, com sufixo _set
````
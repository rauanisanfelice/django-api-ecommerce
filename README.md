![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/rauanisanfelice/django-api-ecommerce.svg)
![GitHub top language](https://img.shields.io/github/languages/top/rauanisanfelice/django-api-ecommerce.svg)
![GitHub pull requests](https://img.shields.io/github/issues-pr/rauanisanfelice/django-api-ecommerce.svg)
![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/rauanisanfelice/django-api-ecommerce)
![GitHub contributors](https://img.shields.io/github/contributors/rauanisanfelice/django-api-ecommerce.svg)
![GitHub last commit](https://img.shields.io/github/last-commit/rauanisanfelice/django-api-ecommerce.svg)

![GitHub stars](https://img.shields.io/github/stars/rauanisanfelice/django-api-ecommerce.svg?style=social)
![GitHub followers](https://img.shields.io/github/followers/rauanisanfelice.svg?style=social)
![GitHub forks](https://img.shields.io/github/forks/rauanisanfelice/django-api-ecommerce.svg?style=social)

# Django API E-Commerce

Projeto em Python utilizando Django para criar API de E-Commerce.

## Tela de Início
![Tela início](https://raw.githubusercontent.com/rauanisanfelice/django-api-ecommerce/develop/img/Tela_01.png)

## Tela de Login
![Tela Login](https://raw.githubusercontent.com/rauanisanfelice/django-api-ecommerce/develop/img/Tela_02.png)


## Instruções

1. Virtual env;
2. Dependências;
3. Criando arquivo .env;
4. Baco de dados (caso não tenha);
    1. Configurando o pgAdmin;
5. Migrando conf. para o BD;
6. Criando Super Usuário;
7. Inicializando servidor;

### Virtual env
```
virtualenv -p python3 env
source env/bin/activate
```

### Dependências
```
pip3 install -r requirements.txt
```

### Criando arquivo .env

Copie o conteúdo do arquivo env-example e crie um novo arquivo .env, cole o conteúdo. Crie uma SCRET KEY.

### Baco de dados (caso não tenha)
```
docker-compose up -d
```

#### Configurando o pgAdmin

Acesse o link:

[pgAdmin](http://localhost:80)

Realize o login:
>User: admin  
>Pass: admin

Clique em: Create >> Server

Conecte no Banco com os seguintes parâmetros:  

|Chave|Valor|
|--|--|
|Name | #nome desejado# |
|Host | postgre|
|Port | 5432|
|DB  | postgres|
|User | admin|
|Pass | docker123|


### Migrando conf. para o BD
```
python manage.py migrate
```

### Criando Super Usuário
```
python manage.py createsuperuser
```


### Inicializando servidor

```
python manage.py runserver 8000 --noreload
```

> http://localhost:8000/admin


# Referências

[Django](https://www.djangoproject.com/)  
[Django Rest Framework](https://www.django-rest-framework.org)   
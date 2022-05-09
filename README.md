# web-app-flights


## Primeiros passos para correr aplicação
1. Abra a linha de comandos (PowerShell ou cmd)
1. Descarregue uma cópia (clone) do repositório com o comando `git clone https://github.com/teoria-da-computacao/web-app-flights` 
1. Entre na pasta  `cd web-app-flights`
1. Garanta que tem o pipenv instalado, correndo o comando `python3 -m pip install pipenv`
1. Crie um ambiente virtual `pipenv install django` 
1. Active o ambiente virtual `pipenv shell`
3. Lance a aplicação no browser com o comando `python manage.py runserver`. 
4. Tem disponíveis as aplicações hello no link `http://127.0.0.1:8000`
6. abra a pasta com o Pycharm ou VS Code, para a explorar.
7. devera criar um superuser `python manage.py createsuperuser` para pode aceder ao modo admin e ditar diretamente a base de dados
5. aceda à aplicação admin, em  `http://127.0.0.1:8000/admin`

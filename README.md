# townsq-planos
Um projeto com o objetivo de demonstrar os testes funcionais

# Projeto para demonstrar testes funcionais

Um projeto onde realizo os testes em um sistema de solicitação de demonstração, o objetivo foi aprender mais sobre testes funcionais e a como documentar eles com "casos de teste";

![image](https://user-images.githubusercontent.com/50607185/204666885-fef6d8c1-11e8-4c93-b0bd-e1f5185a449a.png)


# Documentação: Casos de testes

![image](https://user-images.githubusercontent.com/50607185/204667043-1aa9b7be-9379-4575-ad74-854d2d925642.png)
![image](https://user-images.githubusercontent.com/50607185/204667108-4aad5965-677a-4811-a6dd-a0e7db952dbb.png)
![image](https://user-images.githubusercontent.com/50607185/204667438-324600cd-f571-497c-9cc0-bf44e0ad7d70.png)
![image](https://user-images.githubusercontent.com/50607185/204667475-1fb1e0a7-d65b-4df6-aa63-e99af0a8f457.png)
![image](https://user-images.githubusercontent.com/50607185/204667522-f9e3e4ff-1fcd-4d2c-8c6b-389a9459d8c0.png)
![image](https://user-images.githubusercontent.com/50607185/204667567-a64a13a3-3221-465c-8008-54f678ab2b12.png)
![image](https://user-images.githubusercontent.com/50607185/204667587-5ef4a9b3-1b20-436c-8fa2-c6712bda9012.png)
![image](https://user-images.githubusercontent.com/50607185/204667621-f72c68df-6a33-4d83-afc8-d0164ff93fd6.png)
![image](https://user-images.githubusercontent.com/50607185/204667660-9fea5e74-9b16-4b8b-b984-dc949c6be2de.png)
![image](https://user-images.githubusercontent.com/50607185/204667697-a4b03ba3-16d1-4c2d-ad80-8884aa6271c9.png)

**Foi utilizado o selenium nessa automatização**

***

## 🚀 Começando

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

<ul>
    <li>Versão do python utilizada: 3.10.7</li>
    <li>Versão do django: 4.1.2</li>
    <li>Versão do Chromedriver: 107.0.5304 (VERIFIQUE A SUA VERSÃO DE CHROME)</li>
</ul>


#### 1 - Passo: Clone
Realize um clone do projeto em seu computador

```
git clone https://github.com/walexhenrique/lista-de-tarefas-cbv.git
```

#### 2 - Passo: Ambiente virtual
Crie um ambiente virtual na pasta <b>raiz</b> do projeto. No seu terminal use:

Comando para a criação do ambiente virtual no Windows:
```
python -m venv venv
```

Comando para a criação do ambiente virtual no Linux:
```
python3 -m venv venv
```

#### 3 - Passo: Ativação do ambiente virtual
Agora você precisa ativar o ambiente virtual para a posterior instalação das dependências do projeto.

Na pasta raiz do projeto, onde você criou o seu ambiente virtual anteriormente. Use:

Comando para a ativação do ambiente virtual no Windows:
```
.\venv\Scripts\activate
```

Comando para a ativação do ambiente virtual no Linux:
```
source venv/bin/activate
```
Se tudo estiver ocorrido bem, terá (venv) em seu <b>terminal!</b>

#### 4 - Passo: Instalação de depedências
É preciso instalar as depedências do projeto para o funcionamento correto. Com o seu ambiente virtual <b>ativo</b> use o comando no seu terminal:

```
pip install -r requirements.txt
```

#### 6 - Passo: Realize as migrações
Para o correto funcionamento do projeto é preciso que seja feito as migrações do banco de dados.

No seu terminal digite:
Windows:
```
python manage.py migrate
```

Linux:
```
python3 manage.py migrate
```

#### 7 - Passo: Executar o projeto
Comando para a execução do projeto no windows:

```
python manage.py runserver
```

Comando para a execução do projeto no linux:

```
python3 manage.py runserver
```

## ⚙️ Executando os testes
Foram realizados diversos testes funcionais, simulando um usuário real no sistema.

Comando para a realização dos testes. 
No windows:
```
python manage.py test
```

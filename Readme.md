# Louis' Italian Restaurant

Sistema de reservas para o restaurante fictício onde Michael Corleone encontrou Sollozzo e McCluskey.

![GIF do Giphy](https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExenc1cTY2c3oydW9ybGgwZzN5MGtlNHU0MGl0Y3dtenVsNDhnZTAzNyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l4FGA5yLpEhfONOtW/giphy.gif)

## Stacks

- **Back-end:** Python (Flask)
- **Banco de dados:** SQLite
- **Arquitetura:** MVC (Model-View-Controller)
- **Testes:** Pytest

## Estrutura do Projeto

```
backend/
├── init/            # Scripts de inicialização do banco
├── src/             # Código fonte principal
│   ├── controllers/ # Lógica de negócio (clientes, reservas, mesas)
│   ├── errors/      # Manipulação de erros
│   ├── main/        # Inicialização do servidor e rotas
│   ├── models/      # Modelos de dados
│   ├── validators/  # Validações
│   └── views/       # Respostas das rotas
├── test/            # Testes automatizados
├── database.db      # Banco de dados SQLite
├── requirements.txt # Dependências Python
├── run_tests.py     # Script para rodar testes
└── pytest.ini       # Configuração do Pytest
```

## Como começar

1. **Clone o repositório**
   ```sh
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd LouisItalianRestaurant
   ```

2. **Instale as dependências**
   ```sh
   pip install -r backend/requirements.txt
   ```

3. **Inicie o banco de dados**
   ```sh
   sqlite3 backend/src/database.db < backend/init/schema.sql
   ```

4. **Execute o servidor Flask**
   ```sh
   python backend/src/run.py
   ```

   O servidor estará disponível em `http://localhost:5000`.

## Rodando os testes

Execute todos os testes automatizados com:

```sh
python backend/run_tests.py
```
ou
```sh
pytest backend/test/
```

## Endpoints principais

- `GET /customers` — Lista clientes
- `POST /reservations` — Cria reserva
- `GET /tables` — Lista mesas
- Outros endpoints podem ser encontrados em [backend/src/main/routes/](backend/src/main/routes/)

## Observações

- O front-end será implementado futuramente.



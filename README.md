# Instruções para Executar a API Django

Este é um guia simples para ajudá-lo a executar a API Django.

## Passos

1. Abra o terminal.
2. Navegue até a pasta `API_Gabi` usando o comando `cd` (change directory). Por exemplo:
    ```bash
    cd caminho/para/API_Gabi
    ```
3. Certifique-se de que possui o ambiente virtual ativado, se necessário.

4. Execute as migrações do banco de dados:
    ```bash
    python manage.py migrate
    ```
6. Finalmente, inicie o servidor Django com o seguinte comando:
    ```bash
    python manage.py runserver
    ```
7. Agora você pode enviar os dados para a API em http://127.0.0.1:8000/meu_app/receber/.


8. Você pode visualizar os dados da API em http://127.0.0.1:8000/meu_app/exibir/.



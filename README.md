# SD
Sergio Alvarez 115735
Vinicius Kenzo 115672
Guilherme Ferrari 112679


Especificação:

Implemente um SD em uma linguagem de sua escolha, e que faça uso de uma das técnicas de passagem de mensagens estudadas na disciplina. O requisito a ser atendido, é que dadas duas ou mais máquinas do SD, se aquela que estiver atendendo requisições cair, a outra deve assumir o controle e o sistema continuar funcionando.

## Execução
- Necessário instalar Pyro4: ```pip install Pyro4```
- Executar Server1.py e Server2.py
- Executar Client.py
    - Inicialmente, Client vai tentar se conectar com Server1 por padrão.
    - Caso não dê certo, conexão vai para Server2.

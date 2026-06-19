# FluxoNorte

Sistema de apoio operacional em terminal desenvolvido em Python para controle de pedidos, entregadores, prioridades, pagamentos, reembolsos e relatorios em uma empresa de logistica urbana.

Projeto academico desenvolvido para a disciplina de Algoritmos de Programacao, Projetos e Computacao - APPC, adaptado para apresentacao em portfolio.

## Funcionalidades

- Cadastro de pedidos.
- Cadastro de entregadores.
- Validacao de ID do pedido.
- Validacao de ID do entregador.
- Validacao de prioridade do pedido.
- Validacao de veiculo do entregador.
- Busca de pedido por ID.
- Listagem de pedidos pendentes.
- Listagem de pedidos entregues.
- Listagem de entregadores disponiveis.
- Associacao de entregador a pedido.
- Remocao de associacao entre pedido e entregador.
- Atualizacao de status do pedido.
- Controle de pedidos ativos por entregador.
- Limite de pedidos baseado no veiculo.
- Listagem de pedidos pendentes por prioridade.
- Bloqueio de entrega para pedidos nao pagos.
- Geracao de reembolso para pedidos pagos e cancelados.
- Historico de entregas realizadas por entregador.
- Relatorio operacional com totais e indicadores.

## Tecnologias

- Python
- Git e GitHub

## Estrutura do projeto

```text
FluxoNorte/
|-- fluxonorte.py
|-- LICENSE
`-- README.md
```

## Como executar

### 1. Clone o repositorio

```bash
git clone https://github.com/yguioliveira/FluxoNorte.git
cd FluxoNorte
```

### 2. Execute o sistema

No Windows:

```bash
python fluxonorte.py
```

No Linux/macOS:

```bash
python3 fluxonorte.py
```

Tambem e possivel executar o arquivo pelo IDLE do Python.org ou pelo Visual Studio Code.

## Fluxo principal

O sistema inicia pelo arquivo `fluxonorte.py`.

O menu principal permite acessar:

- pedidos;
- entregadores;
- relatorios.

No menu de pedidos, e possivel cadastrar pedidos, atualizar status, buscar pedido por ID, listar pedidos pendentes e listar pedidos entregues.

No menu de entregadores, e possivel cadastrar entregadores, associar entregador a pedido, remover associacao, listar entregadores disponiveis e consultar entregas realizadas por entregador.

No menu de relatorios, o sistema apresenta indicadores operacionais, como total de pedidos, quantidade por status, pedidos de alta prioridade, pedidos pagos, reembolsos gerados e entregador com maior numero de entregas.

## Regras de negocio

### Prioridade dos pedidos

Pedidos com prioridade `Alta` sao listados antes dos pedidos de prioridade `Normal`.

Caso dois pedidos tenham a mesma prioridade, o sistema mantem a ordem de cadastro.

### Limite por veiculo

O limite de pedidos ativos depende do veiculo do entregador:

| Veiculo | Limite |
|---|---:|
| Moto | 2 pedidos ativos |
| Carro | 3 pedidos ativos |
| Van | 5 pedidos ativos |

Quando o entregador atinge o limite do veiculo, ele fica indisponivel para novos pedidos.

### Status dos pedidos

Os status utilizados sao:

- `Pendente`
- `Em Rota`
- `Entregue`
- `Cancelado`

Pedidos com status `Entregue` ou `Cancelado` sao considerados finalizados.

### Pagamento e reembolso

No cadastro do pedido, o sistema registra se o pedido ja foi pago.

Regras aplicadas:

- Pedido nao pago nao pode ser marcado como `Entregue`.
- Pedido pago e cancelado gera reembolso.
- Pedido nao pago e cancelado nao gera reembolso.
- Pedido cancelado nao pode ser reativado.

### Historico de entregas

Quando um pedido e marcado como `Entregue`, ele sai da lista de pedidos ativos do entregador e entra no historico de entregas realizadas.

Esse historico e utilizado para identificar o entregador com maior numero de entregas no relatorio.

## Estruturas utilizadas

O projeto utiliza estruturas nativas do Python:

- listas;
- dicionarios;
- funcoes;
- estruturas condicionais;
- estruturas de repeticao.

Principais estruturas:

- `pedidos`: lista com todos os pedidos cadastrados.
- `entregadores`: lista com todos os entregadores cadastrados.
- `pedido`: dicionario com os dados de um pedido.
- `entregador`: dicionario com os dados de um entregador.
- `pedidos_ativos`: lista interna de pedidos em andamento.
- `entregas_realizadas`: lista interna com o historico de entregas concluidas.
- `LIMITE_PEDIDOS_POR_VEICULO`: dicionario com o limite de pedidos por veiculo.

## Observacoes

- O sistema nao utiliza banco de dados.
- O sistema nao utiliza interface grafica.
- O sistema nao utiliza bibliotecas prontas de gerenciamento empresarial.
- Os dados ficam armazenados apenas em memoria durante a execucao.
- Ao encerrar o programa, os dados cadastrados sao perdidos.

## Licenca

Este projeto esta licenciado sob a licenca MIT.

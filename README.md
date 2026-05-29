# FluxoNorte - Operacao Turno Critico

Projeto desenvolvido para a Atividade Avaliativa A2 da disciplina Algoritmos de Programacao, Projetos e Computacao - APPC.

## Objetivo

O sistema FluxoNorte e um prototipo em Python para apoiar uma empresa de logistica urbana no controle de pedidos, entregadores e operacoes de entrega.

O sistema funciona em modo texto, por meio de menus, e armazena os dados em memoria usando estruturas nativas da linguagem Python.

## Como executar

Execute o arquivo principal:

```bash
python fluxonorte.py
```

Tambem e possivel abrir e executar o arquivo no IDLE do Python.org ou no Visual Studio Code.

## Arquivo principal

- `fluxonorte.py`: versao final completa do sistema.

## Evolucao do projeto

A pasta `evolucao_projeto` contem as versoes usadas para apresentar a evolucao do desenvolvimento:

- `etapa_01_menu.py`: estrutura inicial de menus.
- `etapa_02_pedidos.py`: etapa 1 + cadastro e consulta de pedidos.
- `etapa_03_entregadores.py`: etapas anteriores + cadastro e listagem de entregadores.
- `etapa_04_associacao_relatorios.py`: versao final completa, igual ao `fluxonorte.py`.
- `README_EVOLUCAO.md`: roteiro explicando o que apresentar em cada etapa.

## Funcionalidades principais

- Cadastro de pedidos.
- Cadastro de entregadores.
- Associacao de entregador a pedido.
- Remocao de associacao.
- Atualizacao de status do pedido.
- Consulta de pedidos pendentes.
- Consulta de pedidos entregues.
- Busca de pedido por ID.
- Consulta de entregadores disponiveis.
- Consulta de entregas realizadas por entregador.
- Relatorio operacional.

## Regras de negocio implementadas

### Prioridade dos pedidos

Os pedidos pendentes sao listados por prioridade. Pedidos com prioridade `Alta` aparecem antes dos pedidos `Normal`.

Quando dois pedidos possuem a mesma prioridade, o sistema mantem a ordem de cadastro.

### Limite de pedidos por veiculo

O limite de pedidos ativos depende do veiculo do entregador:

- Moto: ate 2 pedidos ativos.
- Carro: ate 3 pedidos ativos.
- Van: ate 5 pedidos ativos.

Quando o entregador atinge o limite, ele fica indisponivel para novos pedidos.

### Status dos pedidos

Os status utilizados sao:

- `Pendente`
- `Em Rota`
- `Entregue`
- `Cancelado`

Pedidos `Entregue` e `Cancelado` sao considerados finalizados.

### Pagamento e reembolso

No cadastro do pedido, o sistema pergunta se o pedido ja foi pago.

Se um pedido pago for cancelado, o sistema gera reembolso para o cliente.

Se um pedido nao pago for cancelado, nenhum reembolso e necessario.

Pedido nao pago nao pode ser marcado como `Entregue`.

### Historico de entregas

Quando um pedido e marcado como `Entregue`, ele sai da lista de pedidos ativos do entregador e entra na lista de entregas realizadas.

Esse historico e usado para identificar o entregador com maior numero de entregas.

## Estruturas utilizadas

O projeto utiliza:

- Listas para armazenar pedidos e entregadores.
- Dicionarios para representar cada pedido e cada entregador.
- Listas internas para pedidos ativos e entregas realizadas.
- Um dicionario para definir limites de pedidos por tipo de veiculo.

## Relatorio

Os arquivos de relatorio estao na raiz do projeto:

- `relatorio_fluxonorte_ajustado.pdf`
- `relatorio_fluxonorte_ajustado.docx`

O PDF ajustado e a versao recomendada para entrega, pois foi atualizado com as regras finais de pagamento, reembolso e decisoes de implementacao.

## Observacoes

- O projeto nao utiliza banco de dados.
- O projeto nao utiliza interface grafica.
- O projeto nao utiliza bibliotecas prontas de gerenciamento empresarial.
- Os dados ficam armazenados apenas em memoria enquanto o programa esta em execucao.

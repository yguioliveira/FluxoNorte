# FluxoNorte

Sistema de apoio operacional em terminal desenvolvido em Python para controle de pedidos, entregadores, prioridades, pagamentos, reembolsos e relatórios em uma empresa de logística urbana.

Projeto acadêmico desenvolvido para a disciplina de Algoritmos de Programação, Projetos e Computação - APPC, adaptado para apresentação em portfólio.

## Funcionalidades

- Cadastro de pedidos.
- Cadastro de entregadores.
- Validação de ID do pedido.
- Validação de ID do entregador.
- Validação de prioridade do pedido.
- Validação de veículo do entregador.
- Busca de pedido por ID.
- Listagem de pedidos pendentes.
- Listagem de pedidos entregues.
- Listagem de entregadores disponíveis.
- Associação de entregador a pedido.
- Remoção de associação entre pedido e entregador.
- Atualização de status do pedido.
- Controle de pedidos ativos por entregador.
- Limite de pedidos baseado no veículo.
- Listagem de pedidos pendentes por prioridade.
- Bloqueio de entrega para pedidos não pagos.
- Geração de reembolso para pedidos pagos e cancelados.
- Histórico de entregas realizadas por entregador.
- Relatório operacional com totais e indicadores.

## Tecnologias

- Python
- Git e GitHub

## Estrutura do projeto

```text
FluxoNorte/
|-- evolucao_projeto/
|   |-- etapa_01_menu.py
|   |-- etapa_02_pedidos.py
|   |-- etapa_03_entregadores.py
|   |-- etapa_04_associacao_relatorios.py
|   `-- README_EVOLUCAO.md
|-- fluxonorte.py
|-- relatorio_fluxonorte.docx
|-- LICENSE
`-- README.md
```

## Como executar

### 1. Clone o repositório

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

Também é possível executar o arquivo pelo IDLE do Python.org ou pelo Visual Studio Code.

## Fluxo principal

O sistema inicia pelo arquivo `fluxonorte.py`.

O menu principal permite acessar:

- pedidos;
- entregadores;
- relatórios.

No menu de pedidos, é possível cadastrar pedidos, atualizar status, buscar pedido por ID, listar pedidos pendentes e listar pedidos entregues.

No menu de entregadores, é possível cadastrar entregadores, associar entregador a pedido, remover associação, listar entregadores disponíveis e consultar entregas realizadas por entregador.

No menu de relatórios, o sistema apresenta indicadores operacionais, como total de pedidos, quantidade por status, pedidos de alta prioridade, pedidos pagos, reembolsos gerados e entregador com maior número de entregas.

## Regras de negócio

### Prioridade dos pedidos

Pedidos com prioridade `Alta` são listados antes dos pedidos de prioridade `Normal`.

Caso dois pedidos tenham a mesma prioridade, o sistema mantém a ordem de cadastro.

### Limite por veículo

O limite de pedidos ativos depende do veículo do entregador:

| Veículo | Limite |
|---|---:|
| Moto | 2 pedidos ativos |
| Carro | 3 pedidos ativos |
| Van | 5 pedidos ativos |

Quando o entregador atinge o limite do veículo, ele fica indisponível para novos pedidos.

### Status dos pedidos

Os status utilizados são:

- `Pendente`
- `Em Rota`
- `Entregue`
- `Cancelado`

Pedidos com status `Entregue` ou `Cancelado` são considerados finalizados.

### Pagamento e reembolso

No cadastro do pedido, o sistema registra se o pedido já foi pago.

Regras aplicadas:

- Pedido não pago não pode ser marcado como `Entregue`.
- Pedido pago e cancelado gera reembolso.
- Pedido não pago e cancelado não gera reembolso.
- Pedido cancelado não pode ser reativado.

### Histórico de entregas

Quando um pedido é marcado como `Entregue`, ele sai da lista de pedidos ativos do entregador e entra no histórico de entregas realizadas.

Esse histórico é utilizado para identificar o entregador com maior número de entregas no relatório.

## Estruturas utilizadas

O projeto utiliza estruturas nativas do Python:

- listas;
- dicionários;
- funções;
- estruturas condicionais;
- estruturas de repetição.

Principais estruturas:

- `pedidos`: lista com todos os pedidos cadastrados.
- `entregadores`: lista com todos os entregadores cadastrados.
- `pedido`: dicionário com os dados de um pedido.
- `entregador`: dicionário com os dados de um entregador.
- `pedidos_ativos`: lista interna de pedidos em andamento.
- `entregas_realizadas`: lista interna com o histórico de entregas concluídas.
- `LIMITE_PEDIDOS_POR_VEICULO`: dicionário com o limite de pedidos por veículo.

## Evolução do projeto

A pasta `evolucao_projeto` contém versões cumulativas usadas para demonstrar a evolução do desenvolvimento.

Etapas:

- `etapa_01_menu.py`: estrutura inicial de menus.
- `etapa_02_pedidos.py`: menu principal com cadastro e consulta de pedidos.
- `etapa_03_entregadores.py`: etapas anteriores com cadastro e listagem de entregadores.
- `etapa_04_associacao_relatorios.py`: versão final completa, igual ao `fluxonorte.py`.

## Relatório

O arquivo `relatorio_fluxonorte.docx` contém o relatório acadêmico do projeto, com introdução, desenvolvimento, estruturas utilizadas, decisões de implementação e referências bibliográficas.

## Observações

- O sistema não utiliza banco de dados.
- O sistema não utiliza interface gráfica.
- O sistema não utiliza bibliotecas prontas de gerenciamento empresarial.
- Os dados ficam armazenados apenas em memória durante a execução.
- Ao encerrar o programa, os dados cadastrados são perdidos.

## Licença

Este projeto está licenciado sob a licença MIT.

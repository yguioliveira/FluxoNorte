# 🚚 FluxoNorte

Sistema de gerenciamento logístico desenvolvido em Python com foco no controle de pedidos, entregadores e acompanhamento operacional das entregas.

O projeto simula o funcionamento de uma central logística, aplicando regras de negócio para distribuição de pedidos, controle de disponibilidade dos entregadores e geração de relatórios gerenciais.

---

## 🎯 Objetivo

Desenvolver uma solução capaz de auxiliar no gerenciamento do fluxo de entregas, permitindo o cadastro de pedidos e entregadores, a associação entre eles e o acompanhamento do ciclo completo das entregas.

---

## 🚀 Funcionalidades

### 📦 Gerenciamento de pedidos
- Cadastro de pedidos;
- Busca de pedidos por ID;
- Atualização de status;
- Consulta de pedidos pendentes;
- Consulta de pedidos entregues;
- Controle de pagamento dos pedidos;
- Processamento de reembolsos em casos de cancelamento.

### 🛵 Gerenciamento de entregadores
- Cadastro de entregadores;
- Associação de entregadores aos pedidos;
- Remoção de associações;
- Consulta de entregadores disponíveis;
- Histórico de entregas realizadas.

### ⚙️ Regras de negócio implementadas
- Validação dos IDs de pedidos e entregadores;
- Limite de pedidos ativos conforme o tipo de veículo:
  - 🏍️ Moto: até 2 pedidos;
  - 🚗 Carro: até 3 pedidos;
  - 🚐 Van: até 5 pedidos;
- Impedimento de associação de pedidos cancelados ou já entregues;
- Controle automático da disponibilidade dos entregadores;
- Bloqueio da finalização de pedidos sem pagamento;
- Geração automática de reembolso para pedidos pagos e posteriormente cancelados;
- Priorização de pedidos com prioridade alta.

### 📊 Relatórios
- Quantidade total de pedidos;
- Pedidos pendentes;
- Pedidos em rota;
- Pedidos entregues;
- Pedidos cancelados;
- Pedidos de alta prioridade;
- Total de pedidos pagos;
- Reembolsos gerados;
- Identificação do entregador com maior número de entregas.

---

## 🛠️ Tecnologias utilizadas

- Python 3
- Biblioteca padrão do Python (`os`)
- VS Code

---

## 🧠 Conceitos aplicados

Durante o desenvolvimento do projeto foram aplicados conceitos como:

- Estruturas de dados (listas e dicionários);
- Modularização por funções;
- Validação de entradas;
- Controle de fluxo;
- Regras de negócio;
- Simulação de processos logísticos;
- Geração de relatórios operacionais.

---

## ▶️ Como executar

1. Clone este repositório:

```bash
git clone https://github.com/yguioliveira/fluxonorte.git
```

2. Acesse a pasta do projeto:

```bash
cd fluxonorte
```

3. Execute o arquivo principal:

```bash
python fluxonorte.py
```

---

## 📷 Demonstração

Adicione aqui capturas de tela do sistema em execução.

Exemplos:
- Menu principal;
- Cadastro de pedidos;
- Associação de entregadores;
- Relatórios;
- Consulta de pedidos.

---

## 🎓 Contexto acadêmico

Projeto desenvolvido como atividade acadêmica do curso de Engenharia de Software da Pontifícia Universidade Católica de Campinas (PUC Campinas).

---

## 📚 Aprendizados

Este projeto contribuiu para o desenvolvimento de habilidades relacionadas à modelagem de regras de negócio, validação de dados, organização do código e construção de aplicações orientadas à resolução de problemas reais.

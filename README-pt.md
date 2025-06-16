# 🏥 Sistema de Triagem Hospitalar — Lista Encadeada

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📋 Descrição

Projeto acadêmico em Python que simula um sistema de triagem hospitalar com **lista encadeada simples**. Pacientes recebem cartões com cores (A - Amarelo, V - Verde) e são organizados em uma fila de atendimento conforme critérios de prioridade.

## 🚦 Regras da Fila

- Pacientes com cartão **amarelo (A)** têm prioridade sobre os com **verde (V)**.
- Entre os de mesma cor, o atendimento é feito pela ordem numérica.
- Números de cartões amarelos começam em 201, e os verdes em 1.

## 🧠 Funcionalidades

- Inserção de pacientes com ou sem prioridade
- Impressão da lista de espera
- Atendimento (remoção) do primeiro paciente
- Menu interativo com opções:
  - 1: Adicionar paciente
  - 2: Mostrar fila
  - 3: Atender paciente
  - 4: Sair

## 🛠️ Tecnologias

- Python 3
- Estrutura de dados: Lista Encadeada Simples (não circular)

## 📎 Licença

Este projeto está licenciado sob a [Licença MIT](https://opensource.org/licenses/MIT).

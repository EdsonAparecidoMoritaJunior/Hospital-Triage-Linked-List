# 🏥 Hospital Triage System — Linked List

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📋 Description

Academic project in Python that simulates a hospital triage system using a **singly linked list**. Patients receive cards with colors (A - Yellow, V - Green) and are organized in a queue based on priority rules.

## 🚦 Queue Rules

- Patients with **yellow (A)** cards are served before those with **green (V)** cards.
- Among the same color, patients are attended based on card number order.
- Yellow card numbers start at 201; green cards start at 1.

## 🧠 Features

- Insert patients (with and without priority)
- Print the waiting list
- Attend (remove) the first patient
- Interactive menu with options:
  - 1: Add patient
  - 2: Show queue
  - 3: Attend patient
  - 4: Exit

## 🛠️ Technologies

- Python 3
- Data Structure: Singly Linked List (non-circular)

## 📎 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

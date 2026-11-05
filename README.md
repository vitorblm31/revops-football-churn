# RevOps Football: Churn Prediction para Sócio-Torcedor

![Status](https://img.shields.io/badge/Status-Em_Desenvolvimento-brightgreen)
![Python](https://img.shields.io/badge/Python-3.14-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-00a393)
![License](https://img.shields.io/badge/License-MIT-purple)

## O Problema de Negócio
No ecossistema moderno do futebol, clubes operam como corporações complexas onde a previsibilidade de receita é fundamental. O programa de sócio-torcedor é uma das linhas de receita (MRR/ARR) mais importantes, mas sofre com altas taxas de cancelamento (*churn*) motivadas por resultados em campo, problemas logísticos ou falta de engajamento.

## A Solução (Visão RevOps)
Este projeto aplica os conceitos de **Revenue Operations (RevOps)** e **Data Science para Negócios** no futebol. O objetivo é antecipar o comportamento do fã através de um motor de inteligência preditiva. 

A aplicação fornece à diretoria e equipe de marketing um painel interativo em tempo real para identificar quais associados estão em risco de cancelamento, permitindo ações de retenção proativas (descontos, upgrades, experiências exclusivas) antes que a receita seja perdida.

## Stack Tecnológica
*   **Backend:** Python, FastAPI, Uvicorn
*   **Frontend:** HTML5, CSS3, JavaScript Vanilla (Design *Dark Mode* com UI/UX focada em dashboards executivos)
*   **Machine Learning (Roadmap):** PyTorch (Multi-Layer Perceptron)
*   **Banco de Dados (Roadmap):** SQLite / PostgreSQL

## Funcionalidades Atuais
- [x] **API RESTful:** Backend leve e rápido construído com FastAPI.
- [x] **Painel Interativo:** Tabela dinâmica alimentada assincronamente via `fetch` API.
- [x] **KPIs em Tempo Real:** Cálculo imediato de total analisado, risco crítico e risco médio global.
- [x] **Filtros Dinâmicos:** Busca instantânea por ID, plano ou fator crítico (Shapley

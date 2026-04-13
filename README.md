# 💊 MedTrack

> Controle de Medicamentos para Idosos — CLI simples e confiável

![CI](https://github.com/SamuelNHz/medtrack/actions/workflows/ci.yml/badge.svg)

---

## 🩺 Problema Real

Idosos frequentemente precisam tomar vários medicamentos ao longo do dia em horários específicos. Esquecer uma dose ou tomar o remédio em duplicidade pode causar sérios riscos à saúde. Cuidadores e familiares também têm dificuldade em monitorar se os medicamentos foram tomados.

## 💡 Proposta de Solução

O **MedTrack** é uma aplicação de linha de comando (CLI) que permite cadastrar medicamentos com nome, horário e dose, acompanhar quais já foram tomados no dia e resetar o controle a cada novo dia. É simples o suficiente para ser usado por cuidadores sem conhecimento técnico avançado.

## 👥 Público-Alvo

- Idosos com rotina de medicamentos
- Cuidadores e familiares de pacientes
- Profissionais de saúde domiciliar

## ✅ Funcionalidades Principais

| Comando | Descrição |
|---------|-----------|
| `adicionar` | Cadastra um medicamento com nome, horário e dose |
| `listar` | Exibe todos os medicamentos e seu status do dia |
| `tomar` | Marca um medicamento como tomado |
| `remover` | Remove um medicamento do controle |
| `resetar` | Reseta o status de todos para um novo dia |

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+** — linguagem principal
- **argparse** — interface CLI (stdlib)
- **json** — persistência de dados (stdlib)
- **pytest** — testes automatizados
- **ruff** — linting e análise estática
- **GitHub Actions** — integração contínua (CI)

## 📦 Instalação

```bash
# Clone o repositório
git clone https://github.com/SamuelNHz/medtrack.git
cd medtrack

# (Opcional) Crie um ambiente virtual
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt
```

## ▶️ Execução

```bash
# Adicionar um medicamento
python -m src.app adicionar --nome "Paracetamol" --horario "08:00" --dose "500mg"

# Listar medicamentos
python -m src.app listar

# Marcar medicamento ID 1 como tomado
python -m src.app tomar 1

# Remover medicamento ID 1
python -m src.app remover 1

# Resetar status para novo dia
python -m src.app resetar
```

## 🧪 Rodando os Testes

```bash
pytest --tb=short -v
```

## 🔍 Rodando o Lint

```bash
ruff check src/ tests/
```

## 🔖 Versão Atual

`1.0.0`

## 👤 Autor

Samuel Rodrigues Dos Santos — Matrícula: 22606496  
Disciplina: Bootcamp II — CEUB EaD 2026/1

## 🔗 Repositório

[https://github.com/SamuelNHz/medtrack](https://github.com/SamuelNHz/medtrack)

# info_parser

[![Python](https://img.shields.io/badge/python-3.10%2B-blue)]()
[![Status](https://img.shields.io/badge/status-in%20progress-yellow)]()
[![License](https://img.shields.io/badge/license-MIT-green)]()

---

## 🧠 О проекте

**info_parser** — это лёгкая Python-утилита для парсинга веб-страниц по списку URL-адресов.  
Её можно использовать как:

- основу для собственного парсера;
- шаблон для задач web-scraping;
- стартовую архитектуру для сбора данных с сайтов.

⚠️ В текущем состоянии проект представляет **базовую структуру и минимальную реализацию**.:contentReference[oaicite:1]{index=1}

---

## 📦 Структура проекта

```text
info_parser/
├── src/
│   └── parser.py        # Основная логика парсинга
├── output/              # Папка для результатов (создаётся автоматически)
├── .gitignore
├── requirements.txt
└── README.md

---

## 🛠 Установка

# Клонируем репозиторий
git clone https://github.com/Lumos2211/info_parser.git
cd info_parser

# Создаём виртуальное окружение
python3 -m venv venv

# Активируем виртуальное окружение
# Linux / macOS
source venv/bin/activate

# Windows (PowerShell)
venv\Scripts\Activate.ps1

# Устанавливаем зависимости
pip install -r requirements.txt

---
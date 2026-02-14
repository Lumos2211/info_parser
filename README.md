<div align="center">

# 🚀 info_parser

Лёгкий Python-парсер для сбора и обработки данных по списку URL.

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Status](https://img.shields.io/badge/status-in%20progress-yellow)
![License](https://img.shields.io/badge/license-MIT-green)

</div>

---

## 📖 О проекте

**info_parser** — это утилита на Python, предназначенная для автоматического обхода страниц и извлечения информации по заданным ссылкам.

Проект можно использовать как:
- основу для собственного парсера
- шаблон для web-scraping задач
- стартовую архитектуру для сбора данных

⚠️ На текущий момент репозиторий содержит базовую структуру и минимальную реализацию.

---

## 📂 Структура проекта

```text
info_parser/
├── main.py              # Точка входа
├── src/
│   └── parser.py        # Модуль с логикой парсинга
├── output/              # Папка для результатов (по желанию)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🛠 Установка

```bash
git clone https://github.com/Lumos2211/info_parser.git
cd info_parser

# создаём виртуальное окружение
python3 -m venv venv

# активируем
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows

# устанавливаем зависимости
pip install -r requirements.txt

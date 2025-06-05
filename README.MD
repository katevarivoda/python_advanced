# 🧪 Reqres Clone на FastAPI

Проект на FastAPI, реализующий базовый функционал REST API в стиле [reqres.in](https://reqres.in), с хранением данных в JSON-файле и автотестами.

📁 Репозиторий: [katevarivoda/python_advanced](https://github.com/katevarivoda/python_advanced)

---

## 🚀 Быстрый старт

### 1. Клонируй проект

```bash
git clone https://github.com/katevarivoda/python_advanced.git
cd python_advanced

### 2. Установи зависимости
python -m venv .venv
.\.venv\Scripts\activate  # для Windows
pip install -r requirements.txt

### 3. Запусти приложение
uvicorn app.main:app --reload

Приложение будет доступно на: http://localhost:8000
Документация: http://localhost:8000/docs


📚 Доступные эндпоинты
Метод	URL	Описание
GET	/api/users/{id}	Получение пользователя по ID

Пример:
GET http://localhost:8000/api/users/1
Ответ:
{
  "data": {
    "id": 1,
    "email": "janet.weaver@reqres.in",
    "first_name": "Janet",
    "last_name": "Weaver"
  }
}

### Используемые технологии
Python 3.11+
FastAPI
Uvicorn
Pytest
Requests

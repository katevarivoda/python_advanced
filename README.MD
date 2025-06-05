# 🧪 Reqres Clone на FastAPI

Проект на FastAPI, реализующий базовый функционал REST API в стиле [reqres.in](https://reqres.in), с хранением данных в JSON-файле и автотестами.

📁 Репозиторий: [katevarivoda/python_advanced](https://github.com/katevarivoda/python_advanced)

---

## 🚀 Быстрый старт

### 1. Клонируй проект

```bash
git clone https://github.com/katevarivoda/python_advanced.git
cd python_advanced
```

### 2. Установи зависимости

```bash
python -m venv .venv
.\.venv\Scriptsctivate  # для Windows
pip install -r requirements.txt
```

### 3. Запусти приложение

```bash
uvicorn app.main:app --reload
```

Приложение будет доступно по адресу:  
[http://localhost:8000](http://localhost:8000)

Документация Swagger:  
[http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📚 Доступные эндпоинты

| Метод | URL               | Описание                     |
|-------|-------------------|------------------------------|
| GET   | `/api/users/{id}` | Получение пользователя по ID |

### Пример запроса

```
GET http://localhost:8000/api/users/2
```

### Пример ответа

```json
{
  "data": {
    "id": 2,
    "email": "janet.weaver@reqres.in",
    "first_name": "Janet",
    "last_name": "Weaver"
  }
}
```

---

## 🧪 Автотесты

Пример: `tests/test_regress.py`

```python
import requests

def test_user_data():
    response = requests.get("http://localhost:8000/api/users/2")
    assert response.status_code == 200
    assert response.json()["data"]["id"] == 2
```

### Запуск всех тестов

```bash
pytest
```

---

## 💾 Источник данных

Пользователи хранятся в файле:

```
app/data/users.json
```

---

## 🧰 Используемые технологии

- Python 3.11+
- FastAPI
- Uvicorn
- Pytest
- Requests

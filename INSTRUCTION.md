# Краткая инструкция по выполнению

Все исходные файлы (ДО правок по заданию) уже разложены по структуре проекта.

## Структура архива
```
.
├── src/app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py          # Задание 1.3
│   ├── calculator.py      # "грязный" код для рефакторинга (Задание 2.2)
│   ├── logger.py          # Задание 3.1
│   └── client.py          # Задание 4.1
├── tests/
│   ├── test_calculator.py # Задание 3.2
│   └── test_client.py     # Задание 4.1
├── student_code/          # код для code review (Задание 1.1)
│   ├── variant1_data.py
│   └── variant2_api.py
├── .github/workflows/ci.yml  # Задание 4.3
├── Dockerfile             # Задание 4.2
├── .dockerignore
├── pyproject.toml         # настройки black/isort/mypy (Задание 2.1)
├── .flake8                # настройки flake8 (Задание 2.1)
├── .env                   # секреты (Задание 1.3)
├── .gitignore
└── requirements.txt
```

## Старт: окружение и Git
```bash
cd project
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
pip install black flake8 isort mypy pytest

git init
git add .
git commit -m "init: project scaffold"
```

## Занятие 1
- **1.1** Открой `student_code/variant1_data.py` и `variant2_api.py`, выпиши проблемы:
  - В1: хардкод пути, файл не закрывается, `global res`, итерация по индексам вместо векторизации pandas, нет типов/функция без аргументов результата.
  - В2: `while True` без выхода, голый `except: pass` (глушит все ошибки), нет таймаута, нет проверки `status_code`, бесконечный цикл без логирования.
- **1.2** Сравни два способа инициализации (venv+pip / poetry) — выполни команды из методички.
- **1.3** Структура и `config.py` уже готовы. Проверь, что `.env` в `.gitignore`.

## Занятие 2
- **2.1** Конфиги `pyproject.toml` и `.flake8` уже на месте.
- **2.2** Рефакторинг `calculator.py` ПО ПОРЯДКУ:
```bash
isort src/app/calculator.py
black src/app/calculator.py
flake8 src/app/calculator.py        # покажет неиспользуемые import math, sys, datetime — удали
```
  Далее вручную: переименуй `Calc_Func` → `calculate_value`, добавь аннотации
  `x: float, y: float, op: str -> float | None`, добавь docstring, прогони `mypy src/app/calculator.py`.
  ВАЖНО: чтобы прошли тесты 3.2, замени `if y==0: return None` на `raise ValueError("Division by zero")`.

## Занятие 3
- **3.1** `logger.py` готов. В `main.py` добавь `from app.logger import log` и вызовы
  `log.info/debug/error`. Запусти — в консоли только INFO/ERROR, в `app.log` все три.
- **3.2** Тесты готовы. Запуск (из корня проекта):
```bash
PYTHONPATH=src pytest -v tests/
```

## Занятие 4
- **4.1** `client.py` и `test_client.py` (с mock) готовы. Прогони `PYTHONPATH=src pytest -v tests/`.
- **4.2** Docker:
```bash
git checkout -b feature/docker-setup
git add Dockerfile .dockerignore
git commit -m "feat: add Dockerfile and dockerignore"
```
- **4.3** CI `.github/workflows/ci.yml` готов. Запушь на GitHub:
```bash
git checkout main
git add .github/ && git commit -m "ci: add github actions workflow"
git remote add origin <твой_repo_url>
git push -u origin main
```

## Запуск всех проверок локально (как в CI)
```bash
black --check src/ tests/
flake8 src/ tests/
PYTHONPATH=src pytest tests/
```

Примечание: тесты используют `from app...`, поэтому либо ставь `PYTHONPATH=src`,
либо настрой `pyproject.toml`/`pytest.ini` с `pythonpath = ["src"]`.

# Тестовое задание для вакансии Backend-Developer Python (junior) в Тетрика


## Стек технологий

- Python 3.10.10  
- Scrapy 2.13.0  
- pytest 8.1.1 

## Структура проекта

- `task1/` — решение первой задачи  
- `task2/` — решение второй задачи (Scrapy-паук для сбора данных)  
- `task3/` — решение третьей задачи  

## Установка и запуск

### Клонирование репозитория

```bash
git clone git@github.com:Dxndigiden/tetrika_test.git
cd tetrika_test
```
### Создание и активация виртуального окружения

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
```

### Установка зависимостей

```bash
pip install -r requirements.txt
```

## Запуск тестов

Из корня проекта запустите:

```bash
pytest
```

## Запуск Scrapy паука (задача task2)

1. Перейдите в папку с пауком:

```bash
 cd task2/solution/wik_animals/wik_animals/
 ```

 2. Запустите паука командой:

 ```bash
 scrapy crawl animals
  ```

  3. По завершении работы паука появится файл beasts.csv 
  с результатами подсчёта животных по первой букве.
  
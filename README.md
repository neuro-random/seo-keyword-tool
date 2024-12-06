# SEO Keyword Analyzer 🔍

Простой и удобный инструмент для анализа частоты ключевых слов на веб-страницах или в HTML-файлах. Подходит для специалистов по SEO, владельцев сайтов и маркетологов, которые хотят оптимизировать свои ресурсы.

## ✨ Возможности

- **Анализ частоты ключевых слов**: Подсчёт, сколько раз ключевые слова встречаются на странице
- **Работа с веб-страницами и локальными файлами**: Анализируйте контент из интернета или HTML-файлы на вашем компьютере
- **Гибкость**: Простое использование через командную строку

## 🚀 Установка

### Шаг 1: Установка Python

1. Убедитесь, что на вашем компьютере установлен Python версии 3.7 или выше:
```bash
python --version
```

2. Если у вас нет Python:
   - Скачайте с [официального сайта Python](https://python.org)
   - При установке выберите опцию `Add Python to PATH`

### Шаг 2: Установка Git

1. Установите Git с [официального сайта](https://git-scm.com)
2. Проверьте установку:
```bash
git --version
```

### Шаг 3: Клонирование репозитория

```bash
git clone https://github.com/neuro-random/seo-keyword-tool.git
```

### Шаг 4: Установка зависимостей

```bash
cd seo-keyword-tool
pip install -r requirements.txt
```

#### Необходимые библиотеки:
- `beautifulsoup4`: Парсинг HTML-страниц
- `requests`: Выполнение HTTP-запросов

## 💻 Использование

### Базовый анализ URL:
```bash
python main.py <URL> <ключевое_слово1> <ключевое_слово2> ...
```

### Пример:
```bash
python main.py https://example.com "seo" "keyword" "analysis"
```

### Анализ локального файла:
```bash
python main.py файл.html "seo" "keyword" "analysis"
```

## 📝 Примечания

- Убедитесь, что все зависимости установлены корректно
- Для внесения изменений создавайте новую ветку

## 🛠️ Требования

- Python 3.7+
- Git
- Доступ к интернету для анализа веб-страниц

## 📌 TODO

- [ ] Добавить поддержку многоязычного анализа
- [ ] Реализовать экспорт в CSV/Excel
- [ ] Добавить визуализацию результатов

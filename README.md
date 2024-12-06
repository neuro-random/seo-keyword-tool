# SEO Keyword Analyzer

Простой и удобный инструмент для анализа частоты ключевых слов на веб-страницах или в HTML-файлах. Подходит для специалистов по SEO, владельцев сайтов и маркетологов, которые хотят оптимизировать свои ресурсы.

## Возможности

- **Анализ частоты ключевых слов**: Подсчёт, сколько раз ключевые слова встречаются на странице.
- **Работа с веб-страницами и локальными файлами**: Анализируйте контент из интернета или HTML-файлы на вашем компьютере.
- **Гибкость**: Простое использование через командную строку.

## Установка

### Шаг 1: Установка Python

1. Убедитесь, что на вашем компьютере установлен Python версии 3.7 или выше. Для этого откройте командную строку (терминал) и выполните команду:
   ```bash
   python --version
Если у вас нет Python, скачайте его с официального сайта: python.org и установите.

При установке Python не забудьте выбрать опцию Add Python to PATH. Это важно для корректной работы Python в командной строке.
Шаг 2: Установка Git
Если у вас еще не установлен Git, скачайте и установите его с официального сайта: git-scm.com.
После установки откройте командную строку и выполните команду:
bash
Копировать код
git --version
Чтобы проверить, что Git установлен корректно.
Шаг 3: Клонирование репозитория
Теперь, когда у вас установлен Python и Git, клонируйте репозиторий с инструментом на свой компьютер. Для этого выполните команду в командной строке:

bash
Копировать код
git clone https://github.com/neuro-random/seo-keyword-tool.git
Эта команда создаст копию репозитория на вашем компьютере.

Шаг 4: Установка зависимостей
Перейдите в папку с проектом, используя команду:

bash
Копировать код
cd seo-keyword-tool
Затем установите все необходимые зависимости, указанные в файле requirements.txt, с помощью команды:

bash
Копировать код
pip install -r requirements.txt
В requirements.txt указаны следующие библиотеки:

beautifulsoup4: Библиотека для парсинга HTML-страниц.
requests: Библиотека для выполнения HTTP-запросов.
Эти библиотеки необходимы для правильной работы инструмента.

Шаг 5: Запуск инструмента
Теперь вы готовы использовать инструмент! Для анализа страницы выполните следующую команду в терминале:

bash
Копировать код
python main.py <URL> <ключевое_слово1> <ключевое_слово2> ...
Пример:

bash
Копировать код
python main.py https://example.com "seo" "keyword" "analysis"
Этот скрипт проанализирует страницу по указанному URL и подсчитает, сколько раз встречаются ключевые слова на странице.

Дополнительные опции
Вы можете анализировать не только страницы по URL, но и локальные HTML-файлы. Для этого укажите путь к файлу вместо URL:

bash
Копировать код
python main.py файл.html "seo" "keyword" "analysis"
Примечания
Если у вас возникнут проблемы с установкой или запуском, убедитесь, что у вас установлены все необходимые зависимости и правильно настроен Python.
Если вы хотите внести изменения в проект, не забудьте создать новую ветку перед изменениями.

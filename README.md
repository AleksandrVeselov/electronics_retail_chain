# Торговая сеть электроники

В данном задании предлагается разработать онлайн платформу торговой сети электроники.

Сеть должна представлять собой иерархическую структуру из 3 уровней:

- Завод;
- Розничная сеть;
- Индивидуальный предприниматель.
  
Структура проекта:

Приложение retail_chain (торговая сеть):
- Сеть (Link)
- Контакты (Contacts)
- Продукты (Products)
Приложение сотрудники (Employee)
- Сотрудник (Employee)

Доступ к созданию, удалению, редактированию меоделей, а так же созданию, удалению и редактированию сотрудников имеется только через админ-панель.

После создания сотрудника и авторизации он получает доступ к веб и API интерфейсам:
Веб интерфейс (http://127.0.0.1:8000/):
- Просмотр списка всех звеньев торговой сети с возможностью обнулить задолженность любого звена сети перед поставщиком
- Возможность отфильтровать звенья сети по названию города

API:
- http://127.0.0.1:8000/api/token/ - jwt авторизация. Получение токена
- http://127.0.0.1:8000/api/links - просмотр списка всех звеньев сети
- http://127.0.0.1:8000/api/links/create - создание звена сети
- http://127.0.0.1:8000/api/links/<int:pk> - детальная информация о звене сети
- http://127.0.0.1:8000/api/links/delete/<int:pk> - удаление звена сети
- http://127.0.0.1:8000/api/links/update/<int:pk> - изменение данных звена сети, без возможности изменить задолженность перед поставщиком
- http://127.0.0.1:8000/api/contacts/create - создание контактов
- http://127.0.0.1:8000/api/product/create - создание продукта

Инструкция по запуску проекта:
- Скачать исходный код проекта на локальный компьютер (можно средствами git, или просто zip архив)
- Скачать и установить на компьютер docker-desktop по ссылке - https://www.docker.com/products/docker-desktop/
- Создать .env файл на основании .env.sample в папке с проектом
- Запустить docker-desktop через ярлык на рабочем столе
- Открыть консоль и перейти в папку с проектом. Или открыть папку с проектом, нажать правой клавишей на пустое место и выбрать пункт "Открыть в терминале"
- В терминале ввести команду docker-compose up --build -d и дождаться когда проект запуститься
- Попробовать открыть в браузере главную страницу http://127.0.0.1:8000/
- создать суперпользователя, введя в консоли контейнера с приложением команду python manage.py create_su (это создаст пользователя с именем admin и паролем admin для доступа к веб интерфейсу приложения и админ-панели)

Технологии, используемые в проекте - django, djangorestframework, djangorestframework-simplejwt, PostgreSQL, Docker.
Автор - Веселов Александр Сергеевич

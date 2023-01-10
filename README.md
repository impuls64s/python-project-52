### Hexlet tests and linter status:
[![Actions Status](https://github.com/impuls64s/python-project-52/workflows/hexlet-check/badge.svg)](https://github.com/impuls64s/python-project-52/actions)
<a href="https://codeclimate.com/github/impuls64s/python-project-52/maintainability"><img src="https://api.codeclimate.com/v1/badges/01f0a08fb09494b1ba7f/maintainability" /></a>
<a href="https://codeclimate.com/github/impuls64s/python-project-52/test_coverage"><img src="https://api.codeclimate.com/v1/badges/01f0a08fb09494b1ba7f/test_coverage" /></a>
[![CI](https://github.com/impuls64s/python-project-52/actions/workflows/CI.yml/badge.svg)](https://github.com/impuls64s/python-project-52/actions/workflows/CI.yml)

<h3>Менеджер задач</h3>
https://python-project-52-production-37c4.up.railway.app/
<p>Простое веб-приложения для управления задачами в компании или команде.
Реализовано на фреймворке <b>Django 4.1.4</b> используя встроенные представления на основе классов (CBV) и базу данных <b>PostgreSql</b>. Дизайн сайта - <a href='https://getbootstrap.com/docs/5.0/getting-started/introduction/'>Bootstrap v5.0</a></p>
<ul>
  <li>Регистрация и аутентификация пользователей.</li>
  <li>CRUD : пользователей, статусов, меток, задач.</li>
  <li>Доступ к статусам, меткам и задачам имеют только авторизированные пользователи.</li>
  <li>Пока задаче присвоен статус или метка, ее нельзя удалить.</li>
  <li>Присутсвует фильтрация задач.</li>
  <li>Локализация RU/EN. По умолачанию RU. Переведено с EN. Папка с переводами locale/ru/</li>
  <li>Подключен <a href='https://rollbar.com'>Rollbar</a> (сервис для отслеживания и сбора ошибок)</li>
  <li>Покрытие тестами</li>
</ul>
<h3>Переменные окружения</h3>
<p>Необходимо в корне проекта созлать файл .env и записать в переменные свои значения.</p>
<pre>
SECRET_KEY =
DATABASE_URL = postgres://USER:PASSWORD@HOST:PORT/NAME
ROLLBAR_TOKEN = 
</pre>
<h3>Установка</h3>
<pre>
$ git clone https://github.com/impuls64s/python-project-52.git
$ cd python-project-52.git
$ make setup
# Сайт станет доступен по адресу http://127.0.0.1:8000/ и http://0.0.0.0:8000/ 
</pre>

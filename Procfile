# File for Heroku server with the app and cron/s
web: gunicorn home_project.wsgi --log-file -
cron-weather: python utils/cron_dataweather.py

# File for Heroku server with the app and cron/s
web: gunicorn PROJECT_FOLDER.wsgi --log-file -
cron-covid19: python cron/cron_covid19.py
cron-graphs: python cron/cron_graphs.py

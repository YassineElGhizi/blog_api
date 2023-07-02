#!/bin/bash

file_content=$(cat salim.txt)

if [[ "$file_content" == "0" ]]; then
    echo "1" > /var/www/html/django/django_adnanE/salim.txt
    source /var/www/html/django/django_adnanE/venv/bin/activate
    /var/www/html/django/django_adnanE/manage.py motarjim
    /var/www/html/django/django_adnanE/manage.py copy_right
    /var/www/html/django/django_adnanE/manage.py splitter
    echo "0" > /var/www/html/django/django_adnanE/salim.txt
else
    echo "Skipping commands. Content of salim.txt is not '0'."
fi

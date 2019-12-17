from pprint import pprint

from django.shortcuts import render
import csv

from app import settings



def inflation_view(request):
    template_name = 'inflation.html'

    # чтение csv-файла и заполнение контекста

    with open(settings.INFLATION_CSV, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';',)
        a = list((dict(rows) for rows in reader))
        context = {'headers': a[0].keys(), 'rows': []}
        for row in a:
            context['rows'].append(list(row.values()))
    pprint(context)

    return render(request, template_name,
                  context)

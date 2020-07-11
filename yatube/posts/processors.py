import datetime as dt


def year(request):
    """
    Добавляет переменную с текущим годом.
    """
    td = dt.datetime.today().year
    return {
        'year': td
    }
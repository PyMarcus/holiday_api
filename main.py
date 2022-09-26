import logging
from datetime import date
from flask import Flask, request
from platform import system
import holidays


app = Flask(__name__)


def path():
    """
    Retorna o caminho de log, correspondente
    ao sistema operacional
    :return:
    """
    if system() == "Windows":
        return "."
    return "/home/ubuntu/logs/"


#logging.basicConfig(filename=path(), encoding='utf-8', level=logging.DEBUG)


def log_creator(text):
    """
    Cria arquivo log
    :return:
    """
    logging.info(text)


@app.route('/', methods=["GET"])
def holiday():
    """
    Quando solicitado, retorna o dia e o mes
    dos feriados do ano atual
    :return: dict
    """
    brazil_holidays = holidays.Brazil(years=date.today().year)
    log_creator(request)
    days = []
    for holiday, name in brazil_holidays.items():
        days.append(str(holiday) + "T" + "03:06:28.000Z")
    log_creator(days)
    return days


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')

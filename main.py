import logging
from datetime import date
import fastapi
import uvicorn
from fastapi import FastAPI
from platform import system
import holidays


app = FastAPI()


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


@app.get('/')
def holiday():
    """
    Quando solicitado, retorna o dia e o mes
    dos feriados do ano atual
    :return: dict
    """
    brazil_holidays = holidays.Brazil(years=date.today().year)
    #log_creator(fastapi.Response())
    days = []
    for holiday, name in brazil_holidays.items():
        days.append(str(holiday) + "T" + "03:06:28.000Z")
    #log_creator(days)
    return days


if __name__ == '__main__':
    uvicorn.run(port=33333, host="127.0.0.1", debug=False)

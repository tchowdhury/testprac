import datetime
from datetime import date
from datetime import timedelta
from dateutil.relativedelta import relativedelta
from config import *


def getsesson(dt):

    mnth = dt.month
    match mnth:
        case 12|1|2:
            return 'Summer'
        case 3|4|5:
            return 'Autmn'
        case 6|7|8:
            return 'Winter'
        case _:
            return 'Spring'

def getloggingrate(sensor_model, battery_type, reading_date):

    session = getsesson(reading_date)
    match sensor_model:
        case "RXW-GP3-922":
            match battery_type:
                case "Chargable":
                    return 5
                case _:
                    return 10
        case "RXW-GP4-922" | "RXW-GP6-922":
            match battery_type:
                case"Chargable":
                    match session:
                        case "Summer" | "Autmn":
                            return 5
                        case _:
                            return 10
                case _:
                    return 15

def generate_date_range(startdate, enddate, delta):


    while startdate < enddate:
        print(startdate)
        logging_rate = getloggingrate(MODEL,BATTERY_TYPE,startdate)
        logging_start = LOGGING_START_TIME
        logging_end = LOGGING_END_TIME
        while logging_start <= logging_end:
            print(logging_start)
            logging_start += logging_rate
        startdate += delta



if __name__ == '__main__':
    # Set start date
    enddate = date.today()
    startdate = enddate - relativedelta(months=BACK_FILL_MONTH)
    delta = timedelta(days=1)

    generate_date_range(startdate, enddate, delta)

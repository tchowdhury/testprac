from datetime import datetime
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
        logging_start = LOGGING_START_TIME
        logging_end = LOGGING_END_TIME
        logging_rate = getloggingrate(MODEL, BATTERY_TYPE, startdate)
        newstartdate = datetime(startdate.year,startdate.month,startdate.day,0,0,0)
        #print(f"dt= {startdate}, logging start :{logging_start}, logging_end:{logging_end}, logging_rate={logging_rate}")

        while logging_start < logging_end:
            logging_min = 0
            while logging_min < 60:
                reading_date = newstartdate + timedelta(hours=logging_start, minutes=logging_min, seconds=0)
                logging_min += logging_rate
                print(reading_date.isoformat())
            logging_start += 1



        startdate += delta




if __name__ == '__main__':
    # Set start date
    enddate = date.today()
    startdate = enddate - relativedelta(months=BACK_FILL_MONTH)
    delta = timedelta(days=1)

    generate_date_range(startdate, enddate, delta)

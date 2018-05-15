rom datetime import date
import holidays
from flask import jsonify
from flask_restful import Resource
from auth import auth
from flask_cors import cross_origin

class RestrictedHolidays(Resource) :
    @auth
    @cross_origin
    def get(self) :

        custom_holidays = holidays.HolidayBase()
        #a dict with date/name key/value pairs,
        custom_holidays.append({"2018-03-29" : "Mahavir Jayanti"})
        custom_holidays.append({"2018-04-30" : "Buddha Purnima" })
        custom_holidays.append({"2018-08-22" : "Id-Ul-Zuha(Bakrid)"})
        custom_holidays.append({"2018-09-03" : "Janamashtami" })
        custom_holidays.append({"2018-11-09" : "Bhai Duj"})
        custom_holidays.append({"2018-11-21" : "Mohammad Prophet's Birthday"})
        
        print(custom_holidays)

        return jsonify({'success' : True,'custom_holidays':custom_holidays})



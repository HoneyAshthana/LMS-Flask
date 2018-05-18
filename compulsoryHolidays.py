from datetime import date
import holidays
from flask import jsonify
from flask_restful import Resource
from flask_cors import cross_origin
from auth import auth
from connect_mongo import lms
class CompulsoryHolidays(Resource) :
    #@auth
    #@cross_origin 
    def get(self):

        custom_holidays = holidays.HolidayBase()
        #a dict with date/name key/value pairs,
        custom_holidays.append({"2018-01-26": "Republic Day"})
        custom_holidays.append({"2018-03-02" : "Holi"})
        custom_holidays.append({"2018-03-30" : "Good Friday" })
        custom_holidays.append({"2018-08-15" : "Independence Day"})
        custom_holidays.append({"2018-09-21" : "Muharram" })
        custom_holidays.append({"2018-10-02" : "Mahatma Gandhi's Birthday"})
        custom_holidays.append({"2018-10-19" : "Dussehra(Maha Navami"})
        custom_holidays.append({"2018-11-07" : "Diwali"})
        custom_holidays.append({"2018-11-23" : "Guru Nanak's Birthday"})
        custom_holidays.append({"2018-12-25" : "Christmas"})
        lms.holidays.insert(custom_holidays)
        print(custom_holidays)

        return jsonify({'success' : True,'custom_holidays':custom_holidays})



#a list of dates (in any format: date, datetime, string, integer),
#custom_holidays.append(['2015-07-01', '07/04/2015'])
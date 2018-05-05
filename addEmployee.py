from flask import Flask,jsonify,request
from flask import request,jsonify
from flask_restful import Resource,Api
from connect_mongo import lms
import uuid

class AddEmployees(Resource) :
    def post(self) :
        """Add new employees"""
        try :
            data = request.get_json(force=True)
            qci_id = data['qci_id']
            name = data['name']
            email = data['email']
            board = data['dept']
            designation = data['designation']
            type_of_employee = data['type_of_employee']
            gender = data['gender']
            #total_cl = int(data['total_cl'])
            #total_sl = int(data['total_sl'])
            #total_rh = int(data['total_rh'])
            password = data['password']    
        
            return jsonify({'success':False, 'error':qci_id})
        except Exception as e:
            return jsonify({'success':False, 'error':e.__str__()})
        
        try:
            qci_id_exist = lms.employees.find_one({'qci_id':qci_id})
            if qci_id_exist:
                return jsonify({'success':True,'message':'QCI ID already exists!'})
            else:
                new_qci_id = uuid.uuid4().hex
                new_emp = {
                    'qci_id' : new_qci_id,
                    'name' : name,
                    'email' : email,
                    'designation' : designation,
                    'board' : board,
                    'gender' : gender,
                    'type_of_employee' : type_of_employee,
                    #'total_cl' : total_cl,
                    #'total_rh' : total_rh,
                    #'total_sl' : total_sl,
                    'password' : password
                }

                empCount = total_emp(employees)
                print (empCount)
                lms.employees.insert_one(new_emp)
                return jsonify({"success":True,"message":"Item details inserted"})
        except Exception as e:
            print (e.__str)
            return jsonify({"succees":False,"error":e.__str__()})

    """Total no. of employees"""
    def total_emp(employees):
        count = 0     
        for emp in employees:
            return count
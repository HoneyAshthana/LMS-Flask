from flask import jsonify,request
from flask_restful import Resource
from connect_mongo import lms
from flask_cors import cross_origin
from auth import auth
import hashlib
"""from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(None)"""
class EditEmployeeDetails(Resource) :
    
    @auth
    @cross_origin()
    def post(self) :
        """Edit employee detail
        Args:
            qci_id : QCI ID of new enrolled employee
            name : name of employee
            email : new email Id of employee
            board : new Board of employee working in
            designation :new Designation of employee
            type_of_employee : Type of employee, whether regular,professional or contract
            gender : Gender of employee
            bal_cl : Balance casual leave of employee
            bal_sl : Balance sick leave of employee
            bal_pl : Balance privilege leave of mployee
            bal_ml : Balance maternity leave only for female employee
            bal_ptl : Balance paternity leave only for male employee
            bal_eol : Balance extra ordinary leave for employee
            password : new Password of employee
        """
        try :
            data = request.get_json(force=True)
            print(data)
            qci_id = data['qci_id']
            name = data['name']
            email = data['email']
            board = data['board']
            designation = data['designation']
            type_of_employee = data['type_of_employee']
            gender = data['gender']
            bal_cl = int(data['bal_cl'])
            bal_sl = int(data['bal_sl'])
            bal_pl = int(data['bal_pl'])
            if gender == 'Male':
                bal_ptl = int(data['bal_ptl'])
                bal_ml = 0
            else:
                bal_ml = int(data['bal_ml'])
                bal_ptl = 0
            bal_eol = int(data['bal_eol'])
            password = data['password']        
        
        except Exception as e:
            return jsonify({'success':False, 'error':e.__str__()})
        
        try:
            qci_id_exist = lms.employees.find_one({'qci_id':qci_id})
            if qci_id_exist :
                password = hashlib.sha256(password.encode("utf-8")).hexdigest()
                #password = bcrypt.generate_password_hash(password)

                lms.employees.update(
                    {'qci_id' : qci_id},
                    {
                        '$set':{
                            'name' : name,
                            'email' : email,
                            'designation' : designation,
                            'board' : board,
                            'gender' : gender,
                            'type_of_employee' : type_of_employee,
                            'bal_cl': bal_cl,
                            'bal_sl' : bal_sl,
                            'bal_pl' : bal_pl,
                            'bal_ml' : bal_ml,
                            'bal_ptl' : bal_ptl,
                            'bal_eol' : bal_eol,  
                            'password' : password
                        }
                    }
                )   
                return jsonify({'success':True,'message':'Employee details successfully updated'})
            else:
                return jsonify({"success":False,"message":"Employee Id does not exist.Create new Id!"})
        except Exception as e:
            return jsonify({"succees":False,"error":e.__str__()}) 

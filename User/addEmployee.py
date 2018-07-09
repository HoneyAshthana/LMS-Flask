from flask import jsonify,request
from flask_restful import Resource
from connect_mongo import lms
from flask_cors import cross_origin
from auth import auth
import hashlib
"""from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(None)"""


class AddEmployee(Resource) :
    @auth
    @cross_origin()
    def post(self) :
        """Add new employee
        Args:
            qci_id : QCI ID of new enrolled employee
            name : name of employee
            email : Email Id of employee
            board : Board of employee working in
            designation : Designation of employee
            type_of_employee : Type of employee, whether regular,professional or contract
            gender : Gender of employee
            bal_cl : Balance casual leave of employee
            bal_sl :Balance sick leave of employee
            bal_pl : Balance privilege leave of mployee
            bal_ml : Balance maternity leave only for female employee
            bal_ptl : Balance paternity leave only for male employee
            bal_eol : Balance extra ordinary leave for employee
            password : Password of employee
        """
        try :
            data = request.get_json(force=True)
            #print(data)
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
        
        except Exception as e :
            return jsonify({'success' : False, 'error' : e.__str__()})
        
        try:
            #indexing on collection employees
            lms.employees.create_index("name",unique=True)

            qci_id_exist = lms.employees.find_one({'qci_id' : qci_id})
            if qci_id_exist :
                return jsonify({'success' : True, 'message' : 'QCI ID already exists!'})
            else:
                password = hashlib.sha256(password.encode("utf-8")).hexdigest()
                #password = bcrypt.generate_password_hash(password)
                new_emp = {
                        'qci_id' : qci_id,
                        'name' : name,
                        'email' : email,
                        'board' : board,   
                        'designation' : designation,
                        'type_of_employee' : type_of_employee,
                        'gender' : gender,
                        'bal_cl': bal_cl,
                        'bal_sl' : bal_sl,
                        'bal_pl' : bal_pl,
                        'bal_ml' : bal_ml,
                        'bal_ptl' : bal_ptl,
                        'bal_eol' : bal_eol,     
                        'password' : password
                        }                                      
                lms.employees.insert_one(new_emp)
                return jsonify({"success" : True, "message" : "New Employee added successfully"})

        except Exception as e :
            return jsonify({"success" : False, "error" : e.__str__()}) 
            

    @auth
    @cross_origin()
    def get(self, id=None) :
        """Displays employees details of particular qci id
        Args:
            QCI ID
        """
        try:
            data = lms.employees.find_one({"qci_id":id},{"_id":0})
            if data :  
                return jsonify({"success" : True,'data' : data})                
            else:
                return jsonify({"success" : False, "messages" : "no data found"})

        except Exception as e :
            return jsonify({'success' : False, 'error' : e.__str__()})


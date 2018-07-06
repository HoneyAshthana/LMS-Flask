










"""import requests
import json
import uuid
from faker import Faker
f= Faker()
app_port = 5000
server = "http://192.168.15.55:" + str(app_port)
def addAdmin(name,email,password):
    data = {
        "name":name,
        "email":email,
        "password" : password,
        }

    r = requests.post(server+  "/lms/addAdmin",data = data)
    if r.json()["success"]:
        print (email , " user created\n")
        return r.json()["user_id"]
    else:
        print(r.json()["message"])
        if "error" in r.json():
            print(r.json()["error"])
    return None
def loginAdmin(email,password):
    data = {
        "email" : email,
        "pwd" : password
        }
    r = requests.post(server+  "/lms/login/",data = data)
    if r.json()["success"]:
        print (email , " Logged in succesfully\n")
        return r.json()
    else:
        print(r.json()["message"])
        if "error" in r.json():
            print(r.json()["error"])
    return None
def loginEmployee(qci_id,password):
    data = {
        "qci_id" : qci_id,
        "password" : password
    }
    r = requests.post(server+ "/lms/loginEmp",data=data)
    if r.json()["success"]:
        print(qci_id,"Logged in successfully\n")
        return r.json()
    else :
        print(r.json()["message"])
        if "error" in r.json() :
            print(r.json()["error"])
        return None

def addEmployee(name,email,board, type_of_employee,gender,bal_cl ,bal_sl ,bal_pl ,bal_ml, bal_ptl,bal_eol,password,designation,qci_id):
    data = {
        "qci_id" : qci_id,
        "email":email,
        "name":name,   
        "board":board,        
        "designation":designation,
        "type_of_employee": type_of_employee,
        "gender":gender,
        "bal_cl":bal_cl,
        "bal_sl":bal_sl,
        "bal_pl":bal_pl,
        "bal_ml":bal_ml,
        "bal_ptl":bal_ptl,
        "bal_eol":bal_eol,   
        "password":password
        }

    r = requests.post(server+  "/lms/addEmployee",data = data)
    if r.json()["success"]:
        print (email , " admin created\n")
        return r.json()["user_id"]
    else:
        print(r.json()["message"])
        if "error" in r.json():
            print(r.json()["error"])
    return None

    def empOnLeave(date):
        data = {
            "date" : date
        }
        r = requests.post(server+  "/lms/empOnLeave",data = data)
        if r.json()["success"]:
            print (date , " employee on leave\n")
            return r.json()["date"]
        else:
            print(r.json()["message"])
            if "error" in r.json():
                print(r.json()["error"])
        return None

    def 

       










    def test_addAdmin(admin_name,data):
        temp = addAdmin("BUgs","honey.ashthana1@gmail.com","1")
        print (temp)
        if temp:
            data[admin_name] = temp
            # save(data)
            print (data)
    def test_addEmployee(qci_id,data):
        temp = addEmployee("123qci","honey.ashthana1@gmail.com","anaa","QCI","general","Male",12,12,12,12,12,12,"1")
        print (temp)
        if temp :
            data[qci_id] = temp
            print(data)

    def test_loginAdmin(email,data):
        temp = loginAdmin("honey.ashthana1@gmail.com","1")
        print (temp)
        if temp :
            data[email] = temp
            print(data)
    def test_loginEmp(qci_id,data):
        temp = loginEmp("123qci","1")
        print (temp)
        if temp :
            data[qci_id] = temp
            print(temp)
    test_addAdmin()
"""


"""
import requests
import json
import uuid
from faker import Faker
f = Faker()

import time
from datetime import datetime

import time
from datetime import datetime
from pytz import timezone
TIME_ZONE =  'Asia/Kolkata'

def itime():
    india  = timezone(TIME_ZONE)
    now = datetime.now(india)
    tt = datetime.timetuple(now)
    n_time = time.mktime(tt)
    return n_time

def nicetime(ep,pattern=None):
    if not pattern:
        # pattern = "%H:%M %d/%m/%Y"
        pattern = "%b %-d, %Y %-I:%M %p"
    return time.strftime(pattern,time.localtime(ep))

app_port = 8000
# server = "http://localhost:" + str(app_port)

# server = "https://qcitech.org:8083"
server = "https://api-collect.qcitech.org" 

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    DEFAULT = '\033[0;37m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m' #yellow
    FAIL = '\033[91m' #red
    ENDC = '\033[90m' #grey

def addthesuperadmin(name,email,password,phone,designation,birthdate,gender,address):
    data = {
        "name":name,
        "email":email,
        "password" : password,
        "phone":phone,
        "designation":designation,
        "birthdate":birthdate,
        "gender":gender,
        "address":address
        }

    r = requests.post(server+  "/addtheultrasupersupersebhiuparsuperadmin/",data = data)
    if r.json()["success"]:
        print (email , " user created\n")
        return r.json()["user_id"]
    else:
        print(r.json()["message"])
        if "error" in r.json():
            print(r.json()["error"])
    return None
def login(email,password):
    data = {
        "email" : email,
        "pwd" : password
        }
    r = requests.post(server+  "/login/",data = data)
    if r.json()["success"]:
        print (email , " Logged in succesfully\n")
        return r.json()
    else:
        print(r.json()["message"])
        if "error" in r.json():
            print(r.json()["error"])
    return None
def addorganization(name,orgtype,industry,phone,establishdate,mission,address,user_id):
    data = {
        "name":name,
        "orgtype":orgtype,
        "industry":industry,
        "phone":phone,
        "establishdate":establishdate,
        "mission":mission,
        "address":address,
        "user_id":user_id
        }
    r = requests.post(server+  "/addorganization/",data = data)
    if r.json()["success"]:
        print (name , " organization created\n")
        return r.json()["org_id"]
    else:
        print(r.json()["message"])
        if "error" in r.json():
            print(r.json()["error"])
    return None
def addadmin(name,email,phone,designation,birthdate,gender,address,user_id,org_id):
    data = {
        "name":name,
        "email":email,
        "phone":phone,
        "designation":designation,
        "birthdate":birthdate,
        "gender":gender,
        "address":address,
        "user_id" : user_id,
        "org_id" : org_id
        }

    r = requests.post(server+  "/addadmin/",data = data)
    if r.json()["success"]:
        print (email , " admin created\n")
        return r.json()["user_id"]
    else:
        print(r.json()["message"])
        if "error" in r.json():
            print(r.json()["error"])
    return None
def addproject(name,cid,desc,created_on,cdate,token):
    data = {
        "name" : name,
        "cid" : cid,
        "desc" : desc,
        "created_on" :  created_on,
        "cdate" :  cdate
    }
    r = requests.post(server+  "/addProject/",json = data,headers={"Authorization":token})
    if r.json()["success"]:
        print (name , " project created")
        return r.json()["project_id"]
    else:
        print(r.json()["message"])
        if "error" in r.json():
            print(r.json()["error"])
    return None
def adduser(name,email,phone,designation,birthdate,gender,address,user_id):
    data = {
        "name":name,
        "email":email,
        "phone":phone,
        "designation":designation,
        "birthdate":birthdate,
        "gender":gender,
        "address":address,
        "user_id" : user_id
        }

    r = requests.post(server+  "/adduser/",data = data)
    if r.json()["success"]:
        print (email , " user created\n")
        return r.json()["user_id"]
    else:
        print(r.json()["message"])
        if "error" in r.json():
            print(r.json()["error"])
    return None
def giveuseraccess(user_id,access,access_id,user_id_togive):
    data = {
        "user_id":user_id,
        "access" : access,
        "access_id" : access_id,
        "user_id_togive" : user_id_togive
    }
    r = requests.post(server+  "/giveuseraccess/",data = data)
    if r.json()["success"]:
        print(r.json()["message"])
    else:
        print(r.json()["message"])
        if "error" in r.json():
            print(r.json()["error"])

def assesorlogin(phone,password):
    data = {
        "phone" : phone,
        "pwd" : password
        }
    r = requests.post(server+  "/assesorlogin/",data = data)
    if r.json()["success"]:
        print (phone , " Logged in succesfully\n")
        return r.json()
    else:
        print(r.json()["message"])
        if "error" in r.json():
            print(r.json()["error"])
    return None


def save(data):
    # local_json = "work.json"
    # local_json  = "home.json"
    # local_json  = "start_dynamic.json"
    local_json = "server.json"
    with open(local_json, 'w') as outfile:
        json.dump(data, outfile)
def getdata():
    # local_json = "work.json"
    # local_json  = "home.json"
    # local_json  = "start_dynamic.json"
    local_json = "server.json"
    data = {}
    with open(local_json) as data_file:    
        data = json.load(data_file)
    return data
def test_addsuperadmin(superadmin_name,data):
    temp = addthesuperadmin("Shubhanshu Soni","shubhanshu.soni@qcin.org","zxcvbn","+91-9956834345","Analyst",time.mktime(datetime.timetuple(f.date_time_this_century())),"Male","C 4/9 Acharya Niketan Mayur Vihar Phase 1 110091 Delhi")
    print (temp)
    if temp:
        data[superadmin_name] = temp
        # save(data)
        print (data)
def test_addorganizations(superadmin,data,no):
    for i in range(0,no):
        temp = addorganization(f.company(),"Goverment","IT,Health and Education","011-24024010",time.mktime(datetime.timetuple(f.date_time_this_century())),"Nationwide Quality",f.address(),superadmin)
        if temp:
            data["o" + str(i+1) ] = temp
            save(data) 
def test_addadmins(superadmin,org,org_name,data,no):
    for i in range(0,no):
        temp = addadmin(f.name_male(),f.email(),"+91" + str(f.phone_number()).replace("-","")[0:10],"MT",time.mktime(datetime.timetuple(f.date_time_this_century())),"Male",f.address(),superadmin,org)
        if temp:
            data["a" + str(i+1) + "_" + org_name] = temp
            save(data)
def test_addprojects(admin,admin_name,data,no):
    for i in range(0,no):
        temp = addproject("Project " + f.company(),admin)
        if temp:
            data["p" + str(i+1) + "_"  +admin_name] =  temp
            save(data)
def test_addusers(admin,admin_name,data,no):
    for i in range(0,no):
        user1 = adduser(f.name_male(),f.email(),"+91" + str(f.phone_number()).replace("-","")[0:10],"MT",time.mktime(datetime.timetuple(f.date_time_this_century())),"Male",f.address(),admin)    
        if user1:
            data["u"+ str(i+1) + "_" +admin_name] =  user1
            save(data)
def test_addforms(user,project,project_name,data,no):
    for i in range(0,no):
        form1 = addform("Form "  + f.city(),project,user,list({"Hey":"Hi"}))
        if form1:
            data["f"+ str(i+1) + "_" +project_name] = form1
        save(data)
def test_addassesors(user,project,project_name,data,no):
    for i in range(0,no):
        form1 = inviteassesor("+91" + str(f.phone_number()).replace("-","")[0:10],user,project)
        if form1:
            data["a"+ str(i+1) + "_" +project_name] = form1
        save(data)
def test_addteams(user,project,project_name,data,no):
    for i in range(0,no):
        t = addteam("Team " + f.company(),user,project)
        if t:
            data["t"+ str(i+1) + "_" +project_name] = t
        save(data)

def getsuperadminsinsystem():
    r = requests.get(server+  "/getsuperadminsinsystem/")
    if r.json()["success"]:
        print(len(r.json()["data"]))
        for d in r.json()["data"]:
            print (d["user_name"],d["user_id"])
        return r.json()["data"]
    else:
        print(r.json()["message"])
        if "error" in r.json():
            print(r.json()["error"])
        return None
# def getalladmins():
# def getallusers():
# def getallprojects():
# def getallforms():
# def getallassesors():
# def getallteams():
# def getallorganizations():
def getadminsinorganization(user_id,org_id):
    data = {
        "org_id":org_id,
        "user_id":user_id
    }
    r = requests.post(server+  "/getadminsinorganization/",data = data)
    if r.json()["success"]:
        print(str(len(r.json()["data"])) + " admins in organization " + r.json()["org_name"])
        for d in r.json()["data"]:
            print (d["user_name"],d["user_id"])
        return r.json()["data"]
    else:
        print(r.json()["message"])
        if "error" in r.json():
            print(r.json()["error"])
        return None
def getprojectsinorganization(user_id,org_id):
    data = {
        "org_id":org_id,
        "user_id":user_id
    }
    r = requests.post(server+  "/getprojectsinorganization/",data = data)
    if r.json()["success"]:
        print(str(len(r.json()["data"])) + " projects in organization " + r.json()["org_name"])
        for d in r.json()["data"]:
            print (d["project_name"],d["project_id"])
    else:
        print(r.json()["message"])
        if "error" in r.json():
            print(r.json()["error"])
    print()
def getusersinorganization(user_id,org_id):
    data = {
        "org_id":org_id,
        "user_id":user_id
    }
    r = requests.post(server+  "/getusersinorganization/",data = data)
    if r.json()["success"]:
        print(str(len(r.json()["data_admins"])) + " admins in organization " + r.json()["org_name"])        
        for d in r.json()["data_admins"]:
            print (d["user_name"],d["user_id"])
        print(str(len(r.json()["data_users"])) + " users in organization " + r.json()["org_name"]) 
        for d in r.json()["data_users"]:
            print (d["user_name"],d["user_id"])
        return r.json()["data_users"]
    else:
        print(r.json()["message"])
        if "error" in r.json():
            print(r.json()["error"])
        return None
    print()
def getorganizationsofuser(user_id):
    data = {
        "user_id":user_id
    }
    r = requests.post(server+  "/getorganizationsofuser/",data = data)
    if r.json()["success"]:
        print(str(len(r.json()["data"])) + " organizations of user " + r.json()["user_name"])        
        for d in r.json()["data"]:
            print (d["org_name"],d["org_id"])
        return r.json()["data"]
    else:
        print(r.json()["message"])
        if "error" in r.json():
            print(r.json()["error"])
        return None
def getprojectsofuser(user_id):
    data = {
        "user_id":user_id
    }
    r = requests.post(server+  "/getprojectsofuser/",data = data)
    if r.json()["success"]:
        print(str(len(r.json()["data"])) + " projects of user " + r.json()["user_name"])
        for d in r.json()["data"]:
            print (d["project_name"],d["project_id"])
        return r.json()["data"]
    else:
        print(r.json()["message"])
        if "error" in r.json():
            print(r.json()["error"])
    return None
def getformsofuser(user_id):
    data = {
        "user_id":user_id
    }
    r = requests.post(server+  "/getformsofuser/",data = data)
    if r.json()["success"]:
        print(str(len(r.json()["data"])) + " forms of user " + r.json()["user_name"])
        for d in r.json()["data"]:
            print (d["form_name"],d["form_id"])
        return r.json()["data"]
    else:
        print(r.json()["message"])
        if "error" in r.json():
            print(r.json()["error"])
        return None
    print()
def getformsinproject(user_id,project_id):
    data = {
        "user_id":user_id,
        "project_id":project_id
    }
    r = requests.post(server+  "/getformsinproject/",data = data)
    if r.json()["success"]:
        print(str(len(r.json()["data"])) + " "  + " forms in project " + r.json()["project_name"])
        for d in r.json()["data"]:
            print (d["form_name"],d["form_id"])
        return r.json()["data"]
    else:
        print(r.json()["message"])
        if "error" in r.json():
            print(r.json()["error"])
        return None
    print()
def getusersinproject(user_id,project_id):
    data = {
        "project_id":project_id,
        "user_id" : user_id
    }
    r = requests.post(server+  "/getusersinproject/",data = data)
    if r.json()["success"]:
        print(str(len(r.json()["data"])) + " "  + " users in project " + r.json()["project_name"])
        for d in r.json()["data"]:
            print (d["user_name"],d["user_id"])
        return r.json()["data"]
    else:
        print(r.json()["message"])
        if "error" in r.json():
            print(r.json()["error"])
        return None
    print()
def getusersinform(user_id,form_id):
    data = {
        "form_id":form_id,
        "user_id" : user_id
    }
    r = requests.post(server+  "/getusersinform/",data = data)
    if r.json()["success"]:
        print(str(len(r.json()["data"])) + " "  + " users in " + r.json()["form_name"])
        for d in r.json()["data"]:
            print (d["user_name"],d["user_id"])
        return r.json()["data"]
    else:
        print(r.json()["message"])
        if "error" in r.json():
            print(r.json()["error"])
        return None
    print()
def getassesorsinproject(user_id,project_id):
    data = {
        "user_id":user_id,
        "project_id":project_id
    }
    r = requests.post(server+  "/getassesorsinproject/",data = data)
    if r.json()["success"]:
        print(str(len(r.json()["data"])) + " "  + " assesors in project " + r.json()["project_name"])
        for d in r.json()["data"]:
            print (d["assesor_phone"],d["assesor_id"])
        return r.json()["data"]
    else:
        print(r.json()["message"])
        if "error" in r.json():
            print(r.json()["error"])
        return None
    print()
def getteamsinproject(user_id,project_id):
    data = {
        "user_id":user_id,
        "project_id":project_id
    }
    r = requests.post(server+  "/getteamsinproject/",data = data)
    if r.json()["success"]:
        print(str(len(r.json()["data"])) + " "  + " teams in project " + r.json()["project_name"])
        for d in r.json()["data"]:
            print (d["team_name"],d["team_id"])
        return r.json()["data"]
    else:
        print(r.json()["message"])
        if "error" in r.json():
            print(r.json()["error"])
        return None
    print()
def getteamsinform(user_id,form_id):
    data = {
        "user_id":user_id,
        "form_id":form_id
    }
    r = requests.post(server+  "/getteamsinform/",data = data)
    if r.json()["success"]:
        print(str(len(r.json()["data"])) + " "  + "teams in form " + r.json()["form_name"])
        for d in r.json()["data"]:
            print (d["team_name"],d["team_id"])
        return r.json()["data"]
    else:
        print(r.json()["message"])
        if "error" in r.json():
            print(r.json()["error"])
        return None
    print()
def getformsinteam(user_id,team_id):
    data = {
        "user_id":user_id,
        "team_id":team_id
    }
    r = requests.post(server+  "/getformsinteam/",data = data)
    if r.json()["success"]:
        print(str(len(r.json()["data"]))  + " forms in team " + r.json()["team_name"])
        for d in r.json()["data"]:
            print (d["form_name"],d["form_id"])
        return r.json()["data"]
    else:
        print(r.json()["message"])
        if "error" in r.json():
            print(r.json()["error"])
        return None
    print()
def getassesorsinteam(user_id,team_id):
    data = {
        "user_id":user_id,
        "team_id":team_id
    }
    r = requests.post(server+  "/getassesorsinteam/",data = data)
    if r.json()["success"]:
        print(str(len(r.json()["data"])) + " "  + "assesors in team " + r.json()["team_name"])
        for d in r.json()["data"]:
            print (d["assesor_phone"],d["assesor_id"])
        return r.json()["data"]
    else:
        print(r.json()["message"])
        if "error" in r.json():
            print(r.json()["error"])
        return None
    print()
def getassesorsinform(user_id,form_id):
    data = {
        "user_id":user_id,
        "form_id":form_id
    }
    r = requests.post(server+  "/getassesorsinform/",data = data)
    if r.json()["success"]:
        print(str(len(r.json()["data"])) + " assesors in form " + r.json()["form_name"])
        for d in r.json()["data"]:
            print (d["assesor_phone"],d["assesor_id"])
        return r.json()["data"]
    else:
        print(r.json()["message"])
        if "error" in r.json():
            print(r.json()["error"])
        return None
    print()
def getformsofassesor(user_id,assesor_phone):
    data = {
        "user_id":user_id,
        "phone":assesor_phone
    }
    r = requests.post(server+  "/getformsofassesor/",data = data)
    if r.json()["success"]:
        print(str(len(r.json()["data"])) + " forms of assesor " + r.json()["assesor_phone"])
        for d in r.json()["data"]:
            print (d["form_name"],d["form_id"])
        return r.json()["data"]
    else:
        print(r.json()["message"])
        if "error" in r.json():
            print(r.json()["error"])
        return None
    print()
def getteamsofassesor(user_id,assesor_phone):
    data = {
        "user_id":user_id,
        "phone":assesor_phone
    }
    r = requests.post(server+  "/getteamsofassesor/",data = data)
    if r.json()["success"]:
        print(str(len(r.json()["data"])) + " teams of assesor " + r.json()["assesor_phone"])
        for d in r.json()["data"]:
            print (d["team_name"],d["team_id"])
        return r.json()["data"]
    else:
        print(r.json()["message"])
        if "error" in r.json():
            print(r.json()["error"])
        return None
    print()
# def getresponsesinform(user_id,form_id):

class check_add_methods():
    def check_addthesuperadmin(total_no,test_no,name):
        data = getdata()
        check = getsuperadminsinsystem()
        if check:
            found1 = False
            for temp in check:
                if temp["user_id"] == data[name]:
                    found1 = True
            if len(check)==total_no:
                if found1:
                    print ("{color}{val}".format(color=colors.OKGREEN,val=str(test_no) + " Passed"),"{color}".format(color=colors.DEFAULT))
                else:
                    print ("{color}{val}".format(color=colors.FAIL,val=str(test_no) + " Failed " + name + "not found"),"{color}".format(color=colors.DEFAULT))            
            else:
                print ("{color}{val}".format(color=colors.FAIL,val=str(test_no) + " Failed Total No Expected : " + str(total_no) + ", Found : " + str(len(check))),"{color}".format(color=colors.DEFAULT))
        else:
            print ("{color}{val}".format(color=colors.FAIL,val=str(test_no) + " Failed Get method returned None"),"{color}".format(color=colors.DEFAULT))
        print()
    def check_login(email,pwd,test_no):
        check = login(email,pwd)
        if check:
            if check["success"]:
                print ("{color}{val}".format(color=colors.OKGREEN,val=str(test_no) + " Passed"),"{color}".format(color=colors.DEFAULT))
            else:
                print ("{color}{val}".format(color=colors.FAIL,val=str(test_no) + " Failed " + check["message"]),"{color}".format(color=colors.DEFAULT))
        else:
            print ("{color}{val}".format(color=colors.FAIL,val=str(test_no) + " Failed Get method returned None"),"{color}".format(color=colors.DEFAULT))
        print()
    def check_addorganizations(total_no,test_no,name):
        data = getdata()
        check = getorganizationsofuser(data["superadmin"])
        if check:
            found1 = False
            for temp in check:
                if temp["org_id"] == data[name]:
                    found1 = True
            if len(check)==total_no:
                if found1:
                    print ("{color}{val}".format(color=colors.OKGREEN,val=str(test_no) + " Passed"),"{color}".format(color=colors.DEFAULT))
                else:
                    print ("{color}{val}".format(color=colors.FAIL,val=str(test_no) + " Failed " + name + "not found"),"{color}".format(color=colors.DEFAULT))            
            else:
                print ("{color}{val}".format(color=colors.FAIL,val=str(test_no) + " Failed Total No Expected : " + str(total_no) + ", Found : " + str(len(check))),"{color}".format(color=colors.DEFAULT))
        else:
            print ("{color}{val}".format(color=colors.FAIL,val=str(test_no) + " Failed Get method returned None"),"{color}".format(color=colors.DEFAULT))
        print()
    def check_addadmins(user_id,org_id,total_no,test_no,name):
        data = getdata()
        check = getadminsinorganization(user_id,org_id)
        if check:
            found1 = False
            for temp in check:
                if temp["user_id"] == data[name]:
                    found1 = True
            if len(check)==total_no:
                if found1:
                    print ("{color}{val}".format(color=colors.OKGREEN,val=str(test_no) + " Passed"),"{color}".format(color=colors.DEFAULT))
                else:
                    print ("{color}{val}".format(color=colors.FAIL,val=str(test_no) + " Failed " + name + "not found"),"{color}".format(color=colors.DEFAULT))            
            else:
                print ("{color}{val}".format(color=colors.FAIL,val=str(test_no) + " Failed Total No Expected : " + str(total_no) + ", Found : " + str(len(check))),"{color}".format(color=colors.DEFAULT))
        else:
            print ("{color}{val}".format(color=colors.FAIL,val=str(test_no) + " Failed Get method returned None"),"{color}".format(color=colors.DEFAULT))
        print()
    def check_addprojects(user_id,total_no,test_no,name):
        data = getdata()
        check = getprojectsofuser(user_id)
        if check:
            found1 = False
            for temp in check:
                if temp["project_id"] == data[name]:
                    found1 = True
            if len(check)==total_no:
                if found1:
                    print ("{color}{val}".format(color=colors.OKGREEN,val=str(test_no) + " Passed"),"{color}".format(color=colors.DEFAULT))
                else:
                    print ("{color}{val}".format(color=colors.FAIL,val=str(test_no) + " Failed " + name + "not found"),"{color}".format(color=colors.DEFAULT))            
            else:
                print ("{color}{val}".format(color=colors.FAIL,val=str(test_no) + " Failed Total No Expected : " + str(total_no) + ", Found : " + str(len(check))),"{color}".format(color=colors.DEFAULT))
        else:
            print ("{color}{val}".format(color=colors.FAIL,val=str(test_no) + " Failed Get method returned None"),"{color}".format(color=colors.DEFAULT))
        print()
    def check_adduser(user_id,org_id,total_no,test_no,name):
        data = getdata()
        check = getusersinorganization(user_id,org_id)
        if check:
            found1 = False
            for temp in check:
                if temp["user_id"] == data[name]:
                    found1 = True
            if len(check)==total_no:
                if found1:
                    print ("{color}{val}".format(color=colors.OKGREEN,val=str(test_no) + " Passed"),"{color}".format(color=colors.DEFAULT))
                else:
                    print ("{color}{val}".format(color=colors.FAIL,val=str(test_no) + " Failed " + name + "not found"),"{color}".format(color=colors.DEFAULT))            
            else:
                print ("{color}{val}".format(color=colors.FAIL,val=str(test_no) + " Failed Total No Expected : " + str(total_no) + ", Found : " + str(len(check))),"{color}".format(color=colors.DEFAULT))
        else:
            print ("{color}{val}".format(color=colors.FAIL,val=str(test_no) + " Failed Get method returned None"),"{color}".format(color=colors.DEFAULT))
        print()
    def check_usersaccessinproject(llist,user_id,project_id,test_no):
        data = getdata()
        check = getusersinproject(user_id,project_id)
        if check:
            found_count = 0
            for temp in check:
                if temp["user_id"] in llist:
                    found_count+=1
            if found_count==len(llist):
                print ("{color}{val}".format(color=colors.OKGREEN,val=str(test_no) + " Passed"),"{color}".format(color=colors.DEFAULT))
            else:
                print ("{color}{val}".format(color=colors.FAIL,val=str(test_no) + " Failed Total No Expected : " + str(len(llist)) + ", Found : " + str(len(check)) +  " Matched : " + str(found_count)),"{color}".format(color=colors.DEFAULT))
        else:
            print ("{color}{val}".format(color=colors.FAIL,val=str(test_no) + " Failed Get method returned None"),"{color}".format(color=colors.DEFAULT))
        print()
    def check_projectsassignedtouser(llist,user_id,test_no):
        data = getdata()
        check = getprojectsofuser(user_id)
        if check:
            found_count = 0
            for temp in check:
                if temp["project_id"] in llist:
                    found_count+=1
            if found_count==len(llist):
                print ("{color}{val}".format(color=colors.OKGREEN,val=str(test_no) + " Passed"),"{color}".format(color=colors.DEFAULT))
            else:
                print ("{color}{val}".format(color=colors.FAIL,val=str(test_no) + " Failed Total No Expected : " + str(len(llist)) + ", Found : " + str(len(check)) +  " Matched : " + str(found_count)),"{color}".format(color=colors.DEFAULT))
        else:
            print ("{color}{val}".format(color=colors.FAIL,val=str(test_no) + " Failed Get method returned None"),"{color}".format(color=colors.DEFAULT))
        print()
    def check_formsinproject(llist,user_id,project_id,test_no):
        data = getdata()
        check = getformsinproject(user_id,project_id)
        if check:
            found_count = 0
            for temp in check:
                if temp["form_id"] in llist:
                    found_count+=1
            if found_count==len(llist):
                print ("{color}{val}".format(color=colors.OKGREEN,val=str(test_no) + " Passed"),"{color}".format(color=colors.DEFAULT))
            else:
                print ("{color}{val}".format(color=colors.FAIL,val=str(test_no) + " Failed Total No Expected : " + str(len(llist)) + ", Found : " + str(len(check)) +  " Matched : " + str(found_count)),"{color}".format(color=colors.DEFAULT))
        else:
            print ("{color}{val}".format(color=colors.FAIL,val=str(test_no) + " Failed Get method returned None"),"{color}".format(color=colors.DEFAULT))
        print()
    def check_formsofuser(llist,user_id,test_no):
        data = getdata()
        check = getformsofuser(user_id)
        if check:
            found_count = 0
            for temp in check:
                if temp["form_id"] in llist:
                    found_count+=1
            if found_count==len(llist):
                print ("{color}{val}".format(color=colors.OKGREEN,val=str(test_no) + " Passed"),"{color}".format(color=colors.DEFAULT))
            else:
                print ("{color}{val}".format(color=colors.FAIL,val=str(test_no) + " Failed Total No Expected : " + str(len(llist)) + ", Found : " + str(len(check)) +  " Matched : " + str(found_count)),"{color}".format(color=colors.DEFAULT))
        else:
            print ("{color}{val}".format(color=colors.FAIL,val=str(test_no) + " Failed Get method returned None"),"{color}".format(color=colors.DEFAULT))
        print()
    def check_usersinform(llist,user_id,form_id,test_no):
        data = getdata()
        check = getusersinform(user_id,form_id)
        if check:
            found_count = 0
            for temp in check:
                if temp["user_id"] in llist:
                    found_count+=1
            if found_count==len(llist):
                print ("{color}{val}".format(color=colors.OKGREEN,val=str(test_no) + " Passed"),"{color}".format(color=colors.DEFAULT))
            else:
                print ("{color}{val}".format(color=colors.FAIL,val=str(test_no) + " Failed Total No Expected : " + str(len(llist)) + ", Found : " + str(len(check)) +  " Matched : " + str(found_count)),"{color}".format(color=colors.DEFAULT))
        else:
            print ("{color}{val}".format(color=colors.FAIL,val=str(test_no) + " Failed Get method returned None"),"{color}".format(color=colors.DEFAULT))
        print()
    def check_assesorsinproject(llist,user_id,project_id,test_no):
        data = getdata()
        check = getassesorsinproject(user_id,project_id)
        if check:
            found_count = 0
            for temp in check:
                if temp["assesor_phone"] in llist:
                    found_count+=1
            if found_count==len(llist):
                print ("{color}{val}".format(color=colors.OKGREEN,val=str(test_no) + " Passed"),"{color}".format(color=colors.DEFAULT))
            else:
                print ("{color}{val}".format(color=colors.FAIL,val=str(test_no) + " Failed Total No Expected : " + str(len(llist)) + ", Found : " + str(len(check)) +  " Matched : " + str(found_count)),"{color}".format(color=colors.DEFAULT))
        else:
            print ("{color}{val}".format(color=colors.FAIL,val=str(test_no) + " Failed Get method returned None"),"{color}".format(color=colors.DEFAULT))
        print()
    def check_teamsinproject(llist,user_id,project_id,test_no):
        data = getdata()
        check = getteamsinproject(user_id,project_id)
        if check:
            found_count = 0
            for temp in check:
                if temp["team_id"] in llist:
                    found_count+=1
            if found_count==len(llist):
                print ("{color}{val}".format(color=colors.OKGREEN,val=str(test_no) + " Passed"),"{color}".format(color=colors.DEFAULT))
            else:
                print ("{color}{val}".format(color=colors.FAIL,val=str(test_no) + " Failed Total No Expected : " + str(len(llist)) + ", Found : " + str(len(check)) +  " Matched : " + str(found_count)),"{color}".format(color=colors.DEFAULT))
        else:
            print ("{color}{val}".format(color=colors.FAIL,val=str(test_no) + " Failed Get method returned None"),"{color}".format(color=colors.DEFAULT))
        print()
    def check_teamsinform(llist,user_id,form_id,test_no):
        data = getdata()
        check = getteamsinform(user_id,form_id)
        if check:
            found_count = 0
            for temp in check:
                if temp["team_id"] in llist:
                    found_count+=1
            if found_count==len(llist):
                print ("{color}{val}".format(color=colors.OKGREEN,val=str(test_no) + " Passed"),"{color}".format(color=colors.DEFAULT))
            else:
                print ("{color}{val}".format(color=colors.FAIL,val=str(test_no) + " Failed Total No Expected : " + str(len(llist)) + ", Found : " + str(len(check)) +  " Matched : " + str(found_count)),"{color}".format(color=colors.DEFAULT))
        else:
            print ("{color}{val}".format(color=colors.FAIL,val=str(test_no) + " Failed Get method returned None"),"{color}".format(color=colors.DEFAULT))
        print()
    def check_formsinteam(llist,user_id,team_id,test_no):
        data = getdata()
        check = getformsinteam(user_id,team_id)
        if check:
            found_count = 0
            for temp in check:
                if temp["form_id"] in llist:
                    found_count+=1
            if found_count==len(llist):
                print ("{color}{val}".format(color=colors.OKGREEN,val=str(test_no) + " Passed"),"{color}".format(color=colors.DEFAULT))
            else:
                print ("{color}{val}".format(color=colors.FAIL,val=str(test_no) + " Failed Total No Expected : " + str(len(llist)) + ", Found : " + str(len(check)) +  " Matched : " + str(found_count)),"{color}".format(color=colors.DEFAULT))
        else:
            print ("{color}{val}".format(color=colors.FAIL,val=str(test_no) + " Failed Get method returned None"),"{color}".format(color=colors.DEFAULT))
        print()
    def check_assesorsinform(llist,user_id,form_id,test_no):
        data = getdata()
        check = getassesorsinform(user_id,form_id)
        if check:
            found_count = 0
            for temp in check:
                if temp["assesor_phone"] in llist:
                    found_count+=1
            if found_count==len(llist):
                print ("{color}{val}".format(color=colors.OKGREEN,val=str(test_no) + " Passed"),"{color}".format(color=colors.DEFAULT))
            else:
                print ("{color}{val}".format(color=colors.FAIL,val=str(test_no) + " Failed Total No Expected : " + str(len(llist)) + ", Found : " + str(len(check)) +  " Matched : " + str(found_count)),"{color}".format(color=colors.DEFAULT))
        else:
            print ("{color}{val}".format(color=colors.FAIL,val=str(test_no) + " Failed Get method returned None"),"{color}".format(color=colors.DEFAULT))
        print()
    def check_formsofassesor(llist,user_id,assesor_phone,test_no):
        data = getdata()
        check = getformsofassesor(user_id,assesor_phone)
        if check:
            found_count = 0
            for temp in check:
                if temp["form_id"] in llist:
                    found_count+=1
            if found_count==len(llist):
                print ("{color}{val}".format(color=colors.OKGREEN,val=str(test_no) + " Passed"),"{color}".format(color=colors.DEFAULT))
            else:
                print ("{color}{val}".format(color=colors.FAIL,val=str(test_no) + " Failed Total No Expected : " + str(len(llist)) + ", Found : " + str(len(check)) +  " Matched : " + str(found_count)),"{color}".format(color=colors.DEFAULT))
        else:
            print ("{color}{val}".format(color=colors.FAIL,val=str(test_no) + " Failed Get method returned None"),"{color}".format(color=colors.DEFAULT))
        print()
    def check_assesorsinteam(llist,user_id,team_id,test_no):
        data = getdata()
        check = getassesorsinteam(user_id,team_id)
        if check:
            found_count = 0
            for temp in check:
                if temp["assesor_phone"] in llist:
                    found_count+=1
            if found_count==len(llist):
                print ("{color}{val}".format(color=colors.OKGREEN,val=str(test_no) + " Passed"),"{color}".format(color=colors.DEFAULT))
            else:
                print ("{color}{val}".format(color=colors.FAIL,val=str(test_no) + " Failed Total No Expected : " + str(len(llist)) + ", Found : " + str(len(check)) +  " Matched : " + str(found_count)),"{color}".format(color=colors.DEFAULT))
        else:
            print ("{color}{val}".format(color=colors.FAIL,val=str(test_no) + " Failed Get method returned None"),"{color}".format(color=colors.DEFAULT))
        print()
    def check_teamsofassesor(llist,user_id,assesor_phone,test_no):
        data = getdata()
        check = getteamsofassesor(user_id,assesor_phone)
        if check:
            found_count = 0
            for temp in check:
                if temp["team_id"] in llist:
                    found_count+=1
            if found_count==len(llist):
                print ("{color}{val}".format(color=colors.OKGREEN,val=str(test_no) + " Passed"),"{color}".format(color=colors.DEFAULT))
            else:
                print ("{color}{val}".format(color=colors.FAIL,val=str(test_no) + " Failed Total No Expected : " + str(len(llist)) + ", Found : " + str(len(check)) +  " Matched : " + str(found_count)),"{color}".format(color=colors.DEFAULT))
        else:
            print ("{color}{val}".format(color=colors.FAIL,val=str(test_no) + " Failed Get method returned None"),"{color}".format(color=colors.DEFAULT))
        print()

def moveadmintouser(user_id,user_id_tomove):
    data = {
        "user_id_tomove":user_id_tomove,
        "user_id":user_id,
    }
    r = requests.post(server+  "/moveadmintouser/",data = data)
    if r.json()["success"]:
        print(r.json()["message"])
    else:
        print(r.json()["message"])
        if "error" in r.json():
            print(r.json()["error"])
    print()
def moveusertoadmin(user_id,user_id_tomove):
    data = {
        "user_id_tomove":user_id_tomove,
        "user_id":user_id,
    }
    r = requests.post(server+  "/moveusertoadmin/",data = data)
    if r.json()["success"]:
        print(r.json()["message"])
    else:
        print(r.json()["message"])
        if "error" in r.json():
            print(r.json()["error"])
    print ()
def removeuserfromproject(user_id,user_id_toremove,project_id):
    data = {
        "user_id_toremove":user_id_toremove,
        "user_id":user_id,
        "project_id" : project_id
    }
    r = requests.post(server+  "/removeuserfromproject/",data = data)
    if r.json()["success"]:
        print(r.json()["message"])
    else:
        print(r.json()["message"])
        if "error" in r.json():
            print(r.json()["error"])
    print ()
def changeProjectName(user_id,project_id,name):
    data = {
        "user_id": user_id,
        "project_id" : project_id,
        "name":name
    }
    r = requests.post(server+  "/changeProjectName/",data=data)
    if r.json()["success"]:
        print ("Changes done\n")
    else:
        print(r.json()["message"])
        if "error" in r.json():
            print(r.json()["error"])
def removeAssesorfromFrom(user_id,form_id,assesor_phone_toremove):
    data = {
        "user_id":user_id,
        "form_id":form_id,
        "assesor_phone_toremove":assesor_phone_toremove
    }
    r = requests.post(server+  "/removeassesorfromform/",data=data)
    if r.json()["success"]:
        print ("Changes done\n")
    else:
        print(r.json()["message"])
        if "error" in r.json():
            print(r.json()["error"])
def logactionfilter(user_id,what=None):
    data = {
        "who":user_id
    }
    r = requests.post(server+  "/logActionsFilter/",json=data)
    if r.json()["success"]:
        print(r.json()["message"])
        print ()
        print ("\n".join([str(item) for item in r.json()["logs"]]))
    else:
        print(r.json()["message"])
        if "error" in r.json():
            print(r.json()["error"])
def test_edit_methods():
    # changeProjectName("ca83bf0d67604cbd8fbc21e2af9a0d03","15145445330663680","Swachch Bharat Toilet Mapping")
    user_id = "319424f5b8524ebe8188c2d40217c48c"
    removeAssesorfromFrom(user_id,"0baf9784ebf149f8a944e3d4520e6f9b","9999999999")
# test_edit_methods()

def test_move_methods():
    data = getdata()

    # getadminsinorganization(data["superadmin"],data["o1"])
    # getusersinorganization(data["superadmin"],data["o1"])

    # moveusertoadmin(data["superadmin"],"f194d9ced15743069300bd9a66462ee8")

    # newadmins = getadminsinorganization(data["superadmin"],data["o1"])
    # newusers  = getusersinorganization(data["superadmin"],data["o1"])
    
    # tn = 1
    # if ("f194d9ced15743069300bd9a66462ee8" in [i["user_id"] for i in newadmins]) and ("f194d9ced15743069300bd9a66462ee8" not in [i["user_id"] for i in newusers]):
    #     print ("{color}{val}".format(color=colors.OKGREEN,val=str(tn) + " Passed "),"{color}".format(color=colors.DEFAULT));tn+=1
    # else:
    #     print ("{color}{val}".format(color=colors.FAIL,val=str(tn) + " Failed "),"{color}".format(color=colors.DEFAULT));tn+=1

    # moveadmintouser(data["superadmin"],"f194d9ced15743069300bd9a66462ee8")

    # newadmins = getadminsinorganization(data["superadmin"],data["o1"])
    # newusers  = getusersinorganization(data["superadmin"],data["o1"])
    
    # if ("f194d9ced15743069300bd9a66462ee8" not in [i["user_id"] for i in newadmins]) and ("f194d9ced15743069300bd9a66462ee8" in [i["user_id"] for i in newusers]):
    #     print ("{color}{val}".format(color=colors.OKGREEN,val=str(tn) + " Passed "),"{color}".format(color=colors.DEFAULT));tn+=1
    # else:
    #     print ("{color}{val}".format(color=colors.FAIL,val=str(tn) + " Failed "),"{color}".format(color=colors.DEFAULT));tn+=1

    getusersinproject(data["a1_o1"],data["p1_a1_o1"])

    # removeuserfromproject(data["a1_o1"],"0f4f382167cd40f2ad966da3b84969d3",data["p1_a1_o1"]) #Will Fail
    removeuserfromproject(data["a1_o1"],"f194d9ced15743069300bd9a66462ee8",data["p1_a1_o1"]) #Will Fail

    
    getusersinproject(data["a1_o1"],data["p1_a1_o1"])
# test_move_methods()
def test_add_methods4():
    data = getdata()    


    # addforminteam(data["t1_z"],data[data["usersof"]["p1_a2_o1"][0]],data["f1_y"])
    # data["teamsof"]["f1_y"] = ["t1_z"]
    # data["formsof"]["t1_z"] = ["f1_y"] 
    # save(data)

    # addforminteam(data["t1_z"],data[data["usersof"]["p1_a2_o1"][0]],data["f1_c"])
    # data["teamsof"]["f1_c"] = ["t1_z"]    
    # data["formsof"]["t1_z"].append("f1_c")
    # save(data)

    # addforminteam(data["t1_y"],data[data["usersof"]["p1_a2_o1"][0]],data["f1_c"])
    # data["teamsof"]["f1_c"].append("t1_y")    
    # data["formsof"]["t1_y"] = ["f1_c"]
    # save(data)

    # check_add_methods.check_teamsinform([data["t1_z"],data["t1_y"]],data["u1_a1_o1"],data["f1_c"],tn);tn+=1
    # check_add_methods.check_teamsinform([data["t1_z"]],data["u1_a1_o1"],data["f1_y"],tn);tn+=1
    # check_add_methods.check_formsinteam([data["f1_c"]],data["u1_a1_o1"],data["t1_y"],tn);tn+=1
    # check_add_methods.check_formsinteam([data["f1_y"],data["f1_c"]],data["u1_a1_o1"],data["t1_z"],tn);tn+=1

    # addassesorinteam(data["a1_z"],data["u1_a1_o1"],data["t1_z"])
    # addassesorinteam(data["a1_y"],data["u1_a1_o1"],data["t1_z"])
    # addassesorinteam(data["a1_z"],data["u1_a1_o1"],data["t1_y"])

    # check_add_methods.check_assesorsinteam([data["a1_z"],data["a1_y"]],data["u1_a1_o1"],data["t1_z"],tn);tn+=1
    # check_add_methods.check_assesorsinteam([data["a1_z"]],data["u1_a1_o1"],data["t1_y"],tn);tn+=1
    # check_add_methods.check_teamsofassesor([data["t1_z"],data["t1_y"]],data["u1_a1_o1"],data["a1_z"],tn);tn+=1
    # check_add_methods.check_teamsofassesor([data["t1_z"]],data["u1_a1_o1"],data["a1_y"],tn);tn+=1

    tn = 54

    # getformsofassesor(data["u1_a1_o1"],data["a1_z"])
    getformsofassesor(data["u1_a1_o1"],data["a1_y"])
    # SINGLEFORMS
    # [{'form_id': '331b5a5a6ebd497796cd5aa17b81f521', 'form_name': 'Form East Matthewshire'}]
    
    # test_addforms(data["u1_a1_o1"],data["p1_a2_o1"],"z",data,1)
    # test_addforms(data["u1_a1_o1"],data["p1_a2_o1"],"b",data,1)

    addassesorinform(data["a1_y"],data["u1_a1_o1"],data["f1_z"])
    addassesorinform(data["a1_y"],data["u1_a1_o1"],data["f1_b"])
    
    getformsofassesor(data["u1_a1_o1"],data["a1_y"])
    # SINGLEFORMS
    # [{'form_id': '331b5a5a6ebd497796cd5aa17b81f521', 'form_name': 'Form East Matthewshire'}, 
    # {'form_id': '19d5a4cf49e543ce9c33d42e3980f502', 'form_name': 'Form Stoneshire'}]

    test_addteams(data["u1_a1_o1"],data["p1_a2_o1"],"a",data,1)

    addforminteam(data["t1_a"],data["u1_a1_o1"],data["f1_z"])

    addassesorinteam(data["a1_y"],data["u1_a1_o1"],data["t1_a"])

    getformsofassesor(data["u1_a1_o1"],data["a1_y"])    
    # SINGLEFORMS
    # [{'form_id': '19d5a4cf49e543ce9c33d42e3980f502', 'form_name': 'Form Stoneshire'}]
# test_add_methods4()
def test_add_methods3():
    data = getdata()

    #TODO data["assesorsof"] = {}
    # test_addassesors(data["a1_o1"],data["p1_a1_o1"],"w",data,1)
    # data["projectsof"]["a1_w"] = ["p1_a1_o1"]
    # data["assesorsof"]["p1_a1_o1"] = ["a1_w"]
    # save(data)

    # test_addassesors(data["a1_o1"],data["p2_a1_o1"],"x",data,1)
    # data["projectsof"]["a1_x"] = ["p2_a1_o1"]
    # data["assesorsof"]["p2_a1_o1"] = ["a1_x"]
    # save(data)

    # test_addassesors(data["u1_a1_o1"],data["p1_a2_o1"],"y",data,1)
    # data["projectsof"]["a1_y"] = ["p1_a2_o1"]
    # data["assesorsof"]["p1_a2_o1"] = ["a1_y"]
    # save(data)

    # test_addassesors(data["u2_a1_o1"],data["p1_a2_o1"],"z",data,1)
    # data["projectsof"]["a1_z"] = ["p1_a2_o1"]
    # data["assesorsof"]["p1_a2_o1"].append("a1_z")
    # save(data)

    # check_add_methods.check_assesorsinproject([data[i] for i in data["assesorsof"]["p1_a1_o1"]],data["u1_a1_o1"],data["p1_a1_o1"],tn);tn+=1
    # check_add_methods.check_assesorsinproject([data[i] for i in data["assesorsof"]["p1_a2_o1"]],data["u1_a1_o1"],data["p1_a2_o1"],tn);tn+=1
    # check_add_methods.check_assesorsinproject([data[i] for i in data["assesorsof"]["p2_a1_o1"]],data["u1_a1_o1"],data["p2_a1_o1"],tn);tn+=1    
    # check_add_methods.check_assesorsinproject([data[i] for i in data["assesorsof"]["p1_a2_o1"]],data[data["usersof"]["p1_a2_o1"][0]],data["p1_a2_o1"],tn);tn+=1
    
    # TODO data["teamsof"] = {}

    # test_addteams(data["a1_o1"],data["p1_a1_o1"],"w",data,1)
    # data["projectsof"]["t1_w"] = ["p1_a1_o1"]
    # data["teamsof"]["p1_a1_o1"] = ["t1_w"]
    # save(data)

    # test_addteams(data["a1_o1"],data["p2_a1_o1"],"x",data,1)
    # data["projectsof"]["t1_x"] = ["p2_a1_o1"]
    # data["teamsof"]["p2_a1_o1"] = ["t1_x"]
    # save(data)

    # test_addteams(data["u1_a1_o1"],data["p1_a2_o1"],"y",data,1)
    # data["projectsof"]["t1_y"] = ["p1_a2_o1"]
    # data["teamsof"]["p1_a2_o1"] = ["t1_y"]
    # save(data)

    # test_addteams(data["u2_a1_o1"],data["p1_a2_o1"],"z",data,1)
    # data["projectsof"]["t1_z"] = ["p1_a2_o1"]
    # data["teamsof"]["p1_a2_o1"].append("t1_z")
    # save(data)

    # check_add_methods.check_teamsinproject([data[i] for i in data["teamsof"]["p1_a1_o1"]],data["u1_a1_o1"],data["p1_a1_o1"],tn);tn+=1
    # check_add_methods.check_teamsinproject([data[i] for i in data["teamsof"]["p1_a2_o1"]],data["u1_a1_o1"],data["p1_a2_o1"],tn);tn+=1
    # check_add_methods.check_teamsinproject([data[i] for i in data["teamsof"]["p2_a1_o1"]],data["u1_a1_o1"],data["p2_a1_o1"],tn);tn+=1    
    # check_add_methods.check_teamsinproject([data[i] for i in data["teamsof"]["p1_a2_o1"]],data[data["usersof"]["p1_a2_o1"][0]],data["p1_a2_o1"],tn);tn+=1
# test_add_methods3()
def test_add_methods2():
    data = getdata()
    # test_addforms(data["a1_o1"],data["p1_a1_o1"],"x",data,1)
    # test_addforms(data["u1_a1_o1"],data["p1_a1_o1"],"a",data,1)
    # test_addforms(data["u1_a1_o1"],data["p1_a2_o1"],"y",data,1)
    # test_addforms(data["u2_a1_o1"],data["p1_a2_o1"],"c",data,1)

    # tn  = 31
    # check_add_methods.check_formsinproject([data["f1_x"],data["f1_a"]],data["a1_o1"],data["p1_a1_o1"],tn);tn+=1
    # check_add_methods.check_formsinproject([data["f1_y"],data["f1_c"]],data["a2_o1"],data["p1_a2_o1"],tn);tn+=1

    # check_add_methods.check_formsofuser([data["f1_y"],data["f1_c"],data["f1_x"],data["f1_a"]],data["u1_a1_o1"],tn);tn+=1
    # check_add_methods.check_formsofuser([data["f1_y"],data["f1_c"]],data["u2_a1_o1"],tn);tn+=1
    # check_add_methods.check_formsofuser([data["f1_x"],data["f1_a"]],data["u1_a2_o1"],tn);tn+=1

    tn = 36
    # usersof = {
    #     "f1_x":["u1_a2_o1","u1_a1_o1"],
    #     "f1_a":["u1_a2_o1","u1_a1_o1"],
    #     "f1_c":["u2_a1_o1","u1_a1_o1"],
    #     "f1_y":["u2_a1_o1","u1_a1_o1"],
    #     "p1_a2_o1":["u1_a1_o1","u2_a1_o1"],
    #     "p2_a1_o1":["u1_a1_o1"],
    #     "p1_a1_o1":["u1_a1_o1","u1_a2_o1"]
    # }
    # projectsof = {
    #     "u1_a2_o1":["p1_a1_o1"],
    #     "u1_a1_o1":["p1_a1_o1","p1_a2_o1","p2_a1_o1"],
    #     "u2_a1_o1":["p1_a2_o1"],
    #     "f1_x":["p1_a1_o1"],
    #     "f1_a":["p1_a1_o1"],
    #     "f1_c":["p1_a2_o1"],
    #     "f1_y":["p1_a2_o1"]
    # }
    # formsof = {
    #     "u1_a1_o1": ["f1_x","f1_a","f1_c" ,"f1_y"],
    #     "u2_a1_o1" : ["f1_y","f1_c"],
    #     "u1_a2_o1": ["f1_x","f1_a"],
    #     "p1_a2_o1" : ["f1_y","f1_c"],
    #     "p1_a1_o1": ["f1_x","f1_a"]
    # }

    # check_add_methods.check_usersinform([data[i] for i in usersof["f1_x"]],data["a1_o1"],data["f1_x"],tn);tn+=1
    # check_add_methods.check_usersinform([data[i] for i in usersof["f1_a"]],data["a1_o1"],data["f1_a"],tn);tn+=1
    # check_add_methods.check_usersinform([data[i] for i in usersof["f1_c"]],data["a2_o1"],data["f1_c"],tn);tn+=1
    # check_add_methods.check_usersinform([data[i] for i in usersof["f1_y"]],data["a2_o1"],data["f1_y"],tn);tn+=1
    
    # giveuseraccess(data["u1_a1_o1"],"form",data["f1_a"],data["u2_a1_o1"])
    # usersof["f1_a"].append("u2_a1_o1")
    # formsof["u2_a1_o1"].append("f1_a")
    # giveuseraccess(data["u1_a1_o1"],"form",data["f1_c"],data["u1_a2_o1"])
    # usersof["f1_c"].append("u1_a2_o1")
    # formsof["u1_a2_o1"].append("f1_c")

    # data["usersof"] = usersof
    # data["projectsof"]  = projectsof
    # data["formsof"] = formsof
    # save(data)

    # check_add_methods.check_usersinform([data[i] for i in usersof["f1_x"]],data["a1_o1"],data["f1_x"],tn);tn+=1
    # check_add_methods.check_usersinform([data[i] for i in usersof["f1_a"]],data["a1_o1"],data["f1_a"],tn);tn+=1
    # check_add_methods.check_usersinform([data[i] for i in usersof["f1_c"]],data["a2_o1"],data["f1_c"],tn);tn+=1
    # check_add_methods.check_usersinform([data[i] for i in usersof["f1_y"]],data["a2_o1"],data["f1_y"],tn);tn+=1
    
    # # # Will Return No Success
    # giveuseraccess(data["u1_a1_o1"],"form",data["f1_x"],data["u1_a2_o1"])
    # giveuseraccess(data["u1_a1_o1"],"form",data["f1_c"],data["u1_a2_o1"])
# test_add_methods2()
def test_add_methods1():
    sleep_time = 2
    data = getdata()
    
    # data = dict()
    # test_addsuperadmin("superadmin",data)
    # time.sleep(sleep_time)
    
    # check_add_methods.check_addthesuperadmin(1,1,"superadmin")
    # check_add_methods.check_login("shubhanshu.soni@qcin.org","zxcvbn",2)

    # test_addorganizations(data["superadmin"],data,1)
    time.sleep(sleep_time)

    # check_add_methods.check_addorganizations(2,3,"o1")
    # check_add_methods.check_addorganizations(2,4,"o2")

    test_addadmins(data["superadmin"],data["o1"],"o1",data,1)
    
    # test_addadmins(data["superadmin"],data["o2"],"o2",data,2)
    # time.sleep(sleep_time)

    # check_add_methods.check_addadmins(data["superadmin"],data["o1"],3,5,"a1_o1")
    # check_add_methods.check_addadmins(data["superadmin"],data["o1"],3,6,"a2_o1")
    # check_add_methods.check_addadmins(data["superadmin"],data["o2"],3,7,"a1_o2")
    # check_add_methods.check_addadmins(data["superadmin"],data["o2"],3,8,"a2_o2")

    # test_addprojects(data["a1_o1"],"a1_o1",data,2)
    # test_addprojects(data["a2_o1"],"a2_o1",data,2)
    # test_addprojects(data["a1_o2"],"a1_o2",data,2)
    # test_addprojects(data["a2_o2"],"a2_o2",data,2)
    # time.sleep(sleep_time)

    # check_add_methods.check_addprojects(data["a1_o1"],2,9,"p1_a1_o1")
    # check_add_methods.check_addprojects(data["a1_o1"],2,10,"p2_a1_o1")
    # check_add_methods.check_addprojects(data["a2_o1"],2,11,"p1_a2_o1")
    # check_add_methods.check_addprojects(data["a2_o1"],2,12,"p2_a2_o1")
    # check_add_methods.check_addprojects(data["a1_o2"],2,13,"p1_a1_o2")
    # check_add_methods.check_addprojects(data["a1_o2"],2,14,"p2_a1_o2")
    # check_add_methods.check_addprojects(data["a2_o2"],2,15,"p1_a2_o2")
    # check_add_methods.check_addprojects(data["a2_o2"],2,16,"p2_a2_o2")
    
    # test_addusers(data["a1_o1"],"a1_o1",data,2)
    # test_addusers(data["a2_o1"],"a2_o1",data,2)
    # test_addusers(data["a1_o2"],"a1_o2",data,2)
    # test_addusers(data["a2_o2"],"a2_o2",data,2)
    # time.sleep(sleep_time)

    # check_add_methods.check_adduser(data["a1_o1"],data["o1"],4,17,"u1_a1_o1")
    # check_add_methods.check_adduser(data["a1_o1"],data["o1"],4,18,"u2_a1_o1")
    # check_add_methods.check_adduser(data["a2_o1"],data["o1"],4,19,"u1_a2_o1")
    # check_add_methods.check_adduser(data["a2_o1"],data["o1"],4,20,"u2_a2_o1")
    # check_add_methods.check_adduser(data["a1_o2"],data["o2"],4,21,"u1_a1_o2")
    # check_add_methods.check_adduser(data["a1_o2"],data["o2"],4,22,"u2_a1_o2")
    # check_add_methods.check_adduser(data["a2_o2"],data["o2"],4,23,"u1_a2_o2")
    # check_add_methods.check_adduser(data["a2_o2"],data["o2"],4,24,"u2_a2_o2")

    # giveuseraccess(data["a1_o1"],"project",data["p1_a1_o1"],data["u1_a1_o1"])
    # giveuseraccess(data["a1_o1"],"project",data["p2_a1_o1"],data["u1_a1_o1"])
    # giveuseraccess(data["a1_o1"],"project",data["p1_a1_o1"],data["u1_a2_o1"])    
    # giveuseraccess(data["a2_o1"],"project",data["p1_a2_o1"],data["u1_a1_o1"])

    # # USER ACCESS IN PROJECTS IS POSSIBLE WITHIN SAME ORGANISATION       
    # giveuseraccess(data["a1_o2"],"project",data["p1_a1_o2"],data["u1_a1_o1"])
    # giveuseraccess(data["a1_o1"],"project",data["p1_a1_o1"],data["u1_a1_o2"]) 
    # # USER ACCESS IN PROJECTS IS POSSIBLE WITHIN SAME ORGANISATION       
    # time.sleep(sleep_time)

    # # EXPECTED BUT INCORRECT METHODS
    # check_add_methods.check_usersaccessinproject([data["u1_a1_o1"],data["u1_a2_o1"],data["u1_a1_o2"]],data["a1_o1"],data["p1_a1_o1"],25)
    # check_add_methods.check_usersaccessinproject([data["u1_a1_o1"]],data["a1_o2"],data["p1_a1_o2"],26)
    # check_add_methods.check_usersaccessinproject([data["u1_a1_o1"]],data["a2_o1"],data["p1_a2_o1"],27)
    # check_add_methods.check_usersaccessinproject([data["u1_a1_o1"]],data["a1_o1"],data["p2_a1_o1"],28)
    # tn = 28
    # check_add_methods.check_projectsassignedtouser([data["p1_a1_o1"],data["p2_a1_o1"],data["p1_a2_o1"],data["p1_a1_o2"]],data["u1_a1_o1"],tn);tn+=1
    # check_add_methods.check_projectsassignedtouser([data["p1_a1_o1"]],data["u1_a1_o2"],tn);tn+=1
    # check_add_methods.check_projectsassignedtouser([data["p1_a1_o1"]],data["u1_a2_o1"],tn);tn+=1
     
    # # CORRECT METHODS
    # check_add_methods.check_usersaccessinproject([data["u1_a1_o1"],data["u1_a2_o1"]],data["a1_o1"],data["p1_a1_o1"],25)
    # check_add_methods.check_usersaccessinproject([data["u1_a1_o1"]],data["a2_o1"],data["p1_a2_o1"],26)
    # check_add_methods.check_usersaccessinproject([data["u1_a1_o1"]],data["a1_o1"],data["p2_a1_o1"],27)

    # tn = 27
    # check_add_methods.check_projectsassignedtouser([data["p1_a1_o1"],data["p2_a1_o1"],data["p1_a2_o1"]],data["u1_a1_o1"],tn);tn+=1
    # check_add_methods.check_projectsassignedtouser([data["p1_a1_o1"]],data["u1_a1_o2"],tn);tn+=1
    # check_add_methods.check_projectsassignedtouser([data["p1_a1_o1"]],data["u1_a2_o1"],tn);tn+=1

    tn = 29
    # giveuseraccess(data["a2_o1"],"project",data["p1_a2_o1"],data["u2_a1_o1"])
    # time.sleep(sleep_time)
    # check_add_methods.check_projectsassignedtouser([data["p1_a2_o1"]],data["u2_a1_o1"],tn);tn+=1
    # check_add_methods.check_usersaccessinproject([data["u1_a1_o1"],data["u2_a1_o1"]],data["a2_o1"],data["p1_a2_o1"],tn);tn+=1
# test_add_methods1()
def test_get_methods():
    data = getdata()

    # getformsinproject(data["admin1_org1"],data["project1_admin1_org1"])

    # getassesorsinform(data["user1_admin1_org1"],data["form1_project1_admin1_org1"])

    # getteamsinform(data["user1_admin1_org1"],data["form1_project1_admin1_org1"])

    # getassesorsinteam(data["user1_admin1_org1"],data["team1_project1_admin1_org1"])
    # getformsinteam(data["user1_admin1_org1"],data["team1_project1_admin1_org1"])

    # getformsinteam(data["user1_admin1_org1"],data["team2_project1_admin1_org1"])
    # getassesorsinteam(data["user1_admin1_org1"],data["team2_project1_admin1_org1"])

    # getadminsinorganization(data["superadmin"],data["org1"])
    # getadminsinorganization(data["superadmin"],data["org2"])
    # getadminsinorganization(data["admin1_org1"],data["org1"])
    # getadminsinorganization("vedbsb",data["org1"])

    # getprojectsinorganization(data["superadmin"],data["org2"])
    # getprojectsinorganization(data["superadmin"],data["org1"])
    
    # getusersinorganization(data["superadmin"],data["org2"])
    # getusersinorganization(data["superadmin"],data["org1"])
    
    # getorganizationsofuser(data["superadmin"])
    # getorganizationsofuser(data["admin1_org1"])

    # getprojectsofuser(data["superadmin"])  
    # getprojectsofuser(data["admin1_org1"])
    # getprojectsofuser(data["admin2_org1"])    
    # getprojectsofuser(data["user1_admin1_org1"])
    # getprojectsofuser(data["user2_admin1_org1"])

    # getformsofuser(data["superadmin"])
    # getformsofuser(data["admin1_org1"])
    # getformsofuser(data["user2_admin2_org1"])

    # giveuseraccess(data["user1_admin1_org1"],"form","b35b5b1e86304c648d5c45bb4edfbc83",data["user2_admin2_org1"])

    # getformsofuser(data["user1_admin1_org1"])
    # getformsofuser(data["user2_admin1_org1"])
    # getformsofuser(data["user1_admin2_org1"])    
    # getformsofuser(data["user2_admin2_org1"])
    # getprojectsofuser(data["user2_admin2_org1"])

    # # CORRECT METHODS
    # getusersinform(data["a1_o1"],data["f1_a"])
    # getusersinform(data["u1_a1_o1"],data["f1_c"])
    # getusersinform(data["a1_o1"],data["f1_x"])
    # getusersinform(data["u1_a1_o1"],data["f1_y"])

    # # INCORRECT METHODS
    # getusersinform(data["a1_o1"],data["f1_c"])    
    # getusersinform(data["a1_o1"],data["f1_y"])
    # # This admin has no permission in f1_c ans f1_y even when these forms were created by its user but created in any other project than of admins's projects
    
    # getformsinproject(data["admin1_org1"],data["project1_admin1_org1"])
    # getformsinproject(data["admin1_org1"],data["project2_admin1_org1"])
    # getformsinproject(data["admin2_org1"],data["project1_admin2_org1"])
    # getformsinproject(data["admin2_org1"],data["project2_admin2_org1"])

    # getusersinproject(data["admin1_org1"],data["project1_admin1_org1"])
    # getusersinproject(data["admin1_org1"],data["project2_admin1_org1"])
    # getusersinproject(data["admin2_org1"],data["project1_admin2_org1"])
    # getusersinproject(data["admin2_org1"],data["project2_admin2_org1"])

    # getassesorsinproject(data["admin1_org1"],data["project1_admin1_org1"])
    # getassesorsinproject(data["admin1_org1"],data["project2_admin1_org1"])
    # getassesorsinproject(data["admin2_org1"],data["project1_admin2_org1"])
    # getassesorsinproject(data["admin2_org1"],data["project2_admin2_org1"])

    # getteamsinproject(data["admin1_org1"],data["project1_admin1_org1"])
    # getteamsinproject(data["admin1_org1"],data["project2_admin1_org1"])
    # getteamsinproject(data["admin2_org1"],data["project1_admin2_org1"])
    # getteamsinproject(data["admin2_org1"],data["project2_admin2_org1"])

    # getassesorsinform(data["admin1_org1"],data["form1_project1_admin1_org1"])

    # getformsofassesor(data["admin1_org1"],data["assesor1_project1_admin1_org1"])

    # getassesorsinform(data["user1_admin1_org1"],data["form1_project1_admin1_org1"])

    # getformsofassesor(data["user1_admin1_org1"],data["assesor1_project1_admin1_org1"])
# test_get_methods()

# test_add_methods1()
def test_log_action():
    fid = "15151456845357301"
    logactionfilter("319424f5b8524ebe8188c2d40217c48c")
"""
import names
import  random
import csv
import datetime
import pandas as pd
from flask import Flask, jsonify, render_template, request,send_file
app=Flask(__name__,template_folder='template') 
@app.route('/')
def index():
    return render_template("no_of_user.html")
@app.route("/", methods=["GET" ,"POST"])
def dumval():
    if request.method=="POST":
        num=int(request.form.get("id1"))
        Student_dict=[]
        columns = ['ID','NAME','EMAIL','PHONENUMBER','PROFESSION','SALARY','DATE_OF_JOINING','YEAR_OF_EXPERIENCE']
        for i in range(num):
                        a=(names.get_first_name())
                        b=(names.get_last_name())
                        fullname=(a+" "+b)
                        emailid=a+b+"@gmail.com"
                        ID=i+1
                        random_number = random.randint(9000000000, 10000000000)
                        salary=random.randrange(25000,75000,100)
                        start_date = datetime.date(2000, 1, 1)
                        end_date = datetime.date(2022, 1, 1)
                        time_between_dates = end_date - start_date
                        days_between_dates = time_between_dates.days
                        random_number_of_days = random.randrange(days_between_dates)
                        random_date = start_date + datetime.timedelta(days=random_number_of_days)
                        experience=end_date.year-random_date.year
                        profession=["Web Developer ","Physician",  "Auditor" ,"Health Educator"  ,"RestaurantManager" ,
                        "Executive Director"  ,"Front Desk Coordinator" ,"Clerk" "Paramedic", "IT Support Staff",
                        "Laboratory Technician", "Software Engineer", "Webmaster" ,"Business Broker" ,"Software  Developer",  "Mobile Developer"]
                        Prof=(random.choice(profession))
                        Student_dict+=[{"ID":ID,'NAME':fullname,'EMAIL': emailid ,'PHONENUMBER':random_number ,
                        'PROFESSION':Prof,'SALARY':salary ,'DATE_OF_JOINING':random_date,'YEAR_OF_EXPERIENCE':experience}]
                        print(Student_dict)
                        try:
                            with open("students.csv", 'w',newline='') as csvfile:
                                writer = csv.DictWriter(csvfile, fieldnames=columns)
                                writer.writeheader()
                                for key in Student_dict:
                                    writer.writerow(key)
                        except IOError:
                            print("I/O error")
    
                        data = pd.read_csv('students.csv')
        return render_template('userdata.html', tables=[data.to_html()])
@app.route("/download" ,methods=["GET","POST"])
def download():
        if request.method=="POST":
            return send_file('students.csv',
                            mimetype='text/csv',
                            attachment_filename='dummy.csv',
                            as_attachment=True)
    

    
if(__name__)=="__main__":
        app.run(debug=True)

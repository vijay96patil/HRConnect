import json
from my_utils.csv import HandleCSV
from flask import Flask
app = Flask(__name__)

#filename = "employee.csv"

@app.route("/api/task_one")
def get_salary():
    filename = "employee.csv"
    obj = HandleCSV()

    lst= HandleCSV.get_data()        # we get list of dictionary

    salary ={}
    for emp in lst:
        for i,j in emp.items():
            if int(emp["SALARY"]) > 9000:
                name=emp["FIRST_NAME"]+" "+emp["LAST_NAME"]
                    # print(f"name:{name}")
                email = emp["EMAIL"]
                    # print(f"email : {email}")
                phone_number= emp["PHONE_NUMBER"]
                    # print(f"phone number : {phone_number}")
                salary.update({"name":name})
                salary.update({"email":email})
                salary.update({"phone_number":phone_number})
    return salary


if __name__ == "__main__":
    app.run(debug=True)
    """creating object of a class HandleCSV """





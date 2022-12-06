from my_utils.csv import HandleCSV
from datetime import datetime

if __name__ == "__main__":
    print("name")

    obj = HandleCSV()
    lst_ = HandleCSV.get_data()
    dic={}
    for emp in lst_:
        if 30 < int(emp["DEPARTMENT_ID"]) < 110 and int(emp["SALARY"]) > 4200:
            f_name = emp["FIRST_NAME"]+" "+emp["LAST_NAME"]
            # print(f"f_name:{f_name}")
            hire_date= emp["HIRE_DATE"]
            date_ = datetime.strptime(hire_date,"%d-%b-%y")
            result = str(date_.date())
            # print(result)
            dic[result] = [f_name]
            dic.update({result:[f_name]})
    print(dic)






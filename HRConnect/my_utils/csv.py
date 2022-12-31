import csv
from typing import List,Dict

class HandleCSV:
    filename = "employee.csv"

    @classmethod
    def get_data(cls)-> List[Dict]:
        """classmethod returns csv to list of dictonary format"""
        lst = []
        with open(cls.filename, mode='r') as f:
            data = csv.DictReader(f)
            for line in data:
                lst.append(line)
            return(lst)

    @classmethod
    def read_line_by_line(cls)
        with open(cls.filename) as foo:
            for line in csv.DictReader(foo):
                yield line


    @classmethod
    def convert(cls):
        dic={}
        with open(cls.filename) as bar:
            for line in bar:
                key,val = line.split()
                dic[key]=val
            print(dic)


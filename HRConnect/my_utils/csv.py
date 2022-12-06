import csv
class HandleCSV:
    filename = "employee.csv"

    @classmethod
    def get_data(cls):
        """classmethod returns csv to list of dictonary format"""
        lst = []
        with open(cls.filename, mode='r') as f:
            data = csv.DictReader(f)
            for row in data:
                lst.append(dict(row))
            return(lst)

    @classmethod
    def read_entire_csv(cls):
        with open(cls.filename,"r") as foo:
            return foo.readlines()


    @classmethod
    def read_csv_line_by_line(cls):
        with open(cls.filename) as bar:
            yield bar.readline()

    @classmethod
    def convert(cls):
        dic={}
        with open(cls.filename) as bar:
            for line in bar:
                key,val = line.split()
                dic[key]=val
            print(dic)


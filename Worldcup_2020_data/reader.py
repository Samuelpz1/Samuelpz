import csv

def get_data (path):
    with open(path,"r") as csvfile:
        reader = csv.reader(csvfile, delimiter = ",")
        heaader = next(reader)
        data = []

        for row in reader:
            iterable = zip(heaader,row)
            data_dict = {key:value for key,value in iterable}
            data.append(data_dict)
        return data



if __name__=="__main__":
    data = get_data("./data.csv")


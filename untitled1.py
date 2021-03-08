

# my_dict=[{"name":"ali", "id":5644688664},
#           {"name":"hamid", "id":321464877},
#           {"name":"jafar", "id":568874452}]

# for i in my_dict:
#         if i in my_dict:
#           k= my_dict.get(input("enter a name: "))
#           print(k)





import csv

my_dict=[{"name":"ali", "id":5644688664}, 
         {"name":"hamid", "id":321464877}, 
         {"name":"jafar", "id":568874452}]

filenames = "new.csv"
with open("C:/Users/somay/.spyder-py3/new.csv", "r") as new_csv_file:
     reader = csv.DictReader(new_csv_file)
     for row in reader:
               list_of_column_names = [] 
               list_of_column_names.append(row)  
               break
    



     with open("new.csv", "w") as new_csv_file:
             fields = ["name", "id"]
             writer = csv.DictWriter(new_csv_file, fieldnames=fields,delimiter=",")
             writer.writeheader()
             writer.writerow({"name":"ali", "id":5644688664})
             writer.writerow({"name":"hamid", "id":321464877})
             writer.writerow( {"name":"jafar", "id":568874452})
           








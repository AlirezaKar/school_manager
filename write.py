import csv
import main 


# with open('db.csv', 'w', newline='') as csvfile:
#     fieldnames = ['class_name', 'class_code', 'school_name', 'teacher_name']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#     writer.writeheader()
#     writer.writerow({'class_name':class_room_1.name })
#     writer.writerow({'class_code': class_room_1.code })
#     writer.writerow({'school_name':school_1.name})
#     writer.writerow({ 'teacher_name':alireza_kalaie.name})

##########################

# with open('db.csv', newline='') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
       

##########################

# line1 = {
#         'class_name':main.class_room_1.name, 
#          'class_code':main.class_room_1.code, 
#          'school_name': main.salam_1.name,
#          'teacher_name':main.alireza_kalaie.name
#          }
# fields1 = ['class_name', 'class_code', 'school_name', 'teacher_name']

# file_name = 'db.csv'

# with open(file_name, 'w') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=fields1)
#     # writer.writeheader()
#     writer.writerows(line1)

##########################

# file = open('db.csv', 'r+')
# file.write(f"class_name:{main.class_room_1.name},class_code:{main.class_room_1.code}, school_name: {main.salam_1.name}, teacher_name:{main.alireza_kalaie.name} \n")


# print(file.read())

##########################

mydict = {
        'class_name':main.class_room_1.name, 
         'class_code':main.class_room_1.code, 
         'school_name': main.salam_1.name,
         'teacher_name':main.alireza_kalaie.name
}
# import pdb; pdb.set_trace() 

with open('db.csv', 'w') as csv_file:
    fieldnames = ['class_name', 'class_code', 'school_name', 'teacher_name']
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter='\t')
    csv_writer.writeheader()
    # import pdb; pdb.set_trace() 
    for line in mydict.values():
        csv_writer.writerow(line)         # this is the problem


##########################
import csv
print("CSV FILE for address book")
book=[['Name','Address','Mobile','Email'],
      ['Bhumi','Jaipur','9783676757','bhumi@gmail.com'],
      ['Chetan','Dhaulpur','3969798978','chetan@gmail.com'],
      ['Mahak','Jhodhpur','3756699797','mahak@gmail.com']]

with open('book.csv','w')as file:
    writer=csv.writer(file)
    for row in book:
        writer.writerow(row)

with open('book.csv','r')as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)
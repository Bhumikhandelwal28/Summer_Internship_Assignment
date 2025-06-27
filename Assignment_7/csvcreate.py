import csv
print("CSV FILE ")
book=[['Date','Product','Price','Quantity','Total'],
[2024-1-1,'Apple',1.2,10],
[2024-1-1,'Banana',0.5,20],
[2024-1-2,'Apple',1.2,15],
[2024-1-2,'Banana',0.5,],
[2024-1-3,'Orange',1.0,5],
['','Orange',1.0,10],
[2024-1-4,'Apple',1.3,8],
[2024-1-4,'Banana',0.6,12],
[2024-1-5,'',0.8,10]
]

with open('new.csv','w')as file:
    writer=csv.writer(file)
    for row in book:
        writer.writerow(row)


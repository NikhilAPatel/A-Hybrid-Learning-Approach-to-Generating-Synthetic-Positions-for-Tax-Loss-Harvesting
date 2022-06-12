import csv
rows = []
with open("Data/sptm-comp-june-8.csv", 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        rows.append(row)

out = "{"


for i in range(0, len(rows)):
    row = rows[i]
    if(i<len(rows)-1):
        out+="\'"+row[0]+"\': "+row[1]+","
    else:
        out+="\'"+row[0]+"\': "+row[1]

out+="}"


print(out)

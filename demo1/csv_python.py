import csv

with open("test.csv", 'w') as f:
    writer = csv.writer(f)
    H=['Name', 'Call', 'Profession', 'Email']
    writer.writerow(H)
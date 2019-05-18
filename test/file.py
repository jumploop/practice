with open('cafe.txt', 'w', encoding='utf-8') as f:
    f.write('cafe')
with open('cafe.txt', encoding='utf-8') as f:
    msg = f.read()
    print(msg)
import csv

with open('eggs.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

import happybase as hb
import csv

conn = hb.Connection()

table = conn.table('powers')

with open('input.csv') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',')
	for row in spamreader:
		row_key = row[0]
		row_data = {}
		row_data[b'personal:hero'] = str.encode(row[1])
		row_data[b'personal:power'] = str.encode(row[2])
		row_data[b'professional:name'] = str.encode(row[3])
		row_data[b'professional:xp'] = str.encode(row[4])
		row_data[b'custom:color'] = str.encode(row[5])
		#print (row_data)

		table.put(str.encode(row_key), row_data)
		#print(', '.join(row))

conn.close()

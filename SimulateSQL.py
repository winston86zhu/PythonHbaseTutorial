import happybase as hb

conn = hb.Connection()
table = conn.table('powers')
columns = (b'personal:power', b'custom:color', b'professional:name')
# DON'T CHANGE THE PRINT FORMAT, WHICH IS THE OUTPUT
# OR YOU WON'T RECEIVE POINTS FROM THE GRADER
for key, data in table.scan(columns=columns, include_timestamp=False):
	p_color = data[b'custom:color']
	p_name = data[b'professional:name']
	p_power = data[b'personal:power']
	for key2, data2 in table.scan(columns=columns, include_timestamp=False):
		p2_color = data2[b'custom:color']
		p2_name = data2[b'professional:name']
		p2_power = data2[b'personal:power']
		if p2_color == p_color and p_name != p2_name:
			print('{}, {}, {}, {}, {}'.format(p_name, p_power, p2_name, p2_power, p2_color))



# color = ???
# name = ???
# power = ???
#
# color1 = ???
# name1 = ???
# power1 = ???
#
# print('{}, {}, {}, {}, {}'.format(name, power, name1, power1, color))



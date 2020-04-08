import happybase as hb

conn = hb.Connection()


cf1 = {
	'personal': dict(),
	'professional': dict(),
	'custom': dict()
}

cf2 = {
	'nutrition': dict(),
	'taste': dict()
}

conn.create_table('powers', cf1)
conn.create_table('food', cf2)

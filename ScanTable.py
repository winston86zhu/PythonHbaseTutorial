import happybase as hb

# DON'T CHANGE THE PRINT FORMAT, WHICH IS THE OUTPUT
# OR YOU WON'T RECEIVE POINTS FROM THE GRADER
conn = hb.Connection()
table = conn.table('powers')
columns = (b'professional:xp', b'personal:power', b'personal:hero', b'custom:color', b'professional:name')

#Found: row9, {'custom:color': ('green', 1586311833084), 'personal:power':
# ('steal', 1586311833084), 'professional:xp': ('67', 1586311833084), 'personal:hero': ('yes', 1586311833084)}
for key, data in table.scan(columns=columns, include_timestamp=True):
    print('Found: {}, {}'.format(key, data))


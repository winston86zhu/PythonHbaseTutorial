import happybase as hb

conn = hb.Connection()
table = conn.table('powers')
# DON'T CHANGE THE PRINT FORMAT, WHICH IS THE OUTPUT
# OR YOU WON'T RECEIVE POINTS FROM THE GRADER
row = table.row(b'row1')

hero = row[b'personal:hero']
power = row[b'personal:power']
name = row[b'professional:name']
xp = row[b'professional:xp']
color = row[b'custom:color']

print('hero: {}, power: {}, name: {}, xp: {}, color: {}'.format(hero, power, name, xp, color))

row19 = table.row(b'row19')

hero = row19[b'personal:hero']
color = row19[b'custom:color']

print('hero: {}, color: {}'.format(hero, color))

hero = row[b'personal:hero']
name = row[b'professional:name']
color = row[b'custom:color']
print('hero: {}, name: {}, color: {}'.format(hero, name, color))
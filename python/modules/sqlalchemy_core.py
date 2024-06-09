import sqlalchemy as sql_a

engine = sql_a.create_engine('sqlite:///:memory')

metadata_obj = sql_a.MetaData() # (schema='test') optional
user = sql_a.Table(
	'user',
	metadata_obj,
	sql_a.Column('user_id', sql_a.Integer, primary_key=True),
	sql_a.Column('user_name', sql_a.String(40), nullable=False),
	sql_a.Column('email_address', sql_a.String(60)),
	sql_a.Column('nickname', sql_a.String(50), nullable=False)
)

user_prefs = sql_a.Table(
	'user_prefs',
	metadata_obj,
	sql_a.Column('pref_id', sql_a.Integer, primary_key=True),
	sql_a.Column('user_id', sql_a.Integer, sql_a.ForeignKey('user.user_id'), nullable=False),
	sql_a.Column('pref_name', sql_a.String(40), nullable=False),
	sql_a.Column('pref_value', sql_a.String(100))
)

for table in metadata_obj.sorted_tables:
	print(table)
	
print(user.primary_key)
#print(user_prefs.constraints)
print('-' * 30 + '\n')

metadata_obj.create_all(engine)
# inserting into table
sql_insert = sql_a.text("insert into user values(1, 'juliana', 'ju@email.com', 'ju')")
with engine.begin() as conn:
   conn.execute(sql_insert)

# executing statement sql
sql = sql_a.text('select * from user')
# result = engine.execute(sql) deprecated
with engine.begin() as conn:
	for data in conn.execute(sql):
		print(data)
   
#for row in result:
#	print(row)



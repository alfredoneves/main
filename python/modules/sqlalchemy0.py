from sqlalchemy.orm import declarative_base, relationship, Session
import sqlalchemy as sql_a

Base = declarative_base()	# used to create entities and it's the model structure to map

class User(Base):
	__tablename__ = 'user_account'	# table name
	
	# creating atributes
	id = sql_a.Column(sql_a.Integer, primary_key=True)	# creates column
	name = sql_a.Column(sql_a.String)	# atention to sql_a in the argument
	full_name = sql_a.Column(sql_a.String)

	# defining relationship between the tables
	# back_populates receives the name of the variable of the other class
	address = relationship('Address', back_populates='user', cascade='all, delete-orphan')
	
	# representation of class when returned in the SQL query
	def __repr__(self):
		return f'User(id={self.id}, name={self.name}, full_name={self.full_name})'
		
class Address(Base):
	__tablename__ = 'address'
	id = sql_a.Column(sql_a.Integer, primary_key=True, autoincrement=True)
	email_address = sql_a.Column(sql_a.String(30), nullable=False)
	user_id = sql_a.Column(sql_a.Integer, sql_a.ForeignKey('user_account.id'), nullable=False)

	# defining relationship between the tables
	user = relationship('User', back_populates='address')

	# creating representation for the class
	def __repr__(self):
		return f'Address(id={self.id}, email_address={self.email_address})'

def return_query(stmt):
	print(f'\nQuery: {stmt}')
	for data in session.scalars(stmt):
		print(data)
		
print('User table:')
print(User.__tablename__)

print('Address table:')
print(Address.__tablename__)
	
# database connection
engine = sql_a.create_engine('sqlite://')

# creating the classes as tables in the database
Base.metadata.create_all(engine)

insp = sql_a.inspect(engine)
print(insp.has_table('user_account'))	# verifies if a table exists
print(insp.get_table_names())
print(insp.default_schema_name)
print('-' * 30)

with Session(engine) as session:
	juliana = User(
		name='juliana',
		full_name='Juliana Silva',
		address=[Address(email_address='julianas@mail.com')]
	)
	
	sandy = User(
		name='sandy',
		full_name='Sandy Júnior',
		address=[Address(email_address='sandy@email.com'), Address(email_address='sandyjr@email.com')]
	)
	
	patrick = User(name='patrick', full_name='Patrick Santos')

	session.add_all([juliana, sandy, patrick])	# sends data to the database (persistence)
	session.commit()
	

		
stmt = sql_a.select(User).where(User.name.in_(['juliana', 'sandy']))
return_query(stmt)

stmt = sql_a.select(Address).where(Address.user_id.in_([1,2]))
return_query(stmt)

stmt = sql_a.select(User).order_by(User.full_name.desc())
return_query(stmt)

# scalars takes the first result, now with a join I'm going to use another method
stmt_join = sql_a.select(User.full_name, Address.email_address).join_from(Address, User)	# inner join
connection = engine.connect()
results = connection.execute(stmt_join).fetchall()
print(f'\nQuery: {stmt_join}')
for result in results:
	print(result)

# counting the number of lines in a table
stmt = sql_a.select(sql_a.func.count('*')).select_from(User)
return_query(stmt)

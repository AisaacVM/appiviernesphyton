#Line Coments    

from sqlalchemy import create_engine, event 
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Engine

#Conection to BD
'''StatUs = 1.82
actually= True
profesionUs= 'NONE'
age = 18
'''

userName = 'root'
userPassword = '' 
dataBaseName='gestionbd'
conetionport = '3306'
servconect = 'localhost'

connectionToDB= f'mysql+ mysqlconnector://{userName}:{userPassword}@{servconect}:{conetionport}/{dataBaseName}'

print(connectionToDB)
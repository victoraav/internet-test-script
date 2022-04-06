import speedtest
import math
import mysql.connector
from datetime import datetime

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'net_test'
    )

cursor = conexao.cursor()
print(conexao)

st = speedtest.Speedtest()

d = st.download()
dformatado = str(math.floor(d))[0:3]

u = st.upload()
uformatado = str(math.floor(u))[0:3]


dia = datetime.today().strftime('%Y-%m-%d')
hora = datetime.today().strftime('%H:%M')

cursor.execute(f'INSERT INTO dailytest (download,upload,data,hora) VALUES ("{dformatado}","{uformatado}","{dia}","{hora}")')
conexao.commit()
print("Adicionado ao banco")




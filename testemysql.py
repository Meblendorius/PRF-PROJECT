import mysql.connector
con = mysql.connector.connect(host='localhost',database='Digital',user='thiago',password='Tmysql@4581')
if con.is_connected():
    db_info = con.get_server_info()
    print("Conectado ao servidor MySQL versão ",db_info)
    cursor = con.cursor()

    cursor.execute("select * from func;")
    linha = cursor.fetchall()
    for i in linha:
        print(i[6])
if con.is_connected():
    cursor.close()
    con.close()
    print("Conexão ao MySQL foi encerrada")
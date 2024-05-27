import mysql.connector

# dados do servidor sql
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Tiago1945.",
    database = "Tricornio"
)

mycursor = mydb.cursor()

# Dados que se pretende inserir
sql = "INSERT INTO Cliente (NIF, Nome, Morada, Telefone, Email) VALUES (%s, %s, %s, %s, %s)"
val = [("179825878", "António Silva", "Rua Eusébio, 66, Lisboa", "934457689", "otamendinobolso@benfica.pt"),
       ("273634538", "Ricardo Quaresma", "Rua da Trivela, 7 , Porto", "968033543", "triveladourada7@gmail.com")
    ]

sql2 = "INSERT INTO Arma (idArma, N_licença, Data_Fabrico, Modelo, N_de_Munições, Id_Detetive) VALUES (%s, %s, %s, %s, %s, %s)"
val2 = [("11", "345654", "2021-03-05 16:02:47", "Glock 22", "17" , "11"),    
       ("12", "123679", "2001-09-11 08:46:00", "Dandelion 21", "12" , "12")
    ]


mycursor.executemany(sql, val)
mycursor.executemany(sql2, val2)
mydb.commit()
 
print(mycursor.rowcount, "detalhes inseridos")
 
# desconectar do servidor
mydb.close()


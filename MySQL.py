import mysql.connector
from tkinter import messagebox


def Save_Data_MySql(B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R):
    try:
        mydb = mysql.connector.connect(host='localhost', user='root', password="992922")
        mycursor=mydb.cursor()
        print("Connection stablished!")
    except:
        messagebox.showerror("Connection", "Database connection not stablished!!")
    try:
        print(B)
        print(C)
        print(D)
        print(E)
        print(F)
        print(G)
        print(H)
        print(I)
        print(J)
        print(K)
        print(L)
        print(M)
        print(N)
        print(O)
        print(P)
        print(Q)
        print(R)
    except:
        pass


Save_Data_MySql("mr unknown","08/08/2023","1979","44","1","1","233","233","1","1","233","1","233.0","0","2","1","0")


# Last : 16:24 Part-4
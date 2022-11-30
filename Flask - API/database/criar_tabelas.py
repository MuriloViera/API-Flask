import sqlite3

try:
    conn = sqlite3.connect('database/data.db')
    conn.execute('''
        CREATE TABLE tb_cliente (
            id INTEGER PRIMARY KEY NOT NULL,
            nome TEXT NOT NULL,
            marca TEXT NOT NULL,
            ano TEXT NOT NULL
        );
    ''')
    conn.execute(
        '''
        INSERT INTO `tb_cliente` (`id`,`nome`,`marca`,`ano`)
        VALUES
            (1,"XC60","Volvo","2007"),
            (2,"Elantra","Hyundai","2011"),
            (3,"Mustang","Ford","1962"),
            (4,"March","Nissan","2011");    
        '''
    )
    conn.commit()
    print("Operacao realizada com sucesso!")
except:
    print("ERRO")
finally:
    conn.close()

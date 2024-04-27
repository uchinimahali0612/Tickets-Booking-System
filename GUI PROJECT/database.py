import sqlite3

def create_table():
    conn = sqlite3.connect('Reservation.db')
    cursor = conn.cursor()

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS Tickets (
                   ticket_id TEXT PRIMARY KEY,
                   movie_name TEXT,
                   ticket_quantity INTEGER,
                   ticket_price INTEGER)''' )
    conn.commit()
    conn.close()


def insert_Tickets():
    conn =sqlite3.connect('Reservation.db')
    cursor =conn.cursor()

    Tickets_data=[
        ('132567','Chennai Express',130,50),
        ('134568','Dhoom3',120,40),
        ('167399','12th Fail',140,60),
        ('146893','Manikarnika',150,70),
        ('122783','YHJD',110,65),
        ('124483', 'Jab We Met', 120, 23),
         ('183483', 'Kantara', 170, 25),
        ('137809', 'Kabhi Khushi Kabhi Gam', 190, 32),
        ('136288', 'The Spiderman', 66, 40),
        ('109372', 'Animal', 89, 59),
        ('137283', 'Leo', 30, 57),
        ('137y89', 'The kerela story', 188, 70)
    ]

    cursor.executemany('INSERT OR IGNORE INTO Tickets (ticket_id, movie_name, ticket_quantity, ticket_price) VALUES (?, ?, ?, ?)', Tickets_data)

    conn.commit()
    conn.close()

def get_tickets():
    conn= sqlite3.connect('Reservation.db')
    cursor =conn.cursor()
    cursor.execute('SELECT * FROM Tickets')
    tickets=cursor.fetchall()
    conn.close()

    return tickets

def update_quantity(id,reserved_quantity):
    conn = sqlite3.connect('Reservation.db')
    cursor =conn.cursor()
    cursor.execute('UPDATE tickets SET ticket_quantity = ticket_quantity - ? WHERE ticket_id=?',(reserved_quantity,id))
    conn.commit()
    conn.close() 

create_table()
insert_Tickets()

import psycopg2 as ps  ## importing MODUL ADAPTOR to work with DB PostgreSQL

con=ps.connect(dbname='postgres', user='postgres',password='(enter you password)')  ## connect to DB
cur = con.cursor() ## connecting cursor

## Create table

def create_table():
    cur.execute('DROP TABLE IF EXISTS MyDiary')
    cur.execute('CREATE TABLE MyDiary (diary_id serial PRIMARY KEY, p_fullname varchar, mobile varchar)')
    con.commit()
    print('Your Diary is created!')

## select table

def select_table():
    try:
        cur.execute('SELECT * FROM MyDiary')
        fill=cur.fetchall()
        for i in fill:
            print(i)
    except (Exception, ps.DatabaseError) as error:
        print(error)
   

## Update table with full name and id / mobile and id 

def update_table():
    select, id = input('Enter your attributes separated(FullName  ID No.):  ').split()
    try:  
        cur.execute('UPDATE MyDiary SET p_fullname = %s WHERE diary_id = %s', (select,id))
        con.commit()
        print('Your Diary is updated successfully! ')
    except (Exception, ps.DatabaseError) as error:
        print(error)  

def update_table_num():
    select, id = input('Enter your attributes separated(Mobile No.  ID No.):  ').split()
    try:
        cur.execute('UPDATE MyDiary SET mobile = %s WHERE diary_id = %s', (select,id))
        con.commit()
        print('Your Diary is updated successfully! ')
    except (Exception, ps.DatabaseError) as error:
        print(error)  
## Insert table

def insert_table():
    name, mobile = input('Enter your attributes separated (FullName Mobile):  ').split()
    try:
        cur.execute('INSERT INTO MyDiary (p_fullname,mobile) VALUES (%s,%s)', (name,mobile))
        con.commit()
        print('Information is inserted')
    except (Exception, ps.DatabaseError) as error:
        print(error)

## delete table

def delete_table():
    diary_id = input('Enter your attributes (ID No.):  ')
    cur.execute('DELETE FROM MyDiary WHERE diary_id = %s', (diary_id))
    con.commit()
    print('Your Diary ID is deleted')


print("""

    If you want to CREATE a table choose a button C
    If you want to INSERT a table choose a button I
    If you want to UPDATE a table choose a button U
    If you want to UPDATE MOBILE choose a button M
    If you want to SELECT a table choose a button S
    If you want to DELETE a table choose a button D
    If you want to QUIT a table choose a button Q

""")



while True:
    select = input('Enter your choice  ')
    if select.lower() == 'c':
        create_table()
    elif select.lower() == 'i':
        insert_table()
    elif select.lower() == 'u':
        update_table()
    elif select.lower() == 'm':
        update_table_num()
    elif select.lower() == 's':
        select_table()
    elif select.lower() == 'd':
        delete_table()
    elif select.lower() == 'q':
        print('Thank you for using our APP!')
        cur.close()
        con.close()
        break

    
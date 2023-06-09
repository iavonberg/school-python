import sqlite3

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE example(Language VARCHAR, Version REAL, Skill TEXT)")

# create_table()

def enter_data():
    c.execute("INSERT INTO example VALUES('Python', 2.7, 'Beginner')")
    c.execute("INSERT INTO example VALUES('Python', 3.3, 'Intermediate')")
    c.execute("INSERT INTO example VALUES('Python', 3.4, 'Expert')")
    conn.commit()

# enter_data()

def enter_dynamic_data():
    lang = input('What language? ')
    version = float(input('What version? '))
    skill = input('What is your skill level? ')

    c.execute("INSERT INTO example (Language, Version, Skill) VALUES (?,?,?)", (lang, version, skill))
    conn.commit()

# enter_dynamic_data()

# def read_from_database():

    what_skill = input("what skill level are we looking for? ")
    what_lang = input('What language? ')
    sql = "SELECT * FROM example WHERE Skill == '? AND Language == ?'"

    for row in c.execute(sql, [(what_skill), (what_lang)]):
        print(row)

# read_from_database()

def update_database():
    sql = "UPDATE example SET Skill = 'Beginner' WHERE Skill = 'beginner'"
    c.execute(sql)
    sql = "SELECT * FROM example"
    for row in c.execute(sql):
        print(row)
    conn.commit()


# update_database()

def delete_from_database():
    sql = "SELECT * FROM example"
    for row in c.execute(sql):
        print(row)
    print(20*"#")
    sql = "DELETE FROM example WHERE Skill='Beginner'"
    c.execute(sql)
    sql = "SELECT * FROM example"
    for row in c.execute(sql):
        print(row)
    conn.commit()


# delete_from_database()

# conn.close()

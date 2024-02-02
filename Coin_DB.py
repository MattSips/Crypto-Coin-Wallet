import sqlite3
pycrypto = Tk()
pycrypto.title("My Crypto Portfolio")
con = sqlite3.connect('coin.db')
cursorObj = con.cursor()
cursorObj.execute("CREATE TABLE IF NOT EXISTS coin(id INTEGER PRIMARY KEY, symbol TEXT, amount INTEGER, price REAL)")
con.commit()

cursorObj.execute('''INSERT INTO coin(
    symbol, amount, price) VALUES 
    ('BTC', 3.5, 27000)''')

### cursor.execute('''INSERT INTO EMPLOYEE(
##    symbol, amount, price) VALUES 
##    ('LTE', 20, 1.5)''') 

### cursor.execute('''INSERT INTO EMPLOYEE(
##    symbol, amount, price) VALUES 
##    ('DMC', 100, 1.08)''')


pycrypto.mainloop()
cursorObj.close()
con.close()

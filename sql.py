import psycopg2

conn = psycopg2.connect(
    host="hopper.proxy.rlwy.net",
    port=22319,
    user="postgres",
    password="VcYzQBuZEoBGZZlkOGQBZpMNoQiKDylK",
    database="railway"
)

if conn:
    print("connection successful!")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IN NOT EXISTS students (
     id INT PRIMARY KEY,
     name VARCHARE(50),
     age INT
 )
 """) 
conn.commit()
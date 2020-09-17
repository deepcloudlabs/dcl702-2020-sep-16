import mysql.connector

# Change Data Capture
# https://www.confluent.io/blog/streaming-data-oracle-using-oracle-goldengate-kafka-connect/
con = mysql.connector.connect(host="localhost", user="root", password="Secret_123", database="world")

sql_query1 = "select co.code, co.name, ci.name  from country as co, city as ci where co.capital=ci.id and co.continent= 'Asia'"
sql_query2 = "select co.name, cl.language, cl.percentage from country as co, countrylanguage as cl where cl.countrycode=co.code and co.code='TUR'"

cur = con.cursor()
cur.execute(sql_query2)
result_set = cur.fetchall()
for row in result_set:  # row is a tuple
    print(row)

print(f"{cur.rowcount} record(s) fetched.")

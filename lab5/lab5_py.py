#!/usr/bin/python3
import cgi, os, time, cgitb
form = cgi.FieldStorage()
  
tytul = form.getvalue("data1","(no data)")
autor = form.getvalue("data2","(no data)")
date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 

def ip_address():
	try:
		ip = cgi.escape(os.environ["REMOTE_ADDR"])
	except:
		ip = "127.0.0.1"
	
	return ip

ip = ip_address()

filepath = "lab5_txt.txt"
f = open(filepath, "a")
f.write(tytul+";"+autor+";"+date+";"+ip+"\n")
f.close()

f = open(filepath, "r")
print ("Content-type: text/html")
print ()
print ("<!DOCTYPE html>")
print ("<html><head>")
print ("<title>REKORDY DOSTEPNE W BAZIE DANYCH</title>")
print ("</head><body>")
print("<table>")
print("<thead>")
print("<tr> <th> tytul <th> autor <th> date <th> IP")
print("<tbody>")
for line in f:
    print("<tr>")
    temp = line.split(";")
    print("<td>" + temp[0] + "<td>" + temp[1] +"<td>" + temp[2] +"<td>" + temp[3])
print("</table>")
print ("</body></html>")
f.close()

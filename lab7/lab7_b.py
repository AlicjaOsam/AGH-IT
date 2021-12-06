#!/usr/bin/python3
import cgi, os, time, cgitb
form = cgi.FieldStorage()

filepath = "lab7_txt.txt"
f = open(filepath, "r")
print ("Content-type: text/html")
print ()
print ("<!DOCTYPE html>")
print ("<html><head>")
print ("<title>REKORDY DOSTEPNE W BAZIE DANYCH</title>")
print ("</head><body>")
print("<table>")
print("<thead>")
print("<tr> <th> tytul <th> autor")
print("<tbody>")
for line in f:
    print("<tr>")
    temp = line.split(";")
    print("<td>" + temp[0] + "<td>" + temp[1])
print("</table>")
print ("</body></html>")
f.close()

#!/usr/bin/python3
import cgi, os, time, cgitb
form = cgi.FieldStorage()
  
tytul = form.getvalue("data1","(no data)")
autor = form.getvalue("data2","(no data)")

filepath = "lab7_txt.txt"
f = open(filepath, "a")
f.write(tytul+";"+autor+"\n")
f.close()
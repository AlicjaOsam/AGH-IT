#!/usr/bin/python3
print ("Content-Type: text/plain")
print ("")
print ("""\
<fieldset style="background-color:purple">
    <form action="cgi-bin/lab7_a.py" method="post"> 
        <fieldset class="f"><p>Tytuł<input type="text" name="data1"></p>
            <p>Autor<input type="text" name="data2"></p>
        </fieldset>
        <p><input type="submit"></p> 
    </form>
</fieldset> 
""" )
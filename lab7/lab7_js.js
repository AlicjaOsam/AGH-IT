var request;
function getRequestObject(){
    if ( window.ActiveXObject)  {
        return ( new ActiveXObject("Microsoft.XMLHTTP")) ;
    } 
    else if (window.XMLHttpRequest)  {
        return (new XMLHttpRequest())  ;
    } 
    else {
        return (null) ;
    }
}
 
function sendRequest(){
    request = getRequestObject() ;
    request.onreadystatechange = handleResponse ;
    request.open("GET", "cgi-bin/lab7_py.py", true);
    request.send(null);
}
 
function handleResponse(){
    myDiv = document.getElementById("MyDivElement")
    if (request.readyState == 4)    {
        myDiv.innerHTML += request.responseText;
    }
}
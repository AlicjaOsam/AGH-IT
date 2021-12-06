var xmlHttp;
 
function getRequestObject()      {
       if ( window.ActiveXObject)  {
            return ( new ActiveXObject("Microsoft.XMLHTTP")) ;
        } else if (window.XMLHttpRequest)  {
           return (new XMLHttpRequest())  ;
        } else {
           return (null) ;
        }
  }
function sendRequest()      {
       xmlHttp = getRequestObject() ;
       if (xmlHttp) {
         try {
           var url = "cgi-bin/lab7_cw2_a.py" ;
           xmlHttp.onreadystatechange = handleResponse ;
           xmlHttp.open("GET", url, true);
           xmlHttp.send(null);
         }
         catch (e) {
           alert ("Nie mozna polaczyc sie z serwerem: " + e.toString()) ;
         }
       } else {
         alert ("Blad") ;
       }
  }

  function sendRequest1()      {
    xmlHttp = getRequestObject() ;
    if (xmlHttp) {
      try {
        var url = "cgi-bin/lab7_cw2_b.py" ;
        xmlHttp.onreadystatechange = handleResponse ;
        xmlHttp.open("GET", url, true);
        xmlHttp.send(null);
      }
      catch (e) {
        alert ("Nie mozna polaczyc sie z serwerem: " + e.toString()) ;
      }
    } else {
      alert ("Blad") ;
    }
}
function handleResponse()      {
    myDiv = document.getElementById("MyDivElement");
    if (xmlHttp.readyState == 4) {
         if ( xmlHttp.status == 200 )  {
             response = xmlHttp.responseXML;
             var xmlRoot = response.documentElement ; 
             var optionArray = xmlRoot.getElementsByTagName('option') ;
             var html = "<select>" ;
             for ( var i=0; i<optionArray.length; i++) 
                 html += "<option>" +  optionArray.item(i).data + "</option>";
                 html += "</select>";
             myDiv.innerHTML += html ;
         }
    }  
}
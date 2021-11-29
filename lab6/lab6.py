from lxml import etree
 xmlfile = open('lab6_xml.xml') 
 xslfile = open('lab6_xsl.xsl')
 xmldom = etree.parse(xmlfile)
 xsldom = etree.parse(xslfile)
 transform = etree.XSLT(xsldom)

 result = transform(xmldom, sortby="’name ’")
 print result

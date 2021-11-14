<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
    <xsl:template match="/">
        <html>
            <link rel="stylesheet" type="text/css" href="lab4_css.css"/> 
            <head>
                <title>Uczelnia</title>
            </head>
            <body>
                <table border="1">
                    <xsl:for-each select="uczelnia/wydzial">
                        <xsl:sort select="nazwa/text()" />
                        <xsl:call-template name="nazwawydzial" />
                        <xsl:for-each select="./kierunek">
                            <xsl:sort select="nazwak/text()" />
                            <xsl:call-template name="nazwakierunek" />
                                <tr>
                                    <td>Nr Indeksu</td>
                                    <td>Nazwisko</td>
                                    <td>Imie</td>
                                </tr>
                                <xsl:for-each select="./student">
                                <xsl:sort select="nrindeksu/text()" />
                                <xsl:call-template name="nazwastudent" />
                            </xsl:for-each>
                        </xsl:for-each>
                    </xsl:for-each>
                </table>
            </body>
        </html>
    </xsl:template>

    <xsl:template name="nazwawydzial">
        <tr style="background-color: purple;">
            <th colspan="3" align="center"><xsl:value-of select="nazwa" /></th>
        </tr>
    </xsl:template>

    <xsl:template name="nazwakierunek">
        <tr>
            <th colspan="3" align="center"><xsl:value-of select="nazwak" /></th>
        </tr>
    </xsl:template>

    <xsl:template name="nazwastudent">
        <tr>
            <td><xsl:value-of select="nrindeksu" /></td>
            <td><xsl:value-of select="nazwisko" /></td>
            <td><xsl:value-of select="imie" /></td>
        </tr>
    </xsl:template>
    
</xsl:stylesheet>
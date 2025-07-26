<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <html>
            <head>
                <title>Gestion de la Scolarité</title>
                <style>
                    h1 {
                        text-align: center;
                        color: #4c4faf;
                        padding: 15px 0;
                        margin: 0;
                    }
                    table {
                        width: 80%;
                        margin: 30px auto;
                        border-collapse: collapse;
                    }
                    th, td {
                        padding: 12px;
                        text-align: center;
                    }
                    th {
                        background-color: #4c4faf;
                        color: white;
                    }
                    .table-container {
                        width: 90%;
                        margin: 20px auto;
                    }
                </style>
            </head>
            <body>
                <div class="table-container">
                    <h1>Liste des Filières</h1>
                    <table>
                        <tr>
                            <th>ID</th>
                            <th>Nom</th>
                        </tr>
                        <xsl:for-each select="scolarite/fillieres/filiere">
                            <tr>
                                <td><xsl:value-of select="idF" /></td>
                                <td><xsl:value-of select="nameF" /></td>
                            </tr>
                        </xsl:for-each>
                    </table>
                </div>
                <div class="table-container">
                    <h1>Liste des Étudiants</h1>
                    <table>
                        <tr>
                            <th>ID</th>
                            <th>Nom</th>
                            <th>Email</th>
                            <th>Classe ID</th>
                        </tr>
                        <xsl:for-each select="scolarite/etudiants/etudiant">
                            <tr>
                                <td><xsl:value-of select="idE" /></td>
                                <td><xsl:value-of select="nameE" /></td>
                                <td><xsl:value-of select="email" /></td>
                                <td><xsl:value-of select="classe_id" /></td>
                            </tr>
                        </xsl:for-each>
                    </table>
                </div>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>


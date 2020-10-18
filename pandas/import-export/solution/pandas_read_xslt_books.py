from io import StringIO
from lxml.etree import XML, XSLT, parse, tostring


TEMPLATE = """
    <html xsl:version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
        <table>
            <thead>
                <tr>
                    <th>Id</th>
                    <th>Author</th>
                    <th>Title</th>
                    <th>Genre</th>
                    <th>Price</th>
                    <th>Publish Date</th>
                    <th>Description</th>
                </tr>
            </thead>
            <tbody>

                <xsl:for-each select="catalog/book">
                    <tr>
                        <td><xsl:value-of select="@id"/></td>
                        <td><xsl:value-of select="author"/></td>
                        <td><xsl:value-of select="title"/></td>
                        <td><xsl:value-of select="genre"/></td>
                        <td><xsl:value-of select="price"/></td>
                        <td><xsl:value-of select="publish_date"/></td>
                        <td><xsl:value-of select="description"/></td>
                    </tr>
                </xsl:for-each>

            </tbody>
        </table>
    </html>
"""

with open('../_data/books.xml') as file:
    data = file.read()


transform = XSLT(XML(TEMPLATE))
data = parse(StringIO(data))
result = transform(data)

pd.read_html(tostring(result))[0]

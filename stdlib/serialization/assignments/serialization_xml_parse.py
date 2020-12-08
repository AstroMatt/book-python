"""
* Assignment: Serialization XML Parsing
* Filename: serialization_xml_parse.py
* Complexity: easy
* Lines of code: 20 lines
* Time: 13 min

English:
    1. Use data from "Given" section (see below)
    2. Convert input data to `list[dict]`

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Przekonwertuj dane wejściowe do `list[dict]`
"""


# Given
DATA = """<?xml version="1.0" encoding="UTF-8"?>
<CATALOG>
    <PLANT>
        <COMMON>Bloodroot</COMMON>
        <BOTANICAL>Sanguinaria canadensis</BOTANICAL>
        <ZONE>4</ZONE>
        <LIGHT>Mostly Shady</LIGHT>
        <PRICE>$2.44</PRICE>
        <AVAILABILITY>031599</AVAILABILITY>
    </PLANT>
    <PLANT>
        <COMMON>Columbine</COMMON>
        <BOTANICAL>Aquilegia canadensis</BOTANICAL>
        <ZONE>3</ZONE>
        <LIGHT>Mostly Shady</LIGHT>
        <PRICE>$9.37</PRICE>
        <AVAILABILITY>030699</AVAILABILITY>
    </PLANT>
    <PLANT>
        <COMMON>Marsh Marigold</COMMON>
        <BOTANICAL>Caltha palustris</BOTANICAL>
        <ZONE>4</ZONE>
        <LIGHT>Mostly Sunny</LIGHT>
        <PRICE>$6.81</PRICE>
        <AVAILABILITY>051799</AVAILABILITY>
    </PLANT>
    <PLANT>
        <COMMON>Cowslip</COMMON>
        <BOTANICAL>Caltha palustris</BOTANICAL>
        <ZONE>4</ZONE>
        <LIGHT>Mostly Shady</LIGHT>
        <PRICE>$9.90</PRICE>
        <AVAILABILITY>030699</AVAILABILITY>
    </PLANT>
<CATALOG>"""


# Solution

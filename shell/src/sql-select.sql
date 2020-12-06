SELECT * FROM kontakty;
SELECT * FROM stocks ORDER BY price;
SELECT long_name_of_the_colum as col FROM kontakty;

SELECT * FROM Customers WHERE CustomerName LIKE 'a%'; -- % - any character
SELECT * FROM Customers WHERE CustomerName LIKE '%or%'; -- % - any character
SELECT * FROM Customers WHERE CustomerName LIKE 'a_%_%'; -- _ - single character

SELECT * FROM Customers WHERE Country IN ('Germany', 'France', 'UK');
SELECT * FROM Customers WHERE Country IN (SELECT Country FROM Suppliers);

SELECT DISTINCT Country FROM Customers;
SELECT COUNT(DISTINCT Country) FROM Customers;

SELECT COUNT(column_name) FROM table_name WHERE condition;
SELECT AVG(column_name) FROM table_name WHERE condition;
SELECT SUM(column_name) FROM table_name WHERE condition;
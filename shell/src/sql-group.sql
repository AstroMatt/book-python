SELECT COUNT(CustomerID), Country
  FROM Customers
  GROUP BY Country;


SELECT COUNT(CustomerID), Country
  FROM Customers
  GROUP BY Country
  ORDER BY COUNT(CustomerID) DESC;

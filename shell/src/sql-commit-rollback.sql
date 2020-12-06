CREATE TABLE customer (id INT, name CHAR (20), INDEX (id));


START TRANSACTION;
INSERT INTO customer VALUES (1, 'Jose Jimenez');
COMMIT;


SET autocommit=0;
INSERT INTO customer VALUES (2, 'Mark Watney');
INSERT INTO customer VALUES (3, 'Ivan Ivanovich');
DELETE FROM customer WHERE name='Jose Jimenez';
ROLLBACK;  -- Now we undo those last 2 inserts and the delete.


SELECT * FROM customer;
-- +------+--------------+
-- | id   | name         |
-- +------+--------------+
-- |    1 | Jose Jimenez |
-- +------+--------------+
-- 1 row in set (0.00 sec)

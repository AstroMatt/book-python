ALTER TABLE table_name ADD column_name datatype;
ALTER TABLE table_name DROP COLUMN column_name;

-- SQL Server / MS Access:
ALTER TABLE table_name ALTER COLUMN column_name datatype;

-- My SQL / Oracle (prior version 10G):
ALTER TABLE table_name MODIFY COLUMN column_name datatype;

-- Oracle 10G and later:
ALTER TABLE table_name MODIFY column_name datatype;

-- MySQL / SQL Server / Oracle / MS Access:
ALTER TABLE table_name ADD PRIMARY KEY (id);

-- MySQL / SQL Server / Oracle / MS Access:
ALTER TABLE table_name ADD CONSTRAINT PK_contacts PRIMARY KEY (id, lastname);

UPDATE kontakty SET
    firstname='José'
  WHERE lastname='Jiménez';


UPDATE kontakty SET
    firstname=:firstname,
    lastname=:lastname,
    address=:address
WHERE id=:id

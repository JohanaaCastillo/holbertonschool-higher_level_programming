-- A script that lists all records of the table second_table of the database hbtn_0c_0
SELECT score, name FROM second_table
-- ORDER BY : Ordena los registros resultantes de una consulta por un campo o campos 
-- especificados en ordene ascendente(ASC) o descendente(DESC)
WHERE score >= 10
ORDER BY score DESC;
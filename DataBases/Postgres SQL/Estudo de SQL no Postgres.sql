/* MER - Lógico Faculdade DB: 


JOIN), comando que une os dados existentes na tabela "A" com os dados existentes na tabela "B". Observemos no código a seguir.
SELECT *
  FROM aluno
  JOIN aluno_curso ON aluno_curso.aluno_id = aluno.id

TIPOS DE DADOS:
SERIAL
VARCHAR
CHAR
TEXT
INTEGER
NUMERIC
BOOLEAN
DATE
TIME
TIMESTAMP



				FILTROS

A selecionar campos específicos da tabela
Como definir um alias para os nomes dos campos
A filtrar registros, utilizando o WHERE para campos do tipo de texto
Operadores =, !=,<>, LIKE e NOT LIKE
A diferença entre = e LIKE
O funcionamento do caractere % no filtro com LIKE e NOT LIKE
O funcionamento do caractere _ no filtro com LIKE e NOT LIKE
Como filtrar utilizando IS NULL e IS NOT NULL
Como filtrar registros para campos do tipos relacionados a números, datas e horas
=, !=, <>, <, <=, >, >=
BETWEEN
Como filtrar registros para campos do tipo booleano
=, !=, <>
Como funciona os operadores lógicos AND e OR

*/


/* 									CRUD                          */

/* CREATE TABLE*/
DROP TABLE DEPARTAMENTO;
CREATE TABLE DEPARTAMENTO (
    cod_depto SERIAL PRIMARY KEY,
    nome_depto VARCHAR(100),
   
	FOREIGN KEY (RA) 
	REFERENCES aluno (RA)
);

/* INSERT DE DADOS*/
INSERT INTO DEPARTAMENTO (nome_depto) VALUES ('CIÊNCIAS EXATAS');

/* UPDATE DE DADOS*/
UPDATE DEPARTAMENTO SET nome_depto = 'CIÊNCIAS HUMANAS' WHERE cod_depto = 1;

/* EXCLUSÃO DE DADOS*/
DELETE FROM DEPARTAMENTO WHERE cod_depto = 2;

/* FILTRANDO DADOS*/
SELECT * FROM DEPARTAMENTO;

/*USANDO ALIAS*/
SELECT cod_depto AS Codigo, 
	   nome_depto AS "Departamento de" 
FROM DEPARTAMENTO;


DROP TABLE aluno;
CREATE TABLE aluno(ra SERIAL PRIMARY KEY);
ALTER TABLE aluno
ADD COLUMN nome VARCHAR;
ALTER TABLE aluno
ADD COLUMN cpf VARCHAR (11);

/*FILTRANDO COM !=, =, LIKE, NOT LIKE, % e _*/
INSERT INTO aluno (nome) VALUES ('Vinícius Dias');
INSERT INTO aluno (nome) VALUES ('Nico Steppat');
INSERT INTO aluno (nome) VALUES ('João Roberto');
INSERT INTO aluno (nome) VALUES ('Diego');
INSERT INTO aluno (nome) VALUES ('Diogo');

SELECT *
    FROM aluno
 WHERE nome = 'Diogo';
 
SELECT *
    FROM aluno
 WHERE nome != 'Diogo'
 ORDER BY nome;
 
 
 SELECT * 
    FROM aluno
 WHERE nome LIKE 'Di_go';
 
 
 SELECT * 
    FROM aluno
 WHERE nome LIKE 'D%';
 
 
 SELECT * 
    FROM aluno
 WHERE nome LIKE '% %';
 
 
 SELECT * 
    FROM aluno
 WHERE nome LIKE '%i%a%';
 
 
 /*FILTRANDO CAMPOS IS NULL IS NOT NULL*/
 SELECT *
    FROM aluno
 WHERE cpf IS NULL;
 
  SELECT *
    FROM aluno
 WHERE cpf IS NOT NULL;


SELECT *
    FROM aluno
 WHERE idade BETWEEN 10 AND 20;
 
 
 SELECT *
    FROM aluno
  WHERE nome LIKE 'D%'
    AND cpf IS NOT NULL;
	
	
	SELECT *
    FROM aluno
  WHERE nome LIKE 'Diogo'
    OR nome LIKE 'Rodrigo';

/*-------------------------------------------------------------*/

/*CRIANDO UM FK*/

CREATE TABLE aluno (
    RA SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    cpf VARCHAR(11)
);

CREATE TABLE departamento (
    cod_depto SERIAL PRIMARY KEY,
    nome_depto VARCHAR(100),
    RA_aluno INTEGER
);

ALTER TABLE departamento
ADD CONSTRAINT fk_RA
FOREIGN KEY (RA_aluno) REFERENCES aluno (RA);
/* nome da constraint FK  NOME DA coluna na tabela que vai receber a FK e a coluna de onde a FK VIRÁ 

OBS NESSE CASO, É PRECISO CRIAR UM CAMPO QUE RECEBERÁ A FK, POIS A TABELA COM A PK QUE SERÁ A FK, JÁ HAVIA SIDO CRIADA.
*/



/*criando uma tabela e as foreing keys */
CREATE TABLE curso (
    id SERIAL PRIMARY KEY
);

CREATE TABLE aluno2 (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL
);

CREATE TABLE aluno_curso (
    aluno_id INTEGER,
        curso_id INTEGER,
        PRIMARY KEY (aluno_id, curso_id),

        FOREIGN KEY (aluno_id)
         REFERENCES aluno2 (id),

        FOREIGN KEY (curso_id)
         REFERENCES curso (id)
/* FOREIGN KEY - NOME DA coluna na tabela que vai receber a FK  REFERENCES - a tabela a coluna de onde a FK VIRÁ */

);
/*JOIN*/
SELECT *
  FROM aluno2
  JOIN aluno_curso ON aluno_curso.aluno_id = aluno2.id




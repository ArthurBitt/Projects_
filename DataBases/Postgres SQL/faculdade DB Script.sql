DROP TABLE aluno_curso, aluno;
CREATE TABLE aluno(
	id SERIAL PRIMARY KEY,
	nome VARCHAR (255) NOT NULL,
	sobrenome VARCHAR (255) NOT NULL,
	data_nascimento DATE NOT NULL
	
);

INSERT INTO aluno (nome,sobrenome,data_nascimento) VALUES ('Arthur','Bittencour', '20-11-1997')

CREATE TABLE curso (
	id SERIAL PRIMARY KEY,
	nome VARCHAR (255) NOT NULL,
	categoria_id INTEGER NOT NULL REFERENCES categoria(id)
);

INSERT INTO curso (nome, categoria_id) VALUES ('Python', 1) 


CREATE TABLE categoria (
	id SERIAL PRIMARY KEY,
	nome VARCHAR (255) NOT NULL

);

INSERT INTO categoria(nome) VALUES('Progamação');

CREATE TABLE aluno_curso(
	aluno_id INTEGER NOT NULL REFERENCES aluno(id),
	curso_id INTEGER NOT NULL REFERENCES curso(id),
	PRIMARY KEY(curso_id, aluno_id)
);


select * from aluno_curso;
select * from aluno;
select * from curso;
select * from categoria;
DROP TABLE produtos;

CREATE TABLE produtos(

id SERIAL PRIMARY KEY,
nome VARCHAR NOT NULL,
preco DECIMAL NOT NULL,
quantidade INTEGER NOT NULL


);


INSERT INTO produtos (nome, preco, quantidade) VALUES ('Galaxy watch 4', 690, 5);
INSERT INTO produtos (nome, preco, quantidade) VALUES ('Galaxy watch 5pro',2000, 5);
INSERT INTO produtos (nome, preco) VALUES ('Galaxy watch 6',2600);

SELECT * FROM produtos;

UPDATE produtos 
	SET preco = 680
	WHERE id = 1;

DELETE FROM produtos WHERE id = 2;


SELECT produtos.nome, produtos.preco
FROM produtos;	

-- DUAS ÁSPAS NO ALIAS PARA STRING 
SELECT produtos.nome AS "Nome do Produto"
FROM produtos;

-- QUERY COM WHERE CAMPO LIKE
SELECT * 
	FROM produtos 
	WHERE produtoS.nome LIKE '%alaxy watch 4';

-- QUERY OCULTANDO 1 CARACTER

SELECT *
	FROM produtos
	WHERE produtos.nome LIKE 'G_laxy watch 4';

-- QUERY COM WHERE CAMPO =
SELECT *
	FROM produtos
	WHERE produtos.nome = 'Galaxy watch 4'
	
-- QUERY COM OPERADORES
SELECT * 
	FROM produtos
	WHERE produtos.preco > 500 AND produtos.quantidade > 1;
	

-- QUERY IS NULL OR IS NOT NULL

SELECT *
	FROM produtos
	WHERE produtos.quantidade IS NULL;
	
SELECT *
	FROM produtos
	WHERE produtos.quantidade IS NOT NULL;
	
	
-- PK OU PRIMARY KEY É O QUE IDENTIFICA UM REGISTRO EM UMA TABELA, É ÚNICA PARA CADA REGISTRO, NÃO SE REPETE

DROP TABLE clientes

CREATE TABLE clientes (
	id SERIAL PRIMARY KEY

);

ALTER TABLE clientes
ADD COLUMN nome_cliente VARCHAR;


INSERT INTO clientes (nome_cliente) VALUES ('Arthur');
INSERT INTO clientes (nome_cliente) VALUES ('Bob');




DROP TABLE pedidos;


-- FK É RESPONSÁVEL POR RELACIONAR AS TABELAS, É A COLA ENTRE OS REGISTROS DE TABELAS DIFERENTE

-- DENTRO DO CREATE TABLE NÃO É NECESSÁRIO PASSAR CONSTRAINT
CREATE TABLE pedidos(

id SERIAL PRIMARY KEY,
id_clientes INTEGER,
	FOREIGN KEY (id_clientes)
	REFERENCES clientes(id)
);

INSERT INTO pedidos (id_clientes, id_produtos) VALUES (1,3);

-- DEPOIS DE CRIADA A TABELA É NECESSÁRIO INSERIR A FK GERENDO NOVO CAMPO, E PASSANDO CONSTRAINT PARA GARANTIR INTEGRIDADE DOS DADOS
ALTER TABLE pedidos
	ADD COLUMN id_produtos INTEGER;


ALTER TABLE pedidos
	ADD CONSTRAINT FK_id_produtos
	FOREIGN KEY (id_produtos)
	REFERENCES produtos (id);


-- USANDO O JOIN

-- O SELECT TRAS AS COLUNAS QUE IRÃO APARECER,
-- O FROM É A TABELA QUE SERÁ RELACIONADA COM A TABELA DO JOIN (CLIENTES)
-- ON CERTIFICA QUAIS SERÃO OS REGISTROS ALINHADOS 
-- CAMPO DA TABELA DO FROM = CAMPO DA TABELA DO JOIN


SELECT clientes.nome_cliente,
		pedidos.id as "ID do Pedido",
		produtos.nome as "Produto"
		
FROM pedidos
-- Da tabela pedidos, une com a tabela clientes e alinha os registros onde a FK da tab 1 é igual a PK da tab 2 - onde pedidos.id_clientes é igual a clientes.id
JOIN clientes ON pedidos.id_clientes = clientes.id
JOIN produtos ON pedidos.id_produtos = produtos.id


-- RESTRICT E CASCADE

-- RESTRICT É CONSERVADOR E MANÉM A INTEGRIDADE DA TABELA RESTRINGINDO QUE UMA TABELA PAI SEJA APAGADA CASO HAJA UMA FK RELACIONADA A SUA PK.
-- CASCADE VIABILIZA QUE AO APAGAR O REGISTRO DE UM PK DA TABELA PAI, A FK CORRESPONDENTE E TODOS OS VÍNCULOS ENTRE OS REGISTROS E A PK TB SEJAM APAGADOS

-- SUPONDO QUE A TABELA produtos TIVESSE SIDO CONFIGURADA PARA ON DELETE CASCADE, AO APAGAR O ID 3, TODOS OS PEDIDOS QUE CONTENHAM RELAÇÃO FK COM ESSE REGISTRO, TAMBÉM SERIAM APAGADOS.
/*
CREATE TABLE produtos(

id SERIAL PRIMARY KEY,
nome VARCHAR NOT NULL,
preco DECIMAL NOT NULL,
quantidade INTEGER NOT NULL

ON DELETE CASCADE
);


DELETE FROM produtos 
WHERE id = 3*/

























CREATE DATABASE IF NOT EXISTS IFOOD;

USE IFOOD;

CREATE TABLE IF NOT EXISTS IFOOD.CLIENTE
(
	ID_CLIENTE INT,
    NOME_COMPLETO VARCHAR(100),
    NUM_CPF CHAR(11),
    DESC_EMAIL VARCHAR(100),
    NUM_TELEFONE VARCHAR(11),
    PRIMARY KEY (ID_CLIENTE)
);
CREATE TABLE IF NOT EXISTS IFOOD.ENTREGADOR
(
	ID_ENTREGADOR INT,
    NOME VARCHAR(25),
    NUM_CPF CHAR(11),
    TIPO_VEICULO VARCHAR(30), -- VOLTAR AQUI
    PLACA CHAR(7),
    PRIMARY KEY (ID_ENTREGADOR)
);

CREATE TABLE IF NOT EXISTS IFOOD.PRODUTO
(
    NOME_ITEM VARCHAR(100),
    DESCFRICAO VARCHAR(100),
    PREÇO_UNITARIO DECIMAL,
    PRIMARY KEY (NOME_ITEM)
);

CREATE TABLE IF NOT EXISTS IFOOD.PEDIDO
 -- CONSTRAINT + FOREIGN KEY + REFERENCES  -- PARA LIGAR TABELAS
(
	ID_CLIENTE INT,
	ID_ENTREGADOR INT,
    NOME_ITEM VARCHAR(100),
	DATA_HORA DATETIME, 
    VALOR_TOTAL DECIMAL,
    CONSTRAINT FK_CLIENTE
		FOREIGN KEY (ID_CLIENTE) REFERENCES IFOOD.CLIENTE (ID_CLIENTE),
	CONSTRAINT FK_ENTREGADOR 
		FOREIGN KEY (ID_ENTREGADOR) REFERENCES IFOOD.ENTREGADOR (ID_ENTREGADOR),
    CONSTRAINT FK_PRODUTO 
		FOREIGN KEY (NOME_ITEM) REFERENCES IFOOD.PRODUTO (NOME_ITEM)
 );

SELECT * FROM IFOOD.CLIENTE;
INSERT INTO IFOOD.CLIENTE (ID_CLIENTE, NOME_COMPLETO, NUM_CPF, DESC_EMAIL, NUM_TELEFONE) VALUES
						  (1, 'Lucas Silva Sauro', '12345678901', 'lucas.silva@email.com', '11988887777'),
						  (2, 'Ana Beatriz Oliveira', '23456789012', 'ana.bea@email.com', '11977776666'),
						  (3, 'Carlos Eduardo Santos', '34567890123', 'cadu.santos@email.com', '21966665555'),
						  (4, 'Mariana Costa Ferreira', '45678901234', 'mari.costa@email.com', '31955554444'),
						  (5, 'Ricardo Pereira Lima', '56789012345', 'ricardo.lima@email.com', '41944443333'),
						  (6, 'Juliana Mendes Rocha', '67890123456', 'ju.mendes@email.com', '51933332222'),
						  (7, 'Fernando Souza Neto', '78901234567', 'fernando.neto@email.com', '61922221111'),
						  (8, 'Beatriz Martins Alvares', '89012345678', 'bia.martins@email.com', '71911110000'),
						  (9, 'Gustavo Henrique Dias', '90123456789', 'gustavo.dias@email.com', '81900009999'),
						  (10, 'Patrícia Albuquerque', '01234567890', 'paty.albu@email.com', '91988881111'),
						  (11, 'Rodrigo Faro Silva', '11223344556', 'rodrigo.faro@email.com', '11922223333'),
						  (12, 'Camila Pitanga Rosa', '22334455667', 'camila.rosa@email.com', '11933334444'),
						  (13, 'Bruno Gagliasso Vaz', '33445566778', 'bruno.vaz@email.com', '21944445555'),
						  (14, 'Vanessa Giácomo Mel', '44556677889', 'vanessa.mel@email.com', '31955556666'),
						  (15, 'Tiago Leifert Junior', '55667788990', 'tiago.jr@email.com', '11966667777'),
						  (16, 'Fernanda Montenegro', '66778899001', 'fernanda.m@email.com', '21977778888'),
						  (17, 'Lázaro Ramos Castro', '77889900112', 'lazaro.castro@email.com', '71988889999'),
						  (18, 'Taís Araújo Silva', '88990011223', 'tais.araujo@email.com', '21999990000'),
						  (19, 'Paolla Oliveira Luz', '99001122334', 'paolla.luz@email.com', '11911112222'),
						  (20, 'Selton Mello Filho', '00112233445', 'selton.filho@email.com', '11922221111');

SELECT * FROM IFOOD.ENTREGADOR;
INSERT INTO IFOOD.ENTREGADOR (ID_ENTREGADOR, NOME, NUM_CPF, TIPO_VEICULO, PLACA) VALUES
(1, 'Marcos Oliveira', '11122233344', 'Moto', 'ABC1D23'),
(2, 'Ana Paula Farias', '22233344455', 'Bicicleta', 'PEDAL01'),
(3, 'João Vitor Cruz', '33344455566', 'Moto', 'XYZ9D87'),
(4, 'Carla Cavalcanti', '44455566677', 'Carro', 'IFD2024'),
(5, 'Douglas Souza', '55566677788', 'Moto', 'KRY5F12'),
(6, 'Elena Moretti', '66677788899', 'Bicicleta', 'BIKE999'),
(7, 'Fabio Junior Jr', '77788899900', 'Moto', 'MTO8G45'),
(8, 'Gisele Bündchen S', '88899900011', 'Carro', 'POP1I00'),
(9, 'Hugo Leonardo', '99900011122', 'Moto', 'DRV4H32'),
(10, 'Igor Guimarães', '00011122233', 'Moto', 'RISO555');

SELECT * FROM IFOOD.PRODUTO;
INSERT INTO IFOOD.PRODUTO (NOME_ITEM, DESCFRICAO, PREÇO_UNITARIO) VALUES
('X-Salada Especial', 'Pão, carne 150g, alface, tomate, queijo e maionese', 25.90),
('Batata Frita G', 'Porção de 400g de batatas crocantes', 18.00),
('Coca-Cola 2L', 'Refrigerante garrafa 2 litros', 12.50),
('Pizza Calabresa', 'Molho de tomate, mussarela, calabresa e cebola', 45.00),
('Pizza Marguerita', 'Molho de tomate, mussarela, manjericão e tomate', 42.00),
('Açaí 500ml', 'Açaí puro com granola e leite em pó', 22.00),
('Combinado Japa 15pçs', '5 hots, 5 uramakis, 5 niguiris', 55.00),
('Temaki Salmão', 'Salmão em cubos, cream cheese e cebolinha', 28.90),
('Pastel de Carne', 'Pastel frito na hora tamanho G', 10.00),
('Pastel de Queijo', 'Pastel frito na hora tamanho G', 10.00),
('Suco de Laranja 500ml', 'Suco natural da fruta', 9.00),
('Marmitex Executiva', 'Arroz, feijão, bife, batata frita e salada', 24.00),
('Espetinho de Carne', 'Acompanha farofa e vinagrete', 8.50),
('Coxinha de Frango', 'Salgado frito com recheio de frango e catupiry', 7.00),
('Hambúrguer Artesanal', 'Pão brioche, blend 180g e cheddar', 32.00),
('Hot Dog Simples', 'Pão, salsicha, batata palha e molhos', 12.00),
('Cerveja Heineken 350ml', 'Lata gelada', 6.50),
('Petit Gateau', 'Bolinho quente com sorvete de baunilha', 19.90),
('Salada Caesar', 'Alface, croutons, frango grelhado e molho', 26.00),
('Nuggets 10 unidades', 'Acompanha molho barbecue', 15.00),
('Beirute de Filé', 'Pão sírio, filé, ovo, queijo e presunto', 38.00),
('Taco Mexicano', 'Tortilha de milho, carne moída e chilli', 14.00),
('Burrito de Frango', 'Tortilha recheada com frango e feijão', 22.00),
('Pudim de Leite', 'Fatia individual', 8.00),
('Brigadeiro Gourmet', 'Unidade 30g', 4.50),
('Água Mineral 500ml', 'Sem gás', 3.50),
('Espaguete à Bolonhesa', 'Massa artesanal com molho de carne', 30.00),
('Lasanha de Presunto', 'Individual ao forno', 35.00),
('Risoto de Camarão', 'Arroz arbóreo com camarões médios', 48.00),
('Milkshake Chocolate', 'Copo de 400ml', 16.00),
('Brownie Recheado', 'Recheio de doce de leite', 12.00),
('Kibe Frito', 'Unidade grande', 6.50),
('Esfiha de Carne', 'Aberta tipo árabe', 5.00),
('Yakisoba de Carne', 'Macarrão, carne e legumes 500g', 34.00),
('Guaraná Antarctica 1.5L', 'Refrigerante garrafa', 10.00),
('Omelete Completa', '3 ovos, queijo, presunto e ervas', 18.00),
('Poke de Salmão', 'Peixe, arroz, sunomono e manga', 42.00),
('Frango Assado Inteiro', 'Acompanha farofa', 45.00),
('Costelinha BBQ', 'Porção individual com fritas', 52.00),
('Sopa de Capeletti', 'Porção de 400ml para o inverno', 20.00);
                              
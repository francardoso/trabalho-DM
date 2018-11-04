CREATE TABLE `cnpjs`
(
	id int not null AUTO_INCREMENT,
  cnpj character varying(50),
  razao_social text,
  nome_fantasia text,
  uf text,
  municipio text,
  cep text,
  data_abertura character varying(20),
  situacao text,
  PRIMARY KEY(id)
);

CREATE TABLE `dados_2017`
(
	id smallint not null,
	txNomeParlamentar varchar(100),
	idecadastro int, 
	nuLegislatura int,
	sgUF char(2),
	sgPartido char(10),
	txtDescricaoEspecificacao varchar(255),
	txtCNPJCPF varchar(50),
	datEmissao timestamp,
	vlrDocumento float,
	numMes smallint,
	PRIMARY KEY (id)
);

create index cnpj1 on cnpjs (cnpj);
create index cnpj2 on dados_2017 (txtCNPJCPF);
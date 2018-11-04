DROP TABLE IF EXISTS `dados_2017`;
DROP TABLE IF EXISTS `cnpjs`;

CREATE TABLE `cnpjs`
(
  cnpj character varying(50) not null,
  razao_social text,
  nome_fantasia text,
  uf text,
  municipio text,
  cep text,
  data_abertura character varying(20),
  situacao text,
  PRIMARY KEY(cnpj)
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
	txtCNPJCPF varchar(50) not null,
	datEmissao datetime,
	vlrDocumento float,
	numMes smallint,
	PRIMARY KEY (id),
	FOREIGN KEY (txtCNPJCPF) 
			REFERENCES cnpjs (cnpj)
);

create index cnpj1 on cnpjs (cnpj);
create index cnpj2 on dados_2017 (txtCNPJCPF);
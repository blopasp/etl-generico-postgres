create table if not exists orgao (
    codigo_orgao integer primary key,
    nome_orgao varchar(100) not null,
    codigo_orgao_superior integer,
    constraint fk_sup foreign key (codigo_orgao_superior) references orgao_superior (codigo_orgao_superior)
);
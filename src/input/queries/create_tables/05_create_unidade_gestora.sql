create table if not exists unidade_gestora (
    codigo_unidade_gestora integer primary key,
    nome_unidade_gestora varchar(50) not null,
    codigo_orgao integer,
    constraint fk_org foreign key (codigo_orgao) references orgao (codigo_orgao)
);
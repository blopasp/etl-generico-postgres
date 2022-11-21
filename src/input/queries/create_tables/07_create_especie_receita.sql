create table if not exists especie_receita (
    codigo_especie_receita serial primary key,
    especie_receita varchar(50),
    codigo_origem_receita integer,
    constraint fk_esprec foreign key (codigo_origem_receita) references origem_receita (codigo_origem_receita)
);
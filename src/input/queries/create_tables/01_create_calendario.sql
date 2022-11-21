create table if not exists calendario(
    data_calendario date primary key,
    dia_calendario int,
    mes_calendario int,
    ano_calendario int,
    dia_semana_calendario int,
    dia_semana_descricao_calendario varchar(10)
);
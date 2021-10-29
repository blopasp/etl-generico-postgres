create table if not exists calendario(
    codigo_calendario serial primary key,
    data_calendario date,
    dia_calendario int,
    mes_calendario int,
    ano_calendario int,
    dia_semana_calendario int,
    dia_semana_descricao_calendario varchar(10)
);
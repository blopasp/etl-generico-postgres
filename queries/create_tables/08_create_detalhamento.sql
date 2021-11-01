create table if not exists detalhamento(
    codigo_detalhamento serial primary key,
    codigo_orgao integer,
    codigo_orgao_superior integer,
    codigo_unidade_gestora integer,
    codigo_categoria_economica integer,
    codigo_origem_receita integer,
    codigo_especie_receita integer,
    data_detalhamento date,
    valor_previsto decimal(18,2),
    valor_lancado decimal(18,2),
    valor_relalizado decimal(18,2)
);
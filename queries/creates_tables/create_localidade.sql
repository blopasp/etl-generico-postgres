CREATE TABLE IF NOT EXISTS public.localidade(
    codigo_localidade serial primary key,
    municipio varchar(255),
    UF varchar(2),
    regiao varchar(25)
);
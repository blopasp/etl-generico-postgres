CREATE TABLE IF NOT EXISTS public.beneficiario(
    codigo_beneficiario serial primary key,
    nome varchar(255),
    codigo_localidade int,
    CONSTRAINT fk_loc FOREIGN KEY (codigo_localidade) REFERENCES public.localidade(codigo_localidade)
);
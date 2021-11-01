create or replace procedure insert_fato_receitas()
language plpgsql as
$proc$
begin
	
	truncate fato_receitas restart identity cascade;
	insert into fato_receitas (
		codigo_orgao_superior,
	    codigo_orgao,
	    codigo_unidade_gestora,
	    codigo_categoria_economica,
	    codigo_origem_receita,
	    codigo_especie_receita,
	    data_receita,
	    valor_previsto,
	    valor_lancado,
	    valor_realizado
	)
	select 
		(
			select codigo_orgao_superior
			from orgao_superior os
			where os.codigo_orgao_superior = rgf.codigo_orgao_superior
			fetch first row only
		) as codigo_orgao_superior,
		(
			select codigo_orgao
			from orgao o
			where o.codigo_orgao = rgf.codigo_orgao
			fetch first row only	
		) as codigo_orgao,
		(
			select codigo_unidade_gestora
			from unidade_gestora ug
			where ug.codigo_unidade_gestora = rgf.codigo_unidade_gestora
			fetch first row only	
		) as codigo_unidade_gestora,
		(
			select codigo_categoria_economica
			from categoria_economica ce
			where trim(ce.nome_categoria_economica) = trim(rgf.categoria_economica)
			fetch first row only	
		) as codigo_categoria_economica,
		(
			select codigo_origem_receita
			from origem_receita ore
			where trim(ore.nome_origem_receita) = trim(rgf.origem_receita)
			fetch first row only	
		) as codigo_origem_receita,
		(
			select codigo_especie_receita
			from especie_receita ore
			where trim(ore.especie_receita) = trim(rgf.especie_receita)
			fetch first row only	
		) as codigo_especie_receita,
		to_date(rgf.data_lancamento, 'DD/MM/YYYY') as data_receita,
		cast(replace(valor_previsto_atualizado, ',', '.') as decimal(18,2)) as valor_previsto,
		cast(replace(valor_lancado, ',', '.') as decimal(18,2)) as valor_lancado,
		cast(replace(valor_realizado, ',', '.') as decimal(18,2)) as valor_realizado
	
	from receitas_governo_federal rgf
	where data_lancamento <> 'NaN';

end;
$proc$

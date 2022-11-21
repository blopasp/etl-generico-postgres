create or replace procedure insert_unidade_gestora()
language plpgsql as
$proc$
begin
	truncate unidade_gestora restart identity cascade;
	insert into unidade_gestora
	select 
		codigo_unidade_gestora,
		trim(nome_unidade_gestora) as nome_unidade_gestora,
		(
			select codigo_orgao
			from orgao o
			where o.codigo_orgao = rgf.codigo_orgao 
			fetch first row only
		) as codigo_orgao
		
	from receitas_governo_federal rgf 
	group by
		codigo_unidade_gestora,
		trim(nome_unidade_gestora),
		(
			select codigo_orgao
			from orgao o
			where o.codigo_orgao = rgf.codigo_orgao 
			fetch first row only
		)
		
	order by codigo_orgao;
end;
$proc$
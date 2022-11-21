create or replace procedure insert_orgao()
language plpgsql as
$proc$
begin
	truncate orgao restart identity cascade;
	insert into orgao
	select 
		codigo_orgao,
		trim(nome_orgao) as nome_orgao,
		(
			select codigo_orgao_superior
			from orgao_superior os
			where os.codigo_orgao_superior = rgf.codigo_orgao_superior 
			fetch first row only
		) as codigo_orgao_superior
		
	from receitas_governo_federal rgf 
	group by
		codigo_orgao,
		trim(nome_orgao),
		(
			select codigo_orgao_superior
			from orgao_superior os
			where os.codigo_orgao_superior = rgf.codigo_orgao_superior 
			fetch first row only
		)
		
	order by codigo_orgao;
end;
$proc$
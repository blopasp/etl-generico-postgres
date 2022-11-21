create or replace procedure insert_orgao_superior()
language plpgsql as
$proc$
begin
	truncate orgao_superior restart identity cascade;
	insert into orgao_superior
	select 
		codigo_orgao_superior,
		trim(nome_orgao_superior) as nome_orgao_superior
	from receitas_governo_federal rgf 
	group by
		codigo_orgao_superior,
		trim(nome_orgao_superior)
	order by codigo_orgao_superior;
end;
$proc$
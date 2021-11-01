create or replace procedure insert_especie_receita()
language plpgsql as
$proc$
begin
	truncate especie_receita restart identity cascade;
	insert into especie_receita (especie_receita, codigo_origem_receita)
	select 
		trim(especie_receita) as especie_receita,
		(
			select codigo_origem_receita
			from origem_receita ore
			where trim(ore.nome_origem_receita) = trim(rgf.origem_receita) 
			fetch first row only
		) as codigo_origem_especie
		
	from receitas_governo_federal rgf 
	group by
		trim(especie_receita),
		(
			select codigo_origem_receita
			from origem_receita ore
			where trim(ore.nome_origem_receita) = trim(rgf.origem_receita) 
			fetch first row only
		);
end;
$proc$
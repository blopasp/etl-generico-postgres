create or replace procedure insert_categoria_economica()
language plpgsql as
$proc$
begin
	truncate categoria_economica restart identity cascade;

	insert into categoria_economica (nome_categoria_economica)
	select 
		distinct trim(categoria_economica) as nome_categoria_economica
	from receitas_governo_federal rgf;
end;
$proc$
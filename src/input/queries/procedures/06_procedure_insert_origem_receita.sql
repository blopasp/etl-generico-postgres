create or replace procedure insert_origem_receita()
language plpgsql as
$proc$
begin
	truncate origem_receita restart identity cascade;
	insert into origem_receita (nome_origem_receita)
	select 
		distinct origem_receita as nome_origem_receita 
	from receitas_governo_federal rgf;
end;
$proc$
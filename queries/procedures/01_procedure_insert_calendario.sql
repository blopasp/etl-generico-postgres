create or replace procedure insert_calendario()
language plpgsql as
$proc_date$ 
declare 
	data1 date;
	data2 date;
begin
	truncate calendario restart identity cascade;

	data1 := (select current_date - interval'20000 day');
	data2 := (select current_date + interval'5000 day');
	insert into calendario (data_calendario, dia_calendario, mes_calendario, ano_calendario, dia_semana_calendario, dia_semana_descricao_calendario)		
		select
			i::date as data_calendario, 
			extract(day from i::date) as dia_calendario,
			extract(month from i::date) as mes_calendario,
			extract(year from i::date) as ano_calendario,
			extract(dow from i::date) + 1 as dia_semana_calendario,
			case
				when extract(dow from i::date) + 1 = 1 then 'Domingo'
				when extract(dow from i::date) + 1 = 2 then 'Segunda'
				when extract(dow from i::date) + 1 = 3 then 'Terca'
				when extract(dow from i::date) + 1 = 4 then 'Quarta'
				when extract(dow from i::date) + 1 = 5 then 'Quinta'
				when extract(dow from i::date) + 1 = 6 then 'Sexta'
				else 'Sabado'
			end dia_semana_descricao_calendario
		from generate_series(data1, 
		  data2, '1 day'::interval) i
		order by data_calendario desc;
	
end;
$proc_date$
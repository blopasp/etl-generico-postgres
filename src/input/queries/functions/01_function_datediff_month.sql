create or replace function public.datediff_month(data1 date, data2 date) returns int
as 'select (DATE_PART(''year'', $1) - DATE_PART(''year'', $2))*12 + 
    (DATE_PART(''MONTH'', $1) - DATE_PART(''MONTH'', $2))'
language 'sql';
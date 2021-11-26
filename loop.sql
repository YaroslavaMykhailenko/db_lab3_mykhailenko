select * from products;
create table productcopy as select * from products; 
select * from productcopy;
drop table productcopy


DO $$
DECLARE
    prod_id     productcopy.prod_id%TYPE;
    prod_name   productcopy.prod_name%TYPE;
	prod_price  productcopy.prod_price%TYPE;
	

BEGIN
    prod_id := 'BRE5';
    prod_name := 'Bombay Aloo';
	prod_price := 5.95;
	
    FOR counter IN 1..10
        LOOP
            INSERT INTO productcopy(prod_id, prod_name, prod_price)
            VALUES (prod_id || counter, prod_name || ' ' || counter, prod_price + counter);
        END LOOP;
END;
$$
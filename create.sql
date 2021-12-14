-------------------------
-- Create Products table
-------------------------
CREATE TABLE Products
(
  prod_id    char(10)      UNIQUE NOT NULL ,
  prod_name  char(50)      NOT NULL ,
  prod_price decimal(8,2)  NOT NULL 

);

--------------------------
-- Create Restaurants table
--------------------------

CREATE TABLE Restaurants
(
  rest_id       char(10)  UNIQUE NOT NULL ,
  rest_name     char(50)  NOT NULL 
);

--------------------------
-- Create Restaurants_Products table
--------------------------

CREATE TABLE Restaurants_Products
(
  rest_id       char(10)    NOT NULL ,
  prod_id       char(10)    NOT NULL 
);


----------------------
-- Create Orders table
----------------------

CREATE TABLE Orders
(
  order_num    int           UNIQUE NOT NULL ,
  rest_id      char(10)      NOT NULL ,
  order_date   date          NOT NULL 
   
);

----------------------
-- Create OrderItems table
----------------------

CREATE TABLE OrderItems
(
  order_num    int           NOT NULL ,
  prod_id      char(10)      NOT NULL ,
  quantity     int           NOT NULL
);





----------------------
-- Define primary keys
----------------------
ALTER TABLE Products ADD CONSTRAINT PK_Products PRIMARY KEY (prod_id);
ALTER TABLE Restaurants ADD CONSTRAINT PK_Restaurants PRIMARY KEY (rest_id);
ALTER TABLE Restaurants_Products ADD CONSTRAINT PK_Restaurants_Products PRIMARY KEY (rest_id,prod_id);
ALTER TABLE Orders ADD CONSTRAINT PK_Orders PRIMARY KEY (order_num);
ALTER TABLE OrderItems ADD CONSTRAINT PK_OrderItems PRIMARY KEY (order_num, prod_id);


----------------------
-- Define foreign keys
----------------------
ALTER TABLE Orders
ADD CONSTRAINT FK_Orders_Restaurants FOREIGN KEY (rest_id) REFERENCES Restaurants (rest_id);
ALTER TABLE OrderItems
ADD CONSTRAINT FK_OrderItems_Orders FOREIGN KEY (order_num) REFERENCES Orders (order_num);
ALTER TABLE OrderItems
ADD CONSTRAINT FK_OrderItems_Products FOREIGN KEY (prod_id) REFERENCES Products (prod_id);
ALTER TABLE Restaurants_Products
ADD CONSTRAINT FK_Restaurants_Products_Restaurants FOREIGN KEY (rest_id) REFERENCES Restaurants (rest_id);
ALTER TABLE Restaurants_Products
ADD CONSTRAINT FK_Restaurants_Products_Products FOREIGN KEY (prod_id) REFERENCES Products (prod_id);
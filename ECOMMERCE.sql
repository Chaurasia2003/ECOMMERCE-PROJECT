CREATE DATABASE ecommerce; 
use ecommerce;
CREATE TABLE `customer` (

`customer_id` varchar(10) NOT NULL,
`name` varchar(100) NOT NULL,
`city` varchar(65) NOT NULL,
`email` varchar(45) NOT NULL,
`phone_no` varchar(15) NOT NULL,
`address` varchar(100) NOT NULL,
`pin_code` int NOT NULL,
PRIMARY KEY (`customer_id`)
) ;
CREATE TABLE `product` (
`product_id` varchar(10) NOT NULL,
`product_name` varchar(100) NOT NULL,
`category` varchar(65) NOT NULL,
`sub_category` varchar(45) NOT NULL,
`original_price` double NOT NULL,
`selling_price` double NOT NULL,
`stock` int NOT NULL,
PRIMARY KEY (`product_id`)
);
CREATE TABLE `order_details` (
`order_id` int NOT NULL AUTO_INCREMENT,
`customer_id` varchar(10) NOT NULL,
`product_id` varchar(10) NOT NULL,
`quantity` double NOT NULL,
`total_price` double NOT NULL,
`payment_mode` varchar(60) NOT NULL,
`order_date` datetime DEFAULT NULL,
`order_status` varchar(20) NOT NULL,
PRIMARY KEY (`order_id`),
KEY `customer_id` (`customer_id`),
KEY `product_id` (`product_id`),
CONSTRAINT `order_details_ibfk_1` FOREIGN KEY (`customer_id`)
REFERENCES `customer` (`customer_id`),
CONSTRAINT `order_details_ibfk_2` FOREIGN KEY (`product_id`)
REFERENCES `product` (`product_id`)
);
show tables;
INSERT INTO customer (customer_id, name, city, email, phone_no, address, pin_code)
VALUES 
('C001', 'John Doe', 'New York', 'john.doe@example.com', '1234567890', '123 Maple St', 10001),
('C002', 'Jane Smith', 'Los Angeles', 'jane.smith@example.com', '0987654321', '456 Oak St', 90001),
('C003', 'Mike Johnson', 'Chicago', 'mike.johnson@example.com', '1122334455', '789 Pine St', 60601),
('C004', 'Emily Davis', 'Houston', 'emily.davis@example.com', '2233445566', '101 Birch St', 77001),
('C005', 'Chris Brown', 'Philadelphia', 'chris.brown@example.com', '3344556677', '202 Cedar St', 19101),
('C006', 'Jessica Wilson', 'Phoenix', 'jessica.wilson@example.com', '4455667788', '303 Walnut St', 85001),
('C007', 'David Martinez', 'San Antonio', 'david.martinez@example.com', '5566778899', '404 Elm St', 78201),
('C008', 'Sarah Taylor', 'San Diego', 'sarah.taylor@example.com', '6677889900', '505 Spruce St', 92101),
('C009', 'Daniel Anderson', 'Dallas', 'daniel.anderson@example.com', '7788990011', '606 Sycamore St', 75201),
('C010', 'Sophia Lee', 'San Jose', 'sophia.lee@example.com', '8899001122', '707 Hickory St', 95101);
INSERT INTO product (product_id, product_name, category, sub_category, original_price, selling_price, stock)
VALUES 
('P001', 'Laptop', 'Electronics', 'Computers', 1000.00, 950.00, 50),
('P002', 'Smartphone', 'Electronics', 'Mobile Phones', 700.00, 650.00, 200),
('P003', 'Headphones', 'Accessories', 'Audio', 100.00, 90.00, 150),
('P004', 'Tablet', 'Electronics', 'Tablets', 300.00, 280.00, 100),
('P005', 'Smartwatch', 'Accessories', 'Wearable Tech', 200.00, 180.00, 120),
('P006', 'Monitor', 'Electronics', 'Displays', 400.00, 350.00, 60),
('P007', 'Keyboard', 'Accessories', 'Peripherals', 50.00, 45.00, 500),
('P008', 'Mouse', 'Accessories', 'Peripherals', 30.00, 25.00, 600),
('P009', 'Printer', 'Electronics', 'Office Equipment', 150.00, 140.00, 80),
('P010', 'External Hard Drive', 'Accessories', 'Storage', 120.00, 110.00, 250);

INSERT INTO order_details (customer_id, product_id, quantity, total_price, payment_mode, order_date, order_status)
VALUES 
('C001', 'P001', 1, 950.00, 'Credit Card', '2024-10-04 10:00:00', 'Delivered'),
('C002', 'P002', 2, 1300.00, 'PayPal', '2024-10-03 14:30:00', 'Shipped'),
('C003', 'P003', 3, 270.00, 'Debit Card', '2024-10-02 09:45:00', 'Processing'),
('C004', 'P004', 1, 280.00, 'Credit Card', '2024-10-01 16:20:00', 'Delivered'),
('C005', 'P005', 2, 360.00, 'Cash on Delivery', '2024-09-30 11:00:00', 'Delivered'),
('C006', 'P006', 1, 350.00, 'Credit Card', '2024-09-29 17:15:00', 'Shipped'),
('C007', 'P007', 5, 225.00, 'PayPal', '2024-09-28 12:45:00', 'Processing'),
('C008', 'P008', 4, 100.00, 'Debit Card', '2024-09-27 14:30:00', 'Delivered'),
('C009', 'P009', 1, 140.00, 'Credit Card', '2024-09-26 13:50:00', 'Shipped'),
('C010', 'P010', 2, 220.00, 'PayPal', '2024-09-25 09:10:00', 'Delivered');
select * from customer;
CREATE DATABASE employee;
use employee;

CREATE TABLE employee_list (
  firstname VARCHAR(20),
  lastname VARCHAR(10)
);

INSERT INTO employee_list
  (firstname, lastname)
VALUES
  ('Lancelot', 'olsen'),
  ('Debasish', 'ghose'),
  ('Galahad', 'herald');

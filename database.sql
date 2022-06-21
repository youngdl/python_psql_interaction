begin;
create table person (
    id serial primary key,
    name varchar(40) not null
);

create table device_category (
    id serial primary key,
    category varchar(50) not null
);

create table device (
    id serial primary key,
    name varchar(100) not null,
    device_category_id integer references device_category(id)
);

create table inventory (
    id serial primary key,
    person_id integer references person(id),
    device_id integer references device(id),
    is_active boolean not null,
    purchase_date date not null,
    price decimal not null
);
commit;

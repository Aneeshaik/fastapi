create table if not exists payments(
    id serial primary key,
    amount numeric(12, 2) not null,
    currency varchar(3) not null,
    status varchar(20) not null default 'pending',
    created_at timestamptz not null default now()
)
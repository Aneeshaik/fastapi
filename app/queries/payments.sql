-- name: create_payment(amount, currency, status)<!
insert into payments (amount, currency, status)
values (:amount, :currency, :status)
returning id;

-- name: get_payment_by_id(payment_id)^
select id, amount, currency, status, created_at
from payments
where id = :payment_id;

-- name: list_payments()
select id, amount, currency, status, created_at
from payments
order by created_at
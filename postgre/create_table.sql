-- Table: public.bmi_calculator

-- DROP TABLE public.bmi_calculator;

CREATE TABLE public.bmi_calculator
(
    id integer NOT NULL DEFAULT nextval('bmi_calculator_id_seq'::regclass),
    min double precision,
    max double precision,
    message text COLLATE pg_catalog."default"
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.bmi_calculator
    OWNER to postgres;
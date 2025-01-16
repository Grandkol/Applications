CREATE TABLE public.application (
    id uuid NOT NULL,
    user_name character varying NOT NULL,
    description character varying NOT NULL,
    created_at timestamp with time zone DEFAULT now() NOT NULL
);
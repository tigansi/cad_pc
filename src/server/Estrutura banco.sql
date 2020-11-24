create table computadores
(
    id serial,
    nr_patrimonio  int unique not null,
    ip_computador  varchar(20) unique not null,
    tp_equipamento varchar(10) not null,
    is_alugado     varchar(30) not null,
    nm_dominio     varchar(100) not null,
    user_ad        varchar(40) not null,
    nm_user        varchar(100) not null,
    setor          varchar(100) not null,
    office         varchar(100) not null,
    prog_especial  text,
    tp_processador varchar(50) not null,
    mem_ram        varchar(10) not null,
    env_preventiva varchar(5) not null,
    rel_tecnico    text not null,
    is_ajustado    boolean default false
);
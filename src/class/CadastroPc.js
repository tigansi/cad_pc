function CadPc() {
    var nr_patrimonio;
    var ip_equipamento;
    var tp_equipamento;
    var is_alugado;
    var nm_dominio;
    var ad_user;
    var nm_user;
    var setor;
    var so;
    var office;
    var prog_especial;
    var tp_processador;
    var mem_ram;
    var is_hdd_ssd;
    var qtd_armazenamento;
    var env_preventiva;
    var rel_tecnico;

    this.setNrPatrimonio = function (value) {
        nr_patrimonio = value;
    };

    this.setIp_equipamento = function (value) {
        ip_equipamento = value;
    };

    this.setTp_equipamento = function (value) {
        tp_equipamento = value;
    };

    this.setIs_alugado = function (value) {
        is_alugado = value;
    };

    this.setNm_dominio = function (value) {
        nm_dominio = value;
    };

    this.setAd_user = function (value) {
        ad_user = value;
    };

    this.setNm_user = function (value) {
        nm_user = value;
    };

    this.setSetor = function (value) {
        setor = value;
    };
}
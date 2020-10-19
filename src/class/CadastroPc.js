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
        if (is_alugado == "") return false;
        else return true;
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

    this.setSo = function (value) {
        so = value;
    };

    this.setOffice = function (value) {
        office = value;
    };

    this.setProg_especial = function (value) {
        prog_especial = value;
    };

    this.setTp_processador = function (value) {
        tp_processador = value;
    };

    this.setMem_ram = function (value) {
        mem_ram = value;
    };

    this.setIs_hdd_ssd = function (value) {
        is_hdd_ssd = value;
    };

    this.setQtd_armazenamento = function (value) {
        qtd_armazenamento = value;
    };

    this.setEnv_preventiva = function (value) {
        env_preventiva = value;
    };

    this.setRel_tecnico = function (value) {
        rel_tecnico = value;
    };

    this.getNrPatrimonio = function () {
        return nr_patrimonio;
    };

    this.getIp_equipamento = function () {
        return ip_equipamento;
    };

    this.getTp_equipamento = function () {
        return tp_equipamento;
    };

    this.getIs_alugado = function () {
        return is_alugado;
    };

    this.getNm_dominio = function () {
        return nm_dominio;
    };

    this.getAd_user = function () {
        return ad_user;
    };

    this.getNm_user = function () {
        return nm_user;
    };

    this.getSetor = function () {
        return setor;
    };

    this.getSo = function () {
        return so;
    };

    this.getOffice = function () {
        return office;
    };

    this.getProg_especial = function () {
        return prog_especial;
    };

    this.getTp_processador = function () {
        return tp_processador;
    };

    this.getTp_processador = function () {
        return tp_processador;
    };

    this.getMem_ram = function () {
        return mem_ram;
    };

    this.getIs_hdd_ssd = function () {
        return is_hdd_ssd;
    };

    this.getQtd_armazenamento = function () {
        return qtd_armazenamento;
    };

    this.getEnv_preventiva = function () {
        return env_preventiva;
    };

    this.getRel_tecnico = function () {
        return rel_tecnico;
    };
}
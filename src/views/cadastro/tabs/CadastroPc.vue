<template>
  <ion-app>
    <ion-content>
      <ion-card style="background-color: white">
        <ion-card-content>
          <div id="form">
            <ion-list>
              <ion-item>
                <ion-label position="floating">Número patrimônio</ion-label>
                <IonInputVue type="tel" />
              </ion-item>

              <ion-item>
                <ion-label position="floating">Ip equipamento</ion-label>
                <IonInputVue type="tel" />
              </ion-item>

              <ion-item>
                <ion-label position="floating">Tipo de equipamento</ion-label>
                <IonSelectVue>
                  <ion-select-option value="PC">Computador</ion-select-option>
                  <ion-select-option value="NB">Notebook</ion-select-option>
                </IonSelectVue>
              </ion-item>

              <ion-item>
                <ion-label position="floating">Wih ou Vivo</ion-label>
                <IonSelectVue>
                  <ion-select-option value="Wih">Wih</ion-select-option>
                  <ion-select-option value="Vivo">Vivo</ion-select-option>
                  <ion-select-option value="EP">Próprio</ion-select-option>
                  <ion-select-option value="NS">Não sei</ion-select-option>
                </IonSelectVue>
              </ion-item>

              <ion-item>
                <ion-label position="floating">Nome do domínio</ion-label>
                <IonInputVue />
              </ion-item>

              <ion-item>
                <ion-label position="floating">Usuário(a) AD</ion-label>
                <IonInputVue />
              </ion-item>

              <ion-item>
                <ion-label position="floating">Nome do usuário(a)</ion-label>
                <IonInputVue />
              </ion-item>

              <ion-item>
                <ion-label position="floating">Setor</ion-label>
                <IonSelectVue>
                  <ion-select-option value="Auditoria"
                    >Auditoria</ion-select-option
                  >
                  <ion-select-option value="Autorizações"
                    >Autorizações</ion-select-option
                  >
                  <ion-select-option value="Cadastro"
                    >Cadastro</ion-select-option
                  >
                  <ion-select-option value="Compras">Compras</ion-select-option>
                  <ion-select-option value="Comercial"
                    >Comercial</ion-select-option
                  >

                  <ion-select-option value="Contabilidade"
                    >Contabilidade</ion-select-option
                  >
                  <ion-select-option value="Contas">Contas</ion-select-option>
                  <ion-select-option value="Controladoria"
                    >Controladoria</ion-select-option
                  >
                  <ion-select-option value="Diretoria"
                    >Diretoria</ion-select-option
                  ><ion-select-option value="Faturamento"
                    >Faturamento</ion-select-option
                  ><ion-select-option value="Financeiro"
                    >Financeiro</ion-select-option
                  ><ion-select-option value="Gp"
                    >Gestão de pessoas</ion-select-option
                  ><ion-select-option value="Intercâmbio"
                    >Intercâmbio</ion-select-option
                  >
                  <ion-select-option value="Jurídico"
                    >Jurídico</ion-select-option
                  >
                  <ion-select-option value="MKT">MKT</ion-select-option>
                  <ion-select-option value="NAIS">NAIS</ion-select-option>
                  <ion-select-option value="Regulação"
                    >Regulação</ion-select-option
                  >
                  <ion-select-option value="Relcli"
                    >Rel. cliente</ion-select-option
                  >
                  <ion-select-option value="Relcoop"
                    >Rel. coop</ion-select-option
                  >
                  <ion-select-option value="Relprest"
                    >Rel. prest</ion-select-option
                  >
                  <ion-select-option value="secretaria"
                    >Secretaria</ion-select-option
                  >
                  <ion-select-option value="TIC">TIC</ion-select-option>
                </IonSelectVue>
              </ion-item>

              <ion-item>
                <ion-label position="floating">Sistema operacional</ion-label>
                <IonSelectVue>
                  <ion-select-option value="Windows 10 Pro"
                    >Windows 10 Pro</ion-select-option
                  >
                  <ion-select-option value="Windows 7 Pro"
                    >Windows 7 Pro</ion-select-option
                  >
                  <ion-select-option value="Windows 8.1 Pro"
                    >Windows 8.1 Pro</ion-select-option
                  >
                  <ion-select-option value="Windows XP Pro"
                    >Windows XP Pro</ion-select-option
                  ><ion-select-option value="Windows Vista Business"
                    >Windows Vista Business</ion-select-option
                  >
                </IonSelectVue>
              </ion-item>

              <ion-item>
                <ion-label position="floating">Pacote office</ion-label>
                <IonSelectVue>
                  <ion-select-option value="Office 2003 Pro"
                    >Office 2003 Pro</ion-select-option
                  >
                  <ion-select-option value="Office 2007"
                    >Office 2007</ion-select-option
                  >
                  <ion-select-option value="2010 Home and Business"
                    >2010 Home and Business</ion-select-option
                  ><ion-select-option value="2013 Home and Business"
                    >2013 Home and Business</ion-select-option
                  >
                  <ion-select-option value="2013 Pro"
                    >2013 Pro</ion-select-option
                  >
                  <ion-select-option value="2016 Home and Business"
                    >2016 Home and Business</ion-select-option
                  ><ion-select-option value="2016 Pro"
                    >2016 Pro</ion-select-option
                  >
                  <ion-select-option value="2016 Professional Plus"
                    >2016 Professional Plus</ion-select-option
                  >
                  <ion-select-option value="2019 Home and Business"
                    >2019 Home and Business</ion-select-option
                  ><ion-select-option value="2019 Pro"
                    >2019 Pro</ion-select-option
                  >
                  <ion-select-option value="Não possui"
                    >Não possui</ion-select-option
                  >
                </IonSelectVue>
              </ion-item>

              <ion-item>
                <ion-label position="floating">Programas especiais</ion-label>
                <IonTextareaVue
                  placeholder="Ex.: O computador Possui licença dos programas de edição da Adobe"
                ></IonTextareaVue>
              </ion-item>

              <ion-item>
                <ion-label position="floating">Tipo de processador</ion-label>
                <IonSelectVue>
                  <ion-select-option value="i7"
                    >Intel core i7</ion-select-option
                  >
                  <ion-select-option value="i5"
                    >Intel core i5</ion-select-option
                  >
                  <ion-select-option value="i3"
                    >Intel core i3</ion-select-option
                  >
                  <ion-select-option value="2quad"
                    >Intel core 2 quad</ion-select-option
                  >
                  <ion-select-option value="Pentium"
                    >Intel Pentium</ion-select-option
                  >
                  <ion-select-option value="Nenhum da lista"
                    >Nenhum da lista</ion-select-option
                  >
                </IonSelectVue>
              </ion-item>

              <ion-item>
                <ion-label position="floating">Memória Ram</ion-label>
                <IonInputVue />
              </ion-item>

              <ion-item>
                <ion-label position="floating">HDD ou SSD</ion-label>
                <IonSelectVue>
                  <ion-select-option value="HDD">HDD</ion-select-option>
                  <ion-select-option value="SSD">SSD</ion-select-option>
                </IonSelectVue>
              </ion-item>

              <ion-item>
                <ion-label position="floating"
                  >Quantidade de armazenamento</ion-label
                >
                <IonInputVue />
              </ion-item>

              <ion-item>
                <ion-label position="floating"
                  >Encaminhar para preventiva</ion-label
                >
                <IonSelectVue>
                  <ion-select-option value="s">Sim</ion-select-option>
                  <ion-select-option value="n">Não</ion-select-option>
                </IonSelectVue>
              </ion-item>

              <ion-item>
                <ion-label position="floating">Relato técnico</ion-label>
                <IonTextareaVue
                  placeholder="Ex.: O computador necessita de formatação e limpeza"
                ></IonTextareaVue>
              </ion-item>
              <br />

              <ion-button
                id="btn_cadastrar"
                class="btn"
                expand="block"
                shape="round"
                >Cadastrar informações</ion-button
              >
            </ion-list>
          </div>
        </ion-card-content>
      </ion-card>
    </ion-content>
  </ion-app>
</template>

<script>
export default {
  data() {
    return {
      form: {
        nr_patrimonio: "",
        ip_equipamento: "",
        tp_equipamento: "",
        is_alugado: "",
        nm_dominio: "",
        ad_user: "",
        nm_user: "",
        setor: "",
        so: "",
        office: "",
        prog_especial: "",
        tp_processador: "",
        mem_ram: "",
        is_hdd_ssd: "",
        qtd_armazenamento: "",
        env_preventiva: false,
        rel_tecnico: "",
      },
    };
  },
  methods: {
    cadastraDados() {
      try {
        console.log("teste1");
      } catch (error) {
        console.log(error);
      }
    },
  },
};
</script>

<style>
#btn_cadastrar {
  --background: #f47920;
  font-weight: bold;
}

#btn_prog {
  --background: rgb(177, 211, 75);
  font-weight: bold;
}
</style>

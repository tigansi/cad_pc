<template>
  <ion-app>
    <ion-content>
      <ion-card style="background-color: white">
        <ion-card-content>
          <div id="form">
            <ion-list>
              <ion-item>
                <ion-label position="floating">Número patrimônio</ion-label>
                <IonInputVue v-model="form.nr_patrimonio" type="tel" />
              </ion-item>

              <ion-item>
                <ion-label position="floating">Ip equipamento</ion-label>
                <IonInputVue v-model="form.ip_equipamento" type="tel" />
              </ion-item>

              <ion-item>
                <ion-label position="floating">Tipo de equipamento</ion-label>
                <IonSelectVue v-model="form.tp_equipamento">
                  <ion-select-option value="PC">Computador</ion-select-option>
                  <ion-select-option value="NB">Notebook</ion-select-option>
                </IonSelectVue>
              </ion-item>

              <ion-item>
                <ion-label position="floating">Wih ou Vivo</ion-label>
                <IonSelectVue v-model="form.is_alugado">
                  <ion-select-option value="Wih">Wih</ion-select-option>
                  <ion-select-option value="Vivo">Vivo</ion-select-option>
                  <ion-select-option value="EP">Próprio</ion-select-option>
                  <ion-select-option value="NS">Não sei</ion-select-option>
                </IonSelectVue>
              </ion-item>

              <ion-item>
                <ion-label position="floating">Nome do domínio</ion-label>
                <IonInputVue v-model="form.nm_dominio" />
              </ion-item>

              <ion-item>
                <ion-label position="floating">Usuário(a) AD</ion-label>
                <IonInputVue v-model="form.ad_user" />
              </ion-item>

              <ion-item>
                <ion-label position="floating">Nome do usuário(a)</ion-label>
                <IonInputVue v-model="form.nm_user" />
              </ion-item>

              <ion-item>
                <ion-label position="floating">Setor</ion-label>
                <IonSelectVue v-model="form.setor">
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
                <IonSelectVue v-model="form.so">
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
                <IonSelectVue v-model="form.office">
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
                  v-model="form.prog_especial"
                  style="font-family: 'Montserrat', sans-serif"
                  placeholder="Ex.: O computador Possui licença dos programas de edição da Adobe"
                ></IonTextareaVue>
              </ion-item>

              <ion-item>
                <ion-label position="floating">Tipo de processador</ion-label>
                <IonSelectVue v-model="form.tp_processador">
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
                <IonInputVue v-model="form.mem_ram" />
              </ion-item>

              <ion-item>
                <ion-label position="floating">HDD ou SSD</ion-label>
                <IonSelectVue v-model="form.is_hdd_ssd">
                  <ion-select-option value="HDD">HDD</ion-select-option>
                  <ion-select-option value="SSD">SSD</ion-select-option>
                </IonSelectVue>
              </ion-item>

              <ion-item>
                <ion-label position="floating"
                  >Quantidade de armazenamento</ion-label
                >
                <IonInputVue v-model="form.qtd_armazenamento" />
              </ion-item>

              <ion-item>
                <ion-label position="floating"
                  >Encaminhar para preventiva</ion-label
                >
                <IonSelectVue v-model="form.env_preventiva">
                  <ion-select-option value="s">Sim</ion-select-option>
                  <ion-select-option value="n">Não</ion-select-option>
                </IonSelectVue>
              </ion-item>

              <ion-item>
                <ion-label position="floating">Relato técnico</ion-label>
                <IonTextareaVue
                  v-model="form.rel_tecnico"
                  style="font-family: 'Montserrat', sans-serif"
                  placeholder="Ex.: O computador necessita de formatação e limpeza"
                ></IonTextareaVue>
              </ion-item>
              <br />

              <ion-button
                id="btn_cadastrar"
                class="btn"
                expand="block"
                shape="round"
                @click="cadastraDados"
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
import Provider from "../../../services/provider";
import { loadingController } from "@ionic/core";
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
    async cadastraDados() {
      try {
        const loading = await loadingController.create({
          cssClass: "my-custom-class",
          message: "Um momento...",
        });
        loading.present();

        let dados = {
          tipo: "cad_pc",
          nr_patrimonio: this.form.nr_patrimonio,
          ip_equipamento: this.form.ip_equipamento,
          tp_equipamento: this.form.tp_equipamento,
          is_alugado: this.form.is_alugado,
          nm_dominio: this.form.nm_dominio,
          ad_user: this.form.ad_user,
          nm_user: this.form.nm_user,
          setor: this.form.setor,
          so: this.form.so,
          office: this.form.office,
          prog_especial: this.form.prog_especial,
          tp_processador: this.form.tp_processador,
          mem_ram: this.form.mem_ram,
          is_hdd_ssd: this.form.is_hdd_ssd,
          qtd_armazenamento: this.form.qtd_armazenamento,
          env_preventiva: this.form.env_preventiva,
          rel_tecnico: this.form.rel_tecnico,
        };

        Provider.provider("computador", JSON.stringify(dados))
          .then((res) => {
            console.log(res.data.msg);
            if (res.data.sucesso) {
              loading.dismiss();
              //this.form = null;
              this.presentToast(res.data.msg);
              setTimeout(function () {
                location.reload();
              }, 2000);
            } else {
              loading.dismiss();
            }
          })
          .catch((error) => {
            loading.dismiss();
            this.presentToast(
              "Ocorreu um erro com o servidor. Contate o suporte"
            );
            console.log("TIMEOUT " + error);
          });
      } catch (error) {
        console.log(error);
      }
    },
    async presentToast(msg) {
      const toast = document.createElement("ion-toast");
      toast.message = msg;
      toast.duration = 2000;
      toast.position = "top";

      document.body.appendChild(toast);
      return toast.present();
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

ion-toast {
  /*color: white;*/
  text-align: center;
  --background: rgb(177, 211, 75);
  color: white;
  font-weight: bold;
}
</style>

<template>
  <ion-app>
    <ion-content>
      <ion-card style="background-color: white">
        <ion-card-header>
          <ion-card-subtitle class="ion-text-center">
            Escolha um dos filtros
          </ion-card-subtitle>
        </ion-card-header>
        <ion-card-content>
          <ion-list id="form">
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
              <ion-label position="floating">Setor</ion-label>
              <IonSelectVue>
                <ion-select-option value="Auditoria"
                  >Auditoria</ion-select-option
                >
                <ion-select-option value="Autorizações"
                  >Autorizações</ion-select-option
                >
                <ion-select-option value="Cadastro">Cadastro</ion-select-option>
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
                <ion-select-option value="Jurídico">Jurídico</ion-select-option>
                <ion-select-option value="MKT">MKT</ion-select-option>
                <ion-select-option value="NAIS">NAIS</ion-select-option>
                <ion-select-option value="Regulação"
                  >Regulação</ion-select-option
                >
                <ion-select-option value="Relcli"
                  >Rel. cliente</ion-select-option
                >
                <ion-select-option value="Relcoop">Rel. coop</ion-select-option>
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
              <ion-label position="floating">Ip equipamento</ion-label>
              <IonInputVue type="tel" />
            </ion-item>
          </ion-list>

          <br />
          <ion-button id="btn_buscar" expand="block"
            >Buscar informações</ion-button
          >
        </ion-card-content>
      </ion-card>

      <ion-card style="background-color: white">
        <ion-card-content></ion-card-content>
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
      formPesq: {
        tp_equipamento: "",
        is_alugado: "",
        setor: "",
        ip_equipamento: "",
      },
    };
  },
  methods: {
    async pesqFiltro() {
      const loading = await loadingController.create({
        cssClass: "my-custom-class",
        message: "Um momento...",
      });
      loading.present();

      let dados = {
        tipo: "list_pc_filtro",
        tp_equipamento: this.formPesq.tp_equipamento,
        is_alugado: this.formPesq.is_alugado,
        setor: this.formPesq.setor,
        ip_equipamento: this.formPesq.ip_equipamento,
      };

      Provider.provider("computador", JSON.stringify(dados))
        .then((res) => {
          if (res.data.sucesso) {
            //
          }
        })
        .catch((error) => {
          loading.dismiss();
          this.presentToast(
            "Ocorreu um erro com o servidor. Contate o suporte"
          );
          console.log("TIMEOUT " + error);
        });
    },
  },
};
</script>


<style>
#btn_buscar {
  --background: #f47920;
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
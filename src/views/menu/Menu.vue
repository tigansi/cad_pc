<template>
  <ion-app>
    <ion-content>
      <ion-card>
        <ion-card-header id="header">
          <ion-card-subtitle>Unimed Pelotas</ion-card-subtitle>
          <ion-card-title>Suporte</ion-card-title>
        </ion-card-header>
      </ion-card>

      <ion-card>
        <ion-card-content>
          <div class="ion-text-center">Melhoria ou reparo das máquinas</div>

          <center>
            <ion-grid>
              <ion-row>
                <ion-col size-sm>
                  <div
                    class="box"
                    @click="direcionaView('/HomeCadastro/CadastroPC')"
                  >
                    <ion-icon name="add-circle"></ion-icon><br />
                    Avaliação das máquinas
                  </div>
                </ion-col>
                <!--<ion-col size-sm>
                  <div class="box">
                    <ion-icon name="server"></ion-icon><br />
                    Avaliação dos servidores
                  </div>
                </ion-col>-->
              </ion-row>
            </ion-grid>
          </center>
        </ion-card-content>
      </ion-card>

      <ion-card>
        <ion-card-content>
          <div class="ion-text-center">Opções de checklist</div>
          <center>
            <ion-grid>
              <ion-row>
                <ion-col size="6" size-sm>
                  <div class="box">
                    <ion-icon name="construct"></ion-icon><br />
                    Preventiva PC's
                  </div>
                </ion-col>
                <!--<ion-col size="6" size-sm>
                  <div class="box">
                    <ion-icon name="construct"></ion-icon><br />
                    Preventiva Serviores
                  </div>
                </ion-col>-->
                <ion-col size="6" size-sm>
                  <div class="box">
                    <ion-icon name="desktop"></ion-icon><br />
                    Notebooks de Empréstimo
                  </div>
                </ion-col>
              </ion-row>
            </ion-grid>
          </center>
        </ion-card-content>
      </ion-card>

      <ion-card>
        <ion-card-content>
          <div class="ion-text-center">Comandos auxiliares</div>
          <center>
            <ion-grid>
              <ion-row>
                <ion-col size-sm>
                  <div class="box">
                    <ion-icon name="refresh-circle"></ion-icon><br />
                    Reiniciar um computador
                  </div>
                </ion-col>
                <ion-col size-sm>
                  <div class="box">
                    <ion-icon name="lock-closed"></ion-icon><br />
                    Revelar senha de usuário
                  </div>
                </ion-col>
              </ion-row>
            </ion-grid>
          </center>
        </ion-card-content>
      </ion-card>
    </ion-content>
    <ion-footer>
      <ion-toolbar id="footer">
        <ion-title>Checklists</ion-title>
      </ion-toolbar>
    </ion-footer>
  </ion-app>
</template>

<script>
import { addIcons } from "ionicons";
import {
  construct,
  desktop,
  addCircle,
  refreshCircle,
  lockClosed,
  server,
} from "ionicons/icons";

addIcons({
  "md-construct": construct,
  "md-desktop": desktop,
  "md-add-circle": addCircle,
  "md-refresh-circle": refreshCircle,
  "md-lock-closed": lockClosed,
  "md-server": server,
});
export default {
  methods: {
    direcionaView(pag) {
      this.$router.push(pag);
    },
  },
};
</script>


<style>
.box {
  transition: box-shadow 0.3s;
  width: 120px;
  height: 90px;
  /*margin: 50px;*/
  border-radius: 10px;
  border: 1px solid #ccc;
  background: #fff;
  /*float: left;*/
  padding: 8px;
  text-align: center;
  color: #00995d;
}
.box:hover {
  box-shadow: 0 0 11px rgba(33, 33, 33, 0.2);
}

.box ion-icon {
  color: rgb(177, 211, 75);
}

#footer,
#header {
  --color: white;
  --background: #00995d;
  font-weight: bold;
}

#header ion-card-subtitle,
#header ion-card-title {
  color: white;
}
</style>
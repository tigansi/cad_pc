<template>
  <ion-app>
    <ion-content>
      <ion-tabs>
        <ion-tab tab="CadastroPc" :routes="['CadastroPc']">
          <CadastroPc />
        </ion-tab>
        <ion-tab tab="CadastroGeral" :routes="['CadastroGeral']">
          <CadastroGeral />
        </ion-tab>

        <ion-tab-bar slot="bottom">
          <ion-tab-button
            tab="CadastroPc"
            class="btn-tab"
            :to="{ name: 'CadastroPc' }"
          >
            <ion-icon name="add-circle"></ion-icon>
            <ion-label>Computador</ion-label>
          </ion-tab-button>

          <ion-tab-button
            tab="CadastroGeral"
            class="btn-tab"
            :to="{ name: 'CadastroGeral' }"
          >
            <ion-icon name="grid"></ion-icon>
            <ion-label>Geral</ion-label>
          </ion-tab-button>
        </ion-tab-bar>
      </ion-tabs>
    </ion-content>
  </ion-app>
</template>

<script>
import CadastroPc from "./tabs/CadastroPc";
import CadastroGeral from "./tabs/CadastroGeral";
import { addIcons } from "ionicons";
import { addCircle, settings, grid } from "ionicons/icons";

addIcons({
  "md-add-circle": addCircle,
  "md-settings": settings,
  "md-grid": grid,
});

export default {
  components: {
    CadastroPc,
    CadastroGeral,
  },
};
</script>

<style>
#form ion-label {
 font-size: 17.5px;
 font-weight: bold;
  font-family: "Montserrat", sans-serif;
}

#form input {
  font-family: "Montserrat", sans-serif;
}

ion-tab-bar {
  --color: white;
  --background: #00995d;
}

ion-tab-button.btn-tab {
  --color-selected: rgb(177, 211, 75);
  font-weight: bold;
}
</style>
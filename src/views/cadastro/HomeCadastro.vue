<template>
  <ion-app>
    <ion-header>
      <ion-toolbar id="header">
        <ion-buttons slot="start">
          <ion-button @click="menu">
            <ion-icon
              slot="icon-only"
              name="arrow-back-circle-sharp"
            ></ion-icon>
          </ion-button>
        </ion-buttons>
        <ion-title>Unimed Pelotas</ion-title>
      </ion-toolbar>
    </ion-header>
    <ion-content>
      <ion-tabs>
        <ion-tab tab="CadastroPc" :routes="['CadastroPc']">
          <CadastroPc />
        </ion-tab>

        <ion-tab tab="ListagemPc" :routes="['ListagemPc']">
          <ListagemPc />
        </ion-tab>

        <ion-tab-bar slot="bottom">
          <ion-tab-button
            tab="CadastroPc"
            class="btn-tab"
            :to="{ name: 'CadastroPc' }"
          >
            <ion-icon name="add-circle"></ion-icon>
            <ion-label>Máquinas</ion-label>
          </ion-tab-button>

          <ion-tab-button
            tab="ListagemPc"
            class="btn-tab"
            :to="{ name: 'ListagemPc' }"
          >
            <ion-icon name="newspaper"></ion-icon>
            <ion-label>Listagem</ion-label>
          </ion-tab-button>
        </ion-tab-bar>
      </ion-tabs>
    </ion-content>
  </ion-app>
</template>

<script>
import CadastroPc from "./tabs/CadastroPc";
import ListagemPc from "./tabs/ListagemPc";
import { addIcons } from "ionicons";
import {
  addCircle,
  settings,
  grid,
  newspaper,
  arrowBackCircleSharp,
} from "ionicons/icons";

addIcons({
  "md-add-circle": addCircle,
  "md-settings": settings,
  "md-grid": grid,
  "md-newspaper": newspaper,
  "md-arrow-back-circle-sharp": arrowBackCircleSharp,
});

export default {
  components: {
    CadastroPc,

    ListagemPc,
  },
  data() {
    return {};
  },
  methods: {
    menu() {
      this.$router.push("/Menu");
    },
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

#header {
  --background: #00995d;
  color: white;
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
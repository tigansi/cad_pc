<template>
  <ion-app>
    <ion-header>
      <ion-toolbar id="header">
        <ion-title>Unimed Pelotas</ion-title>
      </ion-toolbar>
    </ion-header>
    <ion-content>
      <ion-card style="background-color: white">
        <ion-card-content>
          <div id="form">
            <ion-list>
              <ion-item>
                <ion-label position="floating">Número patrimônio</ion-label>
                <IonInputVue />
              </ion-item>

              <ion-item>
                <ion-label position="floating">Ip equipamento</ion-label>
                <IonInputVue />
              </ion-item>

              <ion-item>
                <ion-label position="floating">Tipo de equipamento</ion-label>
                <IonSelectVue>
                  <ion-select-option value="cats">Cats</ion-select-option>
                  <ion-select-option value="dogs">Dogs</ion-select-option>
                </IonSelectVue>
              </ion-item>

              <ion-item>
                <ion-label position="floating">Wih</ion-label>
                <IonSelectVue>
                  <ion-select-option value="cats">Cats</ion-select-option>
                  <ion-select-option value="dogs">Dogs</ion-select-option>
                </IonSelectVue>
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
                  <ion-select-option value="cats">Cats</ion-select-option>
                  <ion-select-option value="dogs">Dogs</ion-select-option>
                </IonSelectVue>
              </ion-item>

              <ion-item>
                <ion-label position="floating">Sistema operacional</ion-label>
                <IonSelectVue>
                  <ion-select-option value="cats">Cats</ion-select-option>
                  <ion-select-option value="dogs">Dogs</ion-select-option>
                </IonSelectVue>
              </ion-item>

              <ion-item>
                <ion-label position="floating">Pacote office</ion-label>
                <IonSelectVue>
                  <ion-select-option value="cats">Cats</ion-select-option>
                  <ion-select-option value="dogs">Dogs</ion-select-option>
                </IonSelectVue>
              </ion-item>

              <ion-item>
                <ion-label position="floating">Tipo de processador</ion-label>
                <IonSelectVue>
                  <ion-select-option value="cats">Cats</ion-select-option>
                  <ion-select-option value="dogs">Dogs</ion-select-option>
                </IonSelectVue>
              </ion-item>

              <ion-item>
                <ion-label position="floating">Memória Ram</ion-label>
                <IonInputVue />
              </ion-item>

              <ion-item>
                <ion-label position="floating">HDD ou SSD</ion-label>
                <IonSelectVue>
                  <ion-select-option value="cats">Cats</ion-select-option>
                  <ion-select-option value="dogs">Dogs</ion-select-option>
                </IonSelectVue>
              </ion-item>

              <ion-item>
                <ion-label position="floating"
                  >Quantidade de armazenamento</ion-label
                >
                <IonInputVue />
              </ion-item>
            </ion-list>
          </div>
        </ion-card-content>
      </ion-card>

      <ion-card style="background-color: white">
        <ion-card-header>
          <ion-card-subtitle class="ion-text-center"
            >Escolha os programas específicos</ion-card-subtitle
          >
        </ion-card-header>
        <ion-card-content>
          <ion-grid>
            <ion-row>
              <div>
                <ion-col>
                  <ion-button id="btn_prog" shape="round" class="btn"
                    >Tasy</ion-button
                  >
                </ion-col>
                <ion-col>
                  <ion-button id="btn_prog" shape="round" class="btn"
                    >PhotoShop</ion-button
                  >
                </ion-col>
                <ion-col>
                  <ion-button id="btn_prog" shape="round" class="btn"
                    >Corel</ion-button
                  >
                </ion-col>
                <ion-col>
                  <ion-button id="btn_prog" shape="round" class="btn"
                    >Certificado</ion-button
                  >
                </ion-col>
                <ion-col>
                  <ion-button id="btn_prog" shape="round" class="btn"
                    >Sicadin</ion-button
                  >
                </ion-col>
                <ion-col>
                  <ion-button id="btn_prog" shape="round" class="btn"
                    >Webstart</ion-button
                  >
                </ion-col>
                <ion-col>
                  <ion-button id="btn_prog" shape="round" class="btn"
                    >PTA</ion-button
                  >
                </ion-col>
              </div>
            </ion-row>
          </ion-grid>
        </ion-card-content>
      </ion-card>

      <ion-card style="background-color: white">
        <ion-card-header>
          <ion-card-subtitle class="ion-text-center"
            >Programas escolhidos</ion-card-subtitle
          >
        </ion-card-header>
        <ion-card-content> </ion-card-content>
      </ion-card>

      <ion-card style="background-color: white">
        <ion-card-content>
          <ion-label position="floating">Relato técnico</ion-label>
          <IonTextareaVue></IonTextareaVue>

          <ion-button
            id="btn_cadastrar"
            class="btn"
            expand="block"
            shape="round"
            >Cadastrar informações</ion-button
          >
        </ion-card-content>
      </ion-card>
    </ion-content>
  </ion-app>
</template>

<style>
#header {
  --background: #00995d;
  color: white;
  
}

#btn_cadastrar {
  --background: #f47920;
  font-weight: bold;
}

#btn_prog {
  --background: rgb(177, 211, 75);
  font-weight: bold;
}
</style>

<template>
  <ion-app>
    <ion-content>
      <ion-card>
        <ion-card-header>
          <ion-card-subtitle>Unimed Pelotas</ion-card-subtitle>
          <ion-card-title>Suporte</ion-card-title>
        </ion-card-header>
      </ion-card>

      <ion-card>
        <ion-card-content>
          <div class="ion-text-center">Escolha um tipo de checklist</div>
          <center>
            <ion-grid>
              <ion-row>
                <ion-col size="6" size-sm>
                  <div class="box">
                    <ion-icon name="person"></ion-icon><br />
                    Notebooks de Empréstimo
                  </div>
                </ion-col>

                <ion-col size="6" size-sm>
                  <div class="box">
                    <ion-icon name="calendar"></ion-icon><br />
                    Manutenção preventiva
                  </div>
                </ion-col>
              </ion-row>
            </ion-grid>
          </center>
        </ion-card-content>
      </ion-card>
    </ion-content>
  </ion-app>
</template>


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
  color: rgb(133, 100, 4);
}
.box:hover {
  box-shadow: 0 0 11px rgba(33, 33, 33, 0.2);
}
</style>
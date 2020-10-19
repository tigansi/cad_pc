# cad_pc

- Projeto que tem o objetivo de auxiliar a TI no mapeamento de computadores e dispositivos computacionais da cooperativa.

## Observações do desenvolvedor
* Desenvolvedor: Tiago Igansi
* Data de criação: 07/10/2020
* Linguagem: VueJS e Pyhon3
* Versão: 1.0

## Dependências
* Python3 ou superior;
* Flask;
* flask_cors;
* @vue/cli 4.4.6 ou superior;
* Ionic 5;
* PostgreSql;

## Configuração
* Para o projeto funcionar, é necessário realizar algumas configurações,
    * instalar o flask 
        * python -m pip install flask
    * instalar o flask CORS
        * python -m pip install flask_cors
    * instalar o psycopg2 para trabalhar com banco
        * python -m pip install psycopg2
    * dentro da pasta do projeto abra o terminal e execute os comandos
        * vue add router
        * npm install @ionic/core
        * npm install @ionic/vue@0.0.9
        * npm install ionicons
        * npm install v-mask
        * npm install --save axios vue-axios
    * no arquivo main.js, adicione as seguintes linhas
        * import Ionic from "@ionic/vue
        * import "@ionic/core/css/ionic.bundle.css"
        * import VueMask from "v-mask"
        * import { VueMaskDirective } from "v-mask"
        * import { VueMaskFilter } from "v-mask"
    * após as declaraçãoes acima, é necessário ativá-las:
        * Vue.use(Ionic)
        * Vue.directive("mask", VueMaskDirective)
        * Vue.filter("VMask", VueMaskFilter)
        * Vue.use(VueMask)
    * deve ocorrer algumas alterações nas rotas, na pasta router, em index.js
        * import { IonicVueRouter } from "@ionic/vue";
        * Vue.use(IonicVueRouter);
        * const router = new IonicVueRouter({routes})
    * Em public/index.html, dentro da tag  é necessário estabelecer o mode, são eles o IOS e o MD;
    * No App.vue, ná área de template é preciso usar em #app, ao invés de router-view, ion-vue-router;
    Para usar os inputs do Ionic com o vue, é necessário consultar as informações no final da página abaixo:
        * https://programmer.help/blogs/v-model-and-ionic4-component-data-binding-failed.html

## Funcionamento do sistema
* Possui um menu onde o usuário pode escolher as opções várias escolhas, como mostra abaixo:
    * Cadastrar computadores para avaliação(preventiva)
    * Escolher um das versões de checklist, Preventiva(cadastrado no item anterior) ou de empréstimo de notebooks
    * Comandos auxiliares, como por exempo,
    reiniciar um computadore remoto o descobrir a senha de um usuário
* Na área de cadastro para avaliação o técnico possui um formulário, que terá que ser preenchido com algumas informações, como no caso de: 
    * ip 
    * número de série
    * sistema operacional
    * quantidade de RAM e armazenamento
    * se o armezanamento é em SSD
    * relato técnico e dentre outras coisas 


## Novidades

## Correções

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

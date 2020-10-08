import Vue from "vue";
import { IonicVueRouter } from "@ionic/vue";

Vue.use(IonicVueRouter);

const routes = [
  {
    path: "/HomeCadastro",
    name: "HomeCadastro",
    component: () => import("@/views/cadastro/HomeCadastro.vue"),
    children: [
      {
        path: "CadastroPc",
        name: "CadastroPc",
        components: {
          tabCadastroPc: () => import("@/views/cadastro/tabs/CadastroPc"),
        },
      },
      {
        path: "CadastroSetor",
        name: "CadastroSetor",
        components: {
          tabCadastroSetor: () => import("@/views/cadastro/tabs/CadastroSetor"),
        },
      },
    ],
  },
  {
    path: "/",
    redirect: "HomeCadastro/CadastroPc",
  },
];

const router = new IonicVueRouter({
  routes,
});

export default router;

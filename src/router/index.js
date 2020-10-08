import Vue from "vue";
import { IonicVueRouter } from "@ionic/vue";

Vue.use(IonicVueRouter);

const routes = [
  {
    path: "/Menu",
    name: "Menu",
    component: () => import("@/views/menu/Menu.vue"),
  },
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
        name: "CadastroGeral",
        components: {
          tabCadastroGeral: () => import("@/views/cadastro/tabs/CadastroGeral"),
        },
      },
    ],
  },
  {
    path: "/",
    redirect: "Menu",
  },
];

const router = new IonicVueRouter({
  routes,
});

export default router;

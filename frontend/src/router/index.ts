import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import HomeView from "@/views/HomeView.vue";
import AboutView from "@/views/AboutView.vue";
import InputView from "@/views/InputView.vue";
import OutputView from "@/views/OutputView.vue";
import MemberView from "@/views/MemberView.vue";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/about",
    name: "about",
    component: AboutView,
  },
  {
    path: "/input",
    name: "input",
    component: InputView,
  },
  {
    path: "/output",
    name: "output",
    component: OutputView,
  },
  {
    path: "/member",
    name: "menber",
    component: MemberView,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;

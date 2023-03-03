<template>
  <v-app>
    <header-main />
    <v-main>
      <router-view />
    </v-main>
    <footer-component></footer-component>
  </v-app>
</template>

<script lang="ts">
import { Options, Vue } from "vue-property-decorator";
import HeaderMain from "@/components/HeaderMain.vue";
import FooterComponent from "@/components/FooterComponent.vue";

@Options({
  components: {
    HeaderMain,
    FooterComponent,
  },
})
export default class App extends Vue {}
</script>
<style></style>

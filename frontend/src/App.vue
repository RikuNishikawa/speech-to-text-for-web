<template>
  <v-app class="font">
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

<style>
.font {
  font-family: "02うつくし明朝体";
  max-width: 1200px;
  margin: 0 auto;
}
</style>

<template>
  <v-app>
    <v-main>
      <header-main />
      <input-main />
      <input-footer />
    </v-main>
  </v-app>
</template>

<script lang="ts">
import { Options, Vue } from "vue-property-decorator";
import TestPage from "@/components/TestPage.vue"; // @ is an alias to /src
import HeaderMain from "@/components/HeaderMain.vue"; // @ is an alias to /src
import InputMain from "@/components/InputMain.vue"; // @ is an alias to /src
import InputFooter from "@/components/InputFooter.vue"; // @ is an alias to /src

@Options({
  components: {
    TestPage,
    HeaderMain,
    InputMain,
    InputFooter,
  },
})
export default class InputView extends Vue {}
</script>

<style></style>

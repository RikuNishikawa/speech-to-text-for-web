<template>
  <v-app>
    <v-main>
      <header-main />
    </v-main>
  </v-app>
</template>

<script lang="ts">
import { Options, Vue } from "vue-property-decorator";
import TestPage from "@/components/TestPage.vue"; // @ is an alias to /src
import HeaderMain from "@/components/HeaderMain.vue"; // @ is an alias to /src

@Options({
  components: {
    TestPage,
    HeaderMain,
  },
})
export default class InputView extends Vue {}
</script>

<style></style>

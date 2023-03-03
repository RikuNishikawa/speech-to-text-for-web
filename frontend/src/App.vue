<template>
  <v-app>
    <header-main />
    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script lang="ts">
import { Options, Vue } from "vue-property-decorator";
import HeaderMain from "@/components/HeaderMain.vue";
import InputHeader from "@/components/InputHeader.vue";

@Options({
  components: {
    HeaderMain,
    InputHeader,
  },
})
export default class App extends Vue {}
</script>
<style></style>

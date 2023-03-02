<template>
  <v-app>
    <v-main>
      <header-item />
      <router-view />
    </v-main>
  </v-app>
</template>

<script lang="ts">
import HeaderItem from "@/components/HeaderItem.vue";
import { Options, Vue } from "vue-property-decorator";

@Options({
  components: {
    HeaderItem,
  },
})
export default class App extends Vue {}
</script>

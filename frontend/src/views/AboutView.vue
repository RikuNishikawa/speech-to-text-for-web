<template>
  <div class="about">
    <h1>This is an about page</h1>
    <h2>Click Test</h2>
  </div>
  <test-page />
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import TestPage from "@/components/TestPage.vue"; // @ is an alias to /src

@Options({
  components: {
    TestPage,
  },
})
export default class HomeView extends Vue {}
</script>

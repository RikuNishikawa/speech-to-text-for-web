<template>
  <test-page />
</template>

<script lang="ts">
import { Options, Vue } from "vue-property-decorator";
import TestPage from "@/components/TestPage.vue"; // @ is an alias to /src

@Options({
  components: {
    TestPage,
  },
})
export default class AboutView extends Vue {}
</script>

<template>
  <header-main />
  <input-main />
</template>

<script lang="ts">
import { Options, Vue } from "vue-property-decorator";
import HeaderMain from "@/components/HeaderMain.vue";
import InputMain from "@/components/InputMain.vue";

@Options({
  components: {
    HeaderMain,
    InputMain,
  },
})
export default class InputView extends Vue {}
</script>

<style></style>

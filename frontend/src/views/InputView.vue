<template>
  <div>
    <input-main />
  </div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-property-decorator";
import InputHeader from "@/components/InputHeader.vue";
import InputMain from "@/components/InputMain.vue";

@Options({
  components: {
    InputMain,
  },
})
export default class InputView extends Vue {}
</script>

<style scoped>
.position {
  position: relative;
}
</style>

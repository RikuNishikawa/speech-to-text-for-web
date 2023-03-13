<template>
  <v-container>
    <div>
      <output-main />
    </div>
  </v-container>
</template>

<script lang="ts">
import { Options, Vue } from "vue-property-decorator";
import OutputMain from "@/components/OutputMain.vue"; // @ is an alias to /src
@Options({
  components: {
    OutputMain,
  },
})
export default class OutputView extends Vue {}
</script>

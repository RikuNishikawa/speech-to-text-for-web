<template>
  <v-img :width="1400" aspect-ratio="16/9" cover src="../assets/headerpage.png"
    >音声→テキスト</v-img
  >
</template>
<script lang="ts">
import { Options, Vue } from "vue-property-decorator";

@Options({})
export default class TestPage extends Vue {
  private extend = [".wav", ".mp3"];
  private voiceFile = "";
  public msg = "";
  private onClick() {
    alert(this.voiceFile);
  }
}
</script>

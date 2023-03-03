<template>
  <v-container class="input-home">
    <h1 class="input-home-maintext font-weight-bold">説明</h1>
    <div class="input-home-subtext">
      <ul>
        <li>「音声データを選択」をクリック</li>
        <li>音声データをフォルダから選択</li>
        <li>「変換」ボタンを押す</li>
      </ul>
    </div>
  </v-container>
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
<style>
.input-home {
  text-align: center;
}
.input-home-maintext {
}
.input-home-subtext li {
  display: block;
}
</style>

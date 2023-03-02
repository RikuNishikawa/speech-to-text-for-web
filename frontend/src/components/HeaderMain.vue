<template>
  <v-img :width="1400" aspect-ratio="16/9" cover src="../assets/headerpage.png"
    ><div class="header-text">
      <p class="header-maintext font-weight-black text-white">
        音&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;声&nbsp;&nbsp;&nbsp;&nbsp;→&nbsp;&nbsp;&nbsp;&nbsp;テ&nbsp;キ&nbsp;ス&nbsp;ト
      </p>
      <p class="header-subtext text-white">
        \音声データを入れて、テキストデータに変換しよう！/
      </p>
    </div></v-img
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
<style>
.header-text {
  position: relative;
  top: 40%;
}
.header-maintext {
  font-size: 44px;
  text-align: center;
}
.header-subtext {
  font-size: 20px;
  text-align: center;
  letter-spacing: 0.4em;
  padding: 32px;
}
</style>

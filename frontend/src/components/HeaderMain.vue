<template>
  <v-img width="1400" aspect-ratio="16/9" cover src="../assets/headerpage.png">
    <div class="header-text">
      <p class="header-maintext font-weight-bold text-white">
        音&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;声&nbsp;&nbsp;&nbsp;&nbsp;→&nbsp;&nbsp;&nbsp;&nbsp;テ&nbsp;キ&nbsp;ス&nbsp;ト
      </p>
      <p class="header-subtext font-weight-normal text-white">
        \音声データを入れて、テキストデータに変換しよう！/
      </p>
    </div>
  </v-img>
</template>
<script lang="ts">
import { Options, Vue } from "vue-property-decorator";

@Options({})
export default class HeaderMain extends Vue {}
</script>
<style>
.header-text {
  position: relative;
  top: 40%;
  text-shadow: 3px 3px 5px #2d2d2d;
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

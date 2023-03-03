<template>
  <v-container class="input-home">
    <div class="input-home-main-pos">
      <v-divider :thickness="2"></v-divider>
      <div class="input-home-maintext font-weight-bold">
        <span>説</span><span>明</span>
      </div>
      <v-divider :thickness="2"></v-divider>
    </div>
    <div class="input-home-subtext">
      <ul>
        <li>「音声データを選択」をクリック</li>
        <li>音声データをフォルダから選択</li>
        <li>「変換」ボタンを押す</li>
      </ul>
    </div>
    <v-img
      class="main-img"
      :width="600"
      aspect-ratio="16/9"
      cover
      src="../assets/2056912.png"
    >
    </v-img>
    <!-- active -->
    <div class="input-main-active">
      <div
        class="d-flex justify-space-around align-center flex-column flex-sm-row fill-height text-success"
      >
        <v-btn variant="falt" font-weight-bold>音声データを選択</v-btn>
      </div>
      <div
        class="d-flex justify-space-around align-center flex-column flex-sm-row fill-height text-success"
      >
        <v-btn class="font-weight-bold" variant="falt" color="success"
          >変換</v-btn
        >
      </div>
    </div>
  </v-container>
</template>
<script lang="ts">
import { Options, Vue } from "vue-property-decorator";

@Options({})
export default class InputMain extends Vue {}
</script>
<style scope>
/* h1にcssを当てるのはよくない。スコープが全体になっているから、他で干渉する可能がある。 style scopeになっているとこのファイル内でのみのスコープになる。 */
.input-home {
  text-align: center;
  color: #35495e;
  margin: 0 auto;
  width: 100%;
}
.input-home-main-pos {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 2rem;
  padding-top: 48px;
  padding-bottom: 24px;
}
/* メインテキスト */
.input-home-maintext {
  /* 48pxは大きすぎるかも */
  font-size: 32px;
  width: 220px;
  display: flex;
  justify-content: space-between;
}
/* subtext */
.input-home-subtext li {
  display: block;
  padding-bottom: 8px;
  letter-spacing: -0.1em;
}
/* img */
.main-img {
  margin: 0 auto;
}

/* active */
.input-main-active {
  display: flex;
  justify-content: space-around;
  width: 320px;
  height: 40px;
  margin: 0 auto;
  border: 2px solid grey;
  margin-top: 16px;
}
</style>

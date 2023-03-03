<template>
  <v-container class="input-home">
    <!-- 「説明」 -->
    <div class="input-home-main-pos">
      <!-- 横棒 -->
      <v-divider :thickness="2"></v-divider>
      <div class="input-home-maintext font-weight-bold">
        <span>説</span><span>明</span>
      </div>
      <!-- 横棒 -->
      <v-divider :thickness="2"></v-divider>
    </div>
    <!-- 説明文 -->
    <div class="input-home-subtext">
      <ul>
        <li>「音声データを選択」をクリック</li>
        <li>音声データをフォルダから選択</li>
        <li>「変換」ボタンを押す</li>
      </ul>
    </div>
    <!-- 画像挿入 -->
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
        class="input-main-active-light d-flex justify-space-around align-center flex-column flex-sm-row fill-height text-green"
      >
        <v-btn variant="flat" font-weight-bold>音声データを選択</v-btn>
      </div>
      <div class="d-flex justify-center align-center" style="gap: 1rem">
        <v-btn
          :loading="loading"
          :disabled="loading"
          color="green"
          @click="load"
        >
          変換
        </v-btn>
      </div>
    </div>
    <!-- subhome -->
    <v-sheet>
      <div class="input-subhome-maintext">
        このツールは、こんな<span class="color-1">悩み</span>を
        <br />お持ちの方にお勧め!
      </div>
    </v-sheet>
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
  min-width: 760px;
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
  margin-bottom: 32px;
}

/* active */
.input-main-active {
  display: flex;
  justify-content: space-around;
  width: 400px;
  height: 60px;
  margin: 0 auto;
  border: 2px solid grey;
  margin-top: px;
  margin-bottom: 128px;
}
.color-1 {
  color: #459866;
  font-size: 36px;
  font-weight: bold;
}
/* subhome */
.input-subhome-maintext {
  font-size: 28px;
  margin-bottom: 28px;
}
</style>

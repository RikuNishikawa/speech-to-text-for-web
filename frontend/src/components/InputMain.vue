<template>
  <v-container class="input-home">
    <!-- 「説明」 -->
    <div class="input-home-main-pos my-8">
      <!-- 横棒 -->
      <v-divider class="border-opacity-50" :thickness="2"></v-divider>
      <div class="input-home-maintext"><span>説</span><span>明</span></div>
      <!-- 横棒 -->
      <v-divider class="border-opacity-50" :thickness="2"></v-divider>
    </div>
    <!-- 説明文 -->
    <div class="input-home-subtext">
      <ul>
        <li class="input-home-subtext-menu pb-2">
          「音声データを選択」をクリック
        </li>
        <li class="input-home-subtext-menu pb-2">
          音声データをフォルダから選択
        </li>
        <li class="input-home-subtext-menu pb-2">「変換」ボタンを押す</li>
      </ul>
    </div>
    <!-- input-homeに画像挿入 -->
    <v-img class="main-img mb-8" :width="600" src="../assets/input-home.png">
    </v-img>
    <!-- active -->
    <div class="input-main-active mb-8">
      <div
        class="d-flex justify-space-around align-center flex-column flex-sm-row fill-height text-green"
      >
        <v-btn class="input-main-active-text" variant="flat" font-weight-bold>
          音声データを選択</v-btn
        >
      </div>
      <div class="d-flex justify-center align-center" style="gap: 1rem">
        <v-btn
          class="input-main-active-text"
          :loading="loading"
          :disabled="loading"
          color="green"
          @click="load"
        >
          変換
        </v-btn>
      </div>
    </div>
    <!-- subhome-title-->
    <v-sheet class="input-subhome pt-16">
      <div class="input-home-main-pos">
        <v-divider class="border-opacity-50" :thickness="2"></v-divider>
        <div class="input-subhome-title">
          このツールは、こんな<span class="color-1">悩み</span>を
          <br />お持ちの方にお勧め!
        </div>
        <v-divider class="border-opacity-50" :thickness="2"></v-divider>
      </div>
    </v-sheet>
  </v-container>
  <!-- input-subhome-main -->
  <v-sheet class="input-subhome mb-16">
    <v-img class="img-width align-center" src="../assets/subhomej.jpg">
      <v-container class="input-subhome-main bg-white align-center">
        <ul class="input-subhome-img py-8">
          <li class="input-subhome-grid-img pl-16">
            <v-img
              :height="150"
              :width="150"
              src="../assets/input-subhome-grid-01.png"
            ></v-img>
            <div class="input-subhome-text">
              <v-card-title class="font-weight-bold mt-4 mb-2"
                >タイトル
              </v-card-title>
              <v-card-subtitle
                >テキストテキストテキスト<br />テキストテキストテキスト<br />テキストテキストテキスト<br />
              </v-card-subtitle>
            </div>
          </li>
          <li class="input-home-grid-img">
            <v-img
              :width="300"
              :height="150"
              src="../assets/input-subhome-grid-02.png"
            ></v-img>
            <div class="input-subhome-text">
              <v-card-title class="font-weight-bold mt-4 mb-2"
                >タイトル
              </v-card-title>
              <v-card-subtitle
                >テキストテキストテキスト<br />テキストテキストテキスト<br />テキストテキストテキスト<br />
              </v-card-subtitle>
            </div>
          </li>
          <li class="input-home-grid-img pr-16">
            <v-img
              :width="150"
              :height="150"
              src="../assets/input-subhome-grid-03.png"
            ></v-img>
            <div class="input-subhome-text">
              <v-card-title class="font-weight-bold mt-4 mb-2"
                >タイトル
              </v-card-title>
              <v-card-subtitle
                >テキストテキストテキスト<br />テキストテキストテキスト<br />テキストテキストテキスト<br />
              </v-card-subtitle>
            </div>
          </li>
        </ul>
      </v-container>
    </v-img>
  </v-sheet>
</template>
<script lang="ts">
import { Options, Vue } from "vue-property-decorator";

@Options({})
export default class InputMain extends Vue {}
</script>
<style scoped>
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
}
/* メインテキスト */
.input-home-maintext {
  /* 48pxは大きすぎるかも */
  font-size: 32px;
  width: 8em;
  display: flex;
  justify-content: space-around;
}
/* subtext */
.input-home-subtext-menu {
  display: block;
  letter-spacing: -0.1em;
}
/* img */
.main-img {
  margin: 0 auto;
}
.img-width {
  width: 100vw;
  min-width: 760px;
  height: auto;
}

/* active */
.input-main-active {
  display: flex;
  justify-content: space-around;
  width: 25em;
  height: 3em;
  margin: 0 auto;
  border: 3px solid green;
}
.color-1 {
  color: #459866;
  font-size: 36px;
  font-weight: bold;
}
.input-main-active-text {
  font-size: 16px;
  font-weight: 900;
}
/* subhome */
.input-subhome {
  min-width: 760px;
}
.input-subhome-title {
  font-size: 28px;
  width: 80em;
  color: #35495e;
}
.input-subhome-main {
  border-radius: 15px;
}
li {
  display: block;
}
.input-subhome-img {
  display: flex;
  justify-content: space-between;
}
.input-subhome-text {
  text-align: center;
  color: #35495e;
}
</style>

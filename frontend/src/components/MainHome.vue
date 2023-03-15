<template>
  <v-container>
    <v-sheet class="main-home pt-8">
      <div class="input-home-main-pos mb-8">
        <v-divider class="border-opacity-50" :thickness="2"></v-divider>
        <div
          class="d-flex justify-space-around main-home-title text-grey-darken-4"
        >
          <span>H</span>
          <span>O</span>
          <span>M</span>
          <span>E</span>
        </div>
        <v-divider class="border-opacity-50" :thickness="2"></v-divider>
      </div>
      <v-img class="img-width align-center mb-8" src="../assets/subhomej.jpg">
        <div class="main-home-main bg-white">
          <ul class="main-home-img py-6">
            <li>
              <v-img
                :height="150"
                :width="200"
                src="../assets/input-subhome-grid-01.png"
              ></v-img>
              <div class="main-home-text">
                <v-card-title class="font-weight-bold mt-4 mb-2"
                  >タイトル
                </v-card-title>
                <v-card-subtitle
                  >テキストテキストテキスト<br />テキストテキストテキスト<br />テキストテキストテキスト<br />
                </v-card-subtitle>
              </div>
            </li>
            <li>
              <v-img
                :width="300"
                :height="150"
                src="../assets/input-subhome-grid-02.png"
              ></v-img>
              <div class="main-home-text">
                <v-card-title class="font-weight-bold mt-4 mb-2"
                  >タイトル
                </v-card-title>
                <v-card-subtitle
                  >テキストテキストテキスト<br />テキストテキストテキスト<br />テキストテキストテキスト<br />
                </v-card-subtitle>
              </div>
            </li>
            <li>
              <v-img
                :width="200"
                :height="150"
                src="../assets/input-subhome-grid-03.png"
              ></v-img>
              <div class="main-home-text">
                <v-card-title class="font-weight-bold mt-4 mb-2"
                  >タイトル
                </v-card-title>
                <v-card-subtitle
                  >テキストテキストテキスト<br />テキストテキストテキスト<br />テキストテキストテキスト<br />
                </v-card-subtitle>
              </div>
            </li>
          </ul>
        </div>
      </v-img>
    </v-sheet>
  </v-container>
</template>

<script lang="ts">
import { Options, Vue } from "vue-property-decorator";

@Options({})
export default class MainHome extends Vue {}
</script>
<style>
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
  /* min-width: 760px; */
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
.input-home-subtext {
  /* min-width: 760px; */
}
.input-home-subtext-menu {
  display: block;
  letter-spacing: -0.1em;
}
/* img */
.main-img {
  margin: 0 auto;
  /* min-width: 760px; */
}
.img-width {
  width: 100vw;
  /* min-width: 760px; */
  height: auto;
}
/* main-home */
.main-home-title {
  font-size: 56px;
  width: 15em;
  color: #35495e;
  text-align: center;
}
.main-home-main {
  border-radius: 15px;
  /* min-width: 760px; */
  width: 750px;
  margin: 0 auto;
}
li {
  display: block;
}
.main-home-img {
  display: flex;
  justify-content: space-between;
}
.main-home-text {
  text-align: center;
  color: #35495e;
}
</style>

<template>
  <v-container>
    <v-sheet class="main-home mt-16">
      <div class="input-home-main-pos mb-8">
        <v-divider class="border-opacity-50" :thickness="2"></v-divider>
        <div
          class="d-flex justify-space-around main-home-title text-green font-weight-bold"
        >
          こんな悩みをお持ちの方におすすめ！
        </div>
        <v-divider class="border-opacity-50" :thickness="2"></v-divider>
      </div>
      <v-img class="img-width align-center mb-8" src="../assets/subhomej.jpg">
        <div class="main-home-main bg-white pa-6">
          <ul class="main-home-img">
            <li>
              <v-img
                :height="150"
                :width="200"
                src="../assets/input-subhome-grid-01.png"
              ></v-img>
              <div class="main-home-text">
                <v-card-title class="font-weight-bold mt-4">
                  議事録のための残業
                </v-card-title>
                <v-card-subtitle>
                  会議の文字起こし作業の<br />
                  ために残業していませんか?<br />
                  残業時間はこれで0です!
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
                <v-card-title class="font-weight-bold mt-4">
                  セミナーの文字起こし
                </v-card-title>
                <v-card-subtitle>
                  セミナー等で聞き逃しや<br />
                  だる～い文字起こしを<br />
                  VCTで解決しましょう!<br />
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
                <v-card-title class="font-weight-bold mt-4">
                  え！こんな言語も！
                </v-card-title>
                <v-card-subtitle>
                  日本語や英語<br />ペルシャ語やアラビア語<br />音MADも!?<br />
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
.main-home {
  text-align: center;
  color: #35495e;
  margin: 0 auto;
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
  font-size: 32px;
  width: 8em;
  display: flex;
  justify-content: space-around;
}
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
  height: auto;
}
/* main-home */
.main-home-title {
  font-size: 24px;
  width: 80em;
  color: #35495e;
  text-align: center;
}
.main-home-main {
  border-radius: 15px;
  width: 750px;
  margin: 0 auto;
  opacity: 0.85;
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

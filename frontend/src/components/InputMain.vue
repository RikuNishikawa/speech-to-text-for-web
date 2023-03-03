<template>
  <v-container class="input-home">
    <div class="input-home-main-pos">
      <v-divider :thickness="3"></v-divider>
      <div class="input-home-maintext font-weight-bold">
        <span>説</span><span>明</span>
      </div>
      <v-divider :thickness="3"></v-divider>
    </div>
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
.input-home-maintext {
  /* 48pxは大きすぎるかも */
  font-size: 48px;
  width: 145px;
  display: flex;
  justify-content: space-around;
}
.input-home-subtext li {
  display: block;
  padding-bottom: 10px;
}
</style>

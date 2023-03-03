<template>
  <v-container class="input-home">
    <h1 class="input-home-maintext font-weight-bold">
      説&nbsp;&nbsp;&nbsp;&nbsp;明
    </h1>
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
<style>
/* h1にcssを当てるのはよくない。スコープが全体になっているから、他で干渉する可能がある。 */
h1 {
  display: flex;
  align-items: center;
}
h1::after,
h1::before {
  content: "";
  flex-grow: 1;
  height: 1px;
  background: #000;
}
h1::after {
  margin-left: 40px;
}
h1::before {
  margin-right: 40px;
}
.input-home {
  text-align: center;
  color: #35495e;
  margin: 0 auto;
  width: 100%;
}
.input-home-maintext {
  padding-top: 60px;
  padding-bottom: 32px;
}
.input-home-subtext li {
  display: block;
  padding-bottom: 10px;
}
</style>

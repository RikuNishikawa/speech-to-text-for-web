<template>
  <v-sheet class="output-main">
    <!-- title -->
    <div class="output-main-title mt-8 mb-4 text-green font-weight-bold">
      \テキスト変換終了!/
    </div>
    <div class="output-main-text">
      変換されたデータをダウンロードボタンよりダウンロードしてください
    </div>
    <!-- output-img -->
    <v-img
      class="output-main-img"
      :width="350"
      :height="250"
      src="../assets/output.png"
    ></v-img>
    <!-- active -->
    <div class="output-main-active my-8">
      <div class="output-main-active-text d-flex justify-space-between">
        <div class="output-active-file">ファイル名.txt</div>
        <!-- ボタンの形を四角にしたい -->
        <v-btn
          tile
          color="green"
          class="output-active-download"
          @click="onClick"
        >
          ダウンロード
        </v-btn>
      </div>
    </div>
  </v-sheet>
  <!-- <div>test: {{ $router.params.data }}</div> -->
</template>
<script lang="ts">
import { Options, Vue } from "vue-property-decorator";

@Options({})
export default class OutputMain extends Vue {
  private onClick() {
    console.log(this.$route, this.$router);
  }
}
</script>
<style scoped>
.output-main {
  text-align: center;
}
.output-main-title {
  font-size: 24px;
  letter-spacing: 0.3em;
}
.output-main-text {
  font-size: 16px;
}
.output-main-img {
  margin: 0 auto;
}
.output-main-active-text {
  width: 40vw;
  border: 1px solid black;
  margin: 0 auto;
}
.output-active-file {
  text-align: center;
}
.output-active-download {
  border-left: 1px solid black;
}
</style>

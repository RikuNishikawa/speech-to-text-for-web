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
        <v-card :text="text" />
        <!-- <div class="output-active-file">ファイル名.txt</div> -->
        <!-- ボタンの形を四角にしたい -->
        <!-- <v-btn
          tile
          color="green"
          class="output-active-download"
          @click="onClick"
        >
          ダウンロード
        </v-btn> -->
      </div>
    </div>
  </v-sheet>
</template>
<script lang="ts">
import { Options, Vue } from "vue-property-decorator";

@Options({})
export default class OutputMain extends Vue {
  private text: string | string[] = "";
  mounted() {
    this.text = this.$route.params.text;
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
  width: 100%;
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

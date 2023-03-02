<template>
  <v-container>
    <v-app-bar flat class="px-16">
      <v-toolbar-title class="header-title">VCT</v-toolbar-title>
      <div class="">
        <v-btn variant="text" class="header-btn"> Home </v-btn>
        <v-btn variant="text" class="header-btn"> 音声テキスト変換 </v-btn>
        <v-btn variant="text" class="header-btn"> 開発メンバー </v-btn>
      </div>
    </v-app-bar>
  </v-container>
</template>

<script lang="ts">
import { Options, Vue } from "vue-property-decorator";

@Options({})
export default class HeaderItem extends Vue {}
</script>
<style>
.header-title {
  font-size: 24px;
}
</style>

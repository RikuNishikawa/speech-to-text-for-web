<template>
  <v-app-bar flat class="header px-16">
    <v-toolbar-title class="header-title font-weight-bold" @click="moveHome">
      VCT
    </v-toolbar-title>
    <v-spacer />
    <v-toolbar-items style="height: 32px">
      <v-btn rounded="lg" class="header-btn font-weight-bold" @click="moveHome">
        Home
      </v-btn>
      <v-btn
        rounded="lg"
        class="header-btn font-weight-bold"
        @click="moveInput"
      >
        音声テキスト変換
      </v-btn>
      <v-btn
        rounded="lg"
        class="header-btn font-weight-bold"
        @click="moveMember"
      >
        開発メンバー
      </v-btn>
    </v-toolbar-items>
  </v-app-bar>
</template>

<script lang="ts">
import { Options, Vue } from "vue-property-decorator";

@Options({})
export default class HeaderMain extends Vue {
  private moveHome() {
    this.$router.push({ path: "/" });
  }
  private moveInput() {
    this.$router.push({ path: "/input" });
  }
  private moveMember() {
    this.$router.push({ path: "/member" });
  }
}
</script>
<!-- css部分 -->
<style>
.header {
  border-bottom: 1px solid #d7d7d7;
}
.header-title {
  font-size: 24px;
}
.px-16 {
  opacity: 0.8;
}
</style>

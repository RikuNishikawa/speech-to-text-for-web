<template>
  <v-container>
    <v-app-bar flat class="px-16">
      <v-toolbar-title class="header-title">VCT</v-toolbar-title>
      <v-spacer />
      <v-toolbar-items>
        <v-btn variant="text" class="header-btn" @click="moveHome">
          Home
        </v-btn>
        <v-btn variant="text" class="header-btn" @click="moveInput">
          音声テキスト変換
        </v-btn>
        <v-btn variant="text" class="header-btn" @click="moveMember">
          開発メンバー
        </v-btn>
      </v-toolbar-items>
    </v-app-bar>
  </v-container>
</template>

<script lang="ts">
import { Options, Vue } from "vue-property-decorator";

@Options({})
export default class HeaderItem extends Vue {
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
<style>
.header-title {
  font-size: 24px;
}
</style>

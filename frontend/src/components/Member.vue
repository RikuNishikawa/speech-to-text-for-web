<template>
  <v-container>
    <div class="member-pos my-8">
      <v-divider class="border-opacity-50" :thickness="2"></v-divider>
      <div class="member-title">開発メンバー紹介</div>
      <v-divider class="border-opacity-50" :thickness="2"></v-divider>
    </div>
  </v-container>
  <v-img class="member-img mb-8" src="../assets/member.png"></v-img>
</template>
<script lang="ts">
import { Options, Vue } from "vue-property-decorator";

@Options({})
export default class Member extends Vue {}
</script>
<style>
.member-pos {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 2rem;
}
.member-title {
  font-size: 32px;
  width: 30em;
  text-align: center;
}
.member-img {
  width: 100vw;
  min-width: 760px;
  height: auto;
}
</style>

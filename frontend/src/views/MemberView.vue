<template>
  <v-container>
    <div class="member-title-pos my-8">
      <v-divider class="border-opacity-50" :thickness="2"></v-divider>
      <div class="member-title">開発メンバー紹介</div>
      <v-divider class="border-opacity-50" :thickness="2"></v-divider>
    </div>
    <!-- img -->
    <v-img class="member-img mb-8" src="../assets/member.png"></v-img>

    <member class="mb-5" :memberInfo="ishizu" position="left" />
    <!-- <v-img src="../assets/riku-profile.png"></v-img> -->
    <member class="mb-5" :memberInfo="nishikawa" position="right" />
    <member class="mb-5" :memberInfo="shibata" position="left" />
  </v-container>
</template>

<script lang="ts">
import { Options, Vue } from "vue-property-decorator";
// eslint-disable-next-line
import Member from "@/components/Member.vue";

@Options({
  components: {
    Member,
  },
})
export default class MemberView extends Vue {
  public ishizu = {
    name: "石津 龍真",
    responsible: "PM",
    data: {
      GitHub: "https://github.com/ryoum-0930",
      Twitter: "@Rym_gdm",
      Facebook: "",
    },
    image: "",
  };
  public nishikawa = {
    name: "西川 陸",
    responsible: "デザイン/フロントエンド",
    data: {
      GitHub: "https://github.com/RikuNishikawa",
      Twitter: "@NRiku0917",
      Facebook: "",
    },
    image: require("../assets/riku-profile.png"),
  };
  public shibata = {
    name: "柴田 康希",
    responsible: "バックエンド",
    data: { GitHub: "", Twitter: "", Facebook: "" },
    image: "",
  };
}
</script>

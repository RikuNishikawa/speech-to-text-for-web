<template>
  <!-- <div>{{ memberInfo.name }}</div> -->
  <!-- member紹介 -->
  <!-- こんな感じでデータを取り出して一人分のパネルだけ作って、dataの中身はiconで隠して、iconクリック時のページ遷移にして欲しい -->
  <!-- cardのホバーいる？アイコンとかにフォーカスしたときにクリック可能がどうかだけ分かる機能の方が欲しくない？ -->

  <v-sheet>
    <v-hover open-delay="200">
      <v-card
        :class="position"
        class="mx-0 member-01"
        height="240"
        max-width="350"
        v-bind="props"
      >
        <v-card-text class="font-weight-normal ma-3">
          <div class="member-name pb-10">{{ memberInfo.name }}</div>
          <div class="member-part pb-10">
            <div>担当: {{ memberInfo.responsible }}</div>
            <v-icon icon="mdi-github"></v-icon>
            <v-icon icon="mdi-twitter"></v-icon>
            <v-icon icon="mdi-facebook"></v-icon>
            <span class="color-01"></span>
          </div>
          <div class="member-sns"></div>
        </v-card-text>
      </v-card>
    </v-hover>
  </v-sheet>
</template>
<script lang="ts">
import { Options, Prop, Vue } from "vue-property-decorator";

export interface URL {
  Facebook: string;
  Twitter: string;
  GitHub: string;
}

export interface MemberInfo {
  name: string;
  responsible: string;
  data: URL;
  image: string;
}

@Options({})
export default class Member extends Vue {
  @Prop({ default: "" }) private memberInfo!: MemberInfo;
  @Prop({ default: "right" }) private position!: string;
}
</script>
<style scope>
.color-01 {
  color: #459866;
}
.left {
  display: flex;
  justify-content: flex-end;
}
.rigth {
  display: flex;
  justify-content: flex-start;
}
.member-title-pos {
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
.member-name {
  font-size: 28px;
}
.member-text {
  gap: auto;
}
.member-02 {
  margin: 0 0 0 auto;
}
</style>

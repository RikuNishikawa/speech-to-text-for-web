<template>
  <v-container>
    <div class="member-title-pos my-8">
      <v-divider class="border-opacity-50" :thickness="2"></v-divider>
      <div class="member-title">開発メンバー紹介</div>
      <v-divider class="border-opacity-50" :thickness="2"></v-divider>
    </div>
  </v-container>
  <!-- img -->
  <v-img class="member-img mb-8" src="../assets/member.png"></v-img>
  <!-- member紹介 -->
  <v-container>
    <v-sheet>
      <v-hover v-slot="{ isHovering, props }" open-delay="200">
        <v-card
          :elevation="isHovering ? 16 : 2"
          :class="{ 'on-hover': isHovering }"
          class="mx-0 member-01"
          height="240"
          max-width="350"
          v-bind="props"
        >
          <v-card-text class="font-weight-normal ma-3">
            <div class="member-name pb-10">石津龍真</div>
            <div class="member-part pb-10">
              <span>担当:</span><span class="color-01">全般サポート</span
              ><br /><span>Email:</span><span class="color-01"></span>
            </div>
            <div class="member-sns"></div>
          </v-card-text>
        </v-card>
      </v-hover>
      <v-hover v-slot="{ isHovering, props }" open-delay="200">
        <v-card
          :elevation="isHovering ? 16 : 2"
          :class="{ 'on-hover': isHovering }"
          class="member-02"
          height="240"
          max-width="350"
          v-bind="props"
        >
          <v-card-text class="font-weight-normal ma-3">
            <div class="member-name pb-10">柴田康希</div>
            <div class="member-part pb-10">
              <span>担当:</span><span class="color-01">バックエンド</span
              ><br /><span>Email:</span><span class="color-01"></span>
            </div>
            <div class="member-sns"></div>
          </v-card-text>
        </v-card>
      </v-hover>
      <v-hover v-slot="{ isHovering, props }" open-delay="200">
        <v-card
          :elevation="isHovering ? 16 : 2"
          :class="{ 'on-hover': isHovering }"
          class="mx-0 member-03"
          height="240"
          max-width="350"
          v-bind="props"
        >
          <v-card-text class="font-weight-normal ma-3">
            <div class="member-name pb-10">西川陸</div>
            <div class="member-part pb-10">
              <span>担当:</span
              ><span class="color-01">デザイン/フロントエンド</span><br /><span
                >Email:</span
              ><span class="color-01"></span>
            </div>
            <div class="member-sns"></div>
          </v-card-text>
        </v-card>
      </v-hover>
    </v-sheet>
  </v-container>
</template>
<script lang="ts">
import { Options, Vue } from "vue-property-decorator";

@Options({})
export default class Member extends Vue {}
</script>
<style scope>
.color-01 {
  color: #459866;
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

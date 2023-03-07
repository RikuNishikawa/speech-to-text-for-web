<template>
  <!-- 真ん中の要素の右配置の仕方がわからない -->
  <!-- 画像の挿入方法がわからない -->
  <v-sheet>
    <v-hover open-delay="200">
      <v-card
        :class="position"
        class="mx-0 member-01"
        height="500"
        max-width="350"
        v-bind="props"
      >
        <v-card-text class="font-weight-normal ma-3">
          <v-img
            class="align-center mb-8"
            :width="300"
            :height="200"
            :src="memberInfo.image"
          ></v-img>
          <v-divider class="border-opacity-50 mb-6" :thickness="1"></v-divider>
          <div class="member-name pb-3">{{ memberInfo.name }}</div>
          <v-divider class="border-opacity-50 mb-3" :thickness="1"></v-divider>
          <div>
            <div class="member-part mb-10">
              担当:<span class="member-part-color pl-4">
                {{ memberInfo.responsible }}
              </span>
            </div>
            <div class="d-flex align-center flex-column flex-sm-row">
              <v-hover v-slot:default="{ isHovering, props }">
                <v-btn
                  class="mr-2"
                  v-bind="props"
                  :color="isHovering ? 'primary' : undefined"
                  variant="outlined"
                  size="x-small"
                  icon="mdi-github"
                  v-bind:href="memberInfo.data.GitHub"
                ></v-btn>
              </v-hover>
              <v-hover v-slot:default="{ isHovering, props }">
                <v-btn
                  class="mr-2"
                  v-bind="props"
                  :color="isHovering ? 'blue' : undefined"
                  variant="outlined"
                  size="x-small"
                  icon="mdi-twitter"
                  v-bind:href="memberInfo.data.Twitter"
                ></v-btn>
              </v-hover>
              <v-hover v-slot:default="{ isHovering, props }">
                <v-btn
                  class="mr-2"
                  v-bind="props"
                  :color="isHovering ? 'blue' : undefined"
                  variant="outlined"
                  size="x-small"
                  icon="mdi-facebook"
                  v-bind:href="memberInfo.data.Facebook"
                ></v-btn>
              </v-hover>
            </div>
          </div>
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
.left {
  display: flex;
  justify-content: flex-end;
}
.right {
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
/* .member-image {
  width: 300px;
  height: 200px;
} */
.member-name {
  font-size: 24px;
}
.member-part {
  font-size: 16px;
}
.member-part-color {
  color: #459866;
}
.member-02 {
  margin: 0 0 0 auto;
}
</style>
// eslint-disable-next-line

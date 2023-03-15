<template>
  <v-sheet class="member">
    <v-hover open-delay="200">
      <v-card class="member-card" height="500" max-width="350">
        <v-card-text class="font-weight-normal ma-3">
          <v-img
            class="member-image align-center mb-8"
            width="300"
            height="200"
            :src="memberInfo.image"
          ></v-img>
          <v-divider class="border-opacity-50 mb-6" :thickness="1"></v-divider>
          <div class="member-name text-color mb-6 font-weight-bold">
            {{ memberInfo.name }}
          </div>
          <v-divider class="border-opacity-50 mb-8" :thickness="1"></v-divider>
          <div>
            <div class="member-part mb-10">
              担当:<span class="member-part-color pl-2">
                {{ memberInfo.responsible }}
              </span>
            </div>
            <div class="member-btn d-flex align-center flex-column flex-sm-row">
              <v-hover v-slot:default="{ isHovering, props }">
                <v-btn
                  class="mr-2"
                  v-bind="props"
                  :color="isHovering ? 'primary' : undefined"
                  variant="outlined"
                  size="small"
                  icon="mdi-github"
                  opacity="0.5"
                  v-bind:href="memberInfo.data.GitHub"
                ></v-btn>
              </v-hover>
              <v-hover v-slot:default="{ isHovering, props }">
                <v-btn
                  class="mr-2"
                  v-bind="props"
                  :color="isHovering ? 'blue' : undefined"
                  variant="outlined"
                  size="small"
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
                  size="small"
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
/* .left {
  display: flex;
  justify-content: flex-end;
}
.right {
  display: flex;
  justify-content: flex-start;
} */
.member {
  max-width: 350px;
}
.member-title-pos {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 2rem;
  min-width: 760px;
}
.member-title {
  font-size: 56px;
  width: 40em;
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
  font-size: 28px;
}
.member-part {
  font-size: 20px;
}
.member-part-color {
  color: #459866;
}
.member-02 {
  margin: 0 0 0 auto;
}
.member-btn {
  max-width: 200px;
  justify-content: space-between;
  margin: 0 auto;
}
.text-color {
  color: #35495e;
}
</style>
// eslint-disable-next-line

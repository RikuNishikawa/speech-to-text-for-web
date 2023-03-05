<template>
  <v-sheet class="position">
    <v-img class="img-width" src="../assets/headerpage-ver2.png">
      <div class="header-text">
        <v-card-title
          class="px-16 header-maintext font-weight-bold text-grey-darken-4"
        >
          <div class="space width">
            <span>音</span>
            <span>声</span>
          </div>
          <div>→</div>
          <div class="space width pl-6">
            <span>テ</span>
            <span>キ</span>
            <span>ス</span>
            <span>ト</span>
          </div>
        </v-card-title>
        <v-card-subtitle
          class="header-subtext font-weight-bold text-grey-darken-4"
        >
          \ 音声データをテキストデータに変換しよう！ /
        </v-card-subtitle>
      </div>
    </v-img>
  </v-sheet>
</template>
<script lang="ts">
import { Options, Vue } from "vue-property-decorator";

@Options({})
export default class InputHeader extends Vue {}
</script>
<style scope>
.position {
  position: absolute;
  margin-top: -108px;
}
.img-width {
  width: 100vw;
  min-width: 760px;
  height: auto;
}
.space {
  width: 250px;
}
.header-text {
  position: relative;
  top: 40%;
  /* text-shadow: 3px 3px 5px #2d2d2d; */
}
.header-maintext {
  font-size: 56px;
  display: flex;
  justify-content: center;
  gap: 1rem;
}
.header-maintext .width {
  display: flex;
  justify-content: space-around;
}
.header-subtext {
  font-size: 24px;
  text-align: center;
  letter-spacing: 0.4em;
  padding-top: 32px;
}
</style>

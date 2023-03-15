<template>
  <v-container>
    <v-sheet class="input-home">
      <!-- 「説明」 -->
      <div class="input-home-main-pos my-8">
        <!-- 横棒 -->
        <v-divider class="border-opacity-50" :thickness="2"></v-divider>
        <div class="input-home-maintext"><span>説</span><span>明</span></div>
        <!-- 横棒 -->
        <v-divider class="border-opacity-50" :thickness="2"></v-divider>
      </div>
      <!-- 説明文 -->
      <div class="input-home-subtext">
        <ul>
          <li class="input-home-subtext-menu pb-2">
            「音声データを選択」をクリック
          </li>
          <li class="input-home-subtext-menu pb-2">
            音声データをフォルダから選択
          </li>
          <li class="input-home-subtext-menu pb-2">「変換」ボタンを押す</li>
        </ul>
      </div>
      <!-- input-homeに画像挿入 -->
      <v-img class="main-img mb-8" :width="600" src="../assets/input-home.png">
      </v-img>
      <!-- active -->
      <div class="input-main-active mb-8">
        <div
          class="d-flex justify-space-around align-center flex-column flex-sm-row fill-height text-green"
        >
          <v-file-input
            :accept="extend"
            label="File input"
            @change="onFileChange"
            name="file"
          />
        </div>
        <div class="d-flex justify-center align-center" style="gap: 1rem">
          <v-btn
            class="input-main-active-text"
            :loading="loading"
            :disabled="loading"
            rounded="0"
            color="green"
            @click="onClick"
          >
            {{ stateName }}
          </v-btn>
        </div>
      </div>
      <!-- subhome-title-->
    </v-sheet>
  </v-container>
</template>
<script lang="ts">
import { Options, Vue } from "vue-property-decorator";
import axios from "axios";

@Options({})
export default class InputMain extends Vue {
  private stateName = "選択";
  private extend = [".wav", ".mp3", "m4a"];
  private voiceFile: File | null = null;
  public msg = "";

  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  private onFileChange(e: any) {
    this.voiceFile = e.target.files[0];
    if (this.voiceFile) {
      this.stateName = "変換";
    } else {
      this.stateName = "選択";
    }
  }
  private onClick() {
    if (this.voiceFile) {
      const formData = new FormData();
      formData.append("file", this.voiceFile);
      axios
        .post("http://127.0.0.1:8000/upload/", formData, {
          headers: { "Content-Type": "multipart/form-data" },
        })
        .then((response) => {
          console.log(response.data.text); //レスポンスデータがこれ
          console.log(response.status); //成功したら200
          //ページ遷移
          this.$router.push({
            name: "output",
            params: {
              text: response.data.text,
              state: response.status,
              path: "/output/",
            },
          });
        })
        .catch((error) => {
          console.log(error.response);
        });
    } else {
      alert(
        "ファイルが選択されていません。ファイルを設定してから変換ボタンを押して下さい。"
      );
    }
  }
}
</script>
<style scoped>
.input-home {
  text-align: center;
  color: #35495e;
  margin: 0 auto;
  width: 100%;
  min-width: 760px;
}
.input-home-main-pos {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 2rem;
  /* min-width: 760px; */
}
/* メインテキスト */
.input-home-maintext {
  font-size: 32px;
  width: 8em;
  display: flex;
  justify-content: space-around;
}
/* subtext */
.input-home-subtext {
  /* min-width: 760px; */
}
.input-home-subtext-menu {
  display: block;
  letter-spacing: -0.1em;
}
/* img */
.main-img {
  margin: 0 auto;
  /* min-width: 760px; */
}
.img-width {
  width: 100vw;
  /* min-width: 760px; */
  height: auto;
}

/* active */
.input-main-active {
  display: flex;
  justify-content: space-around;
  width: 25em;
  height: 3em;
  margin: 0 auto;
  border: 3px solid green;
  /* min-width: 760px; */
}
.color-1 {
  color: #459866;
  font-size: 36px;
  font-weight: bold;
}
.input-main-active-text {
  font-size: 16px;
  font-weight: 900;
}
/* subhome */
.input-subhome {
  /* min-width: 760px; */
}
.input-subhome-title {
  font-size: 28px;
  width: 80em;
  color: #35495e;
}
.input-subhome-main {
  border-radius: 15px;
  /* min-width: 760px; */
  width: 750px;
  margin: 0 auto;
}
li {
  display: block;
}
.input-subhome-img {
  display: flex;
  justify-content: space-between;
}
.input-subhome-text {
  text-align: center;
  color: #35495e;
}
</style>

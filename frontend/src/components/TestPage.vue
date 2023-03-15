<template>
  <v-container>
    <v-icon size="large" color="green-darken-2"> mdi-domain </v-icon>
    <v-file-input
      :accept="extend"
      label="File input"
      @change="onFileChange"
      name="file"
    ></v-file-input>
    <v-btn class="ma-2" color="primary" @click="onClick"> Submit</v-btn>
  </v-container>
</template>

<script lang="ts">
import { Options, Vue } from "vue-property-decorator";
import axios from "axios";

@Options({})
export default class TestPage extends Vue {
  private extend = [".wav", ".mp3"];
  private voiceFile: File | null = null;
  public msg = "";

  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  private onFileChange(e: any) {
    this.voiceFile = e.target.files[0];
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
          console.log("data was sent");
          console.log(response.data);
          console.log(response.status);
        })
        .catch((error) => {
          console.log("error");
          console.log(error.response);
        });
    }
  }
}
</script>

<template>
  <v-container>
    <v-icon size="large" color="green-darken-2"> mdi-domain </v-icon>
    <v-file-input
      :accept="extend"
      label="File input"
      v-model="voiceFile"
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
  private voiceFile = "";
  public msg = "";
  private onClick() {
    console.log(this.voiceFile);

    axios
      .post("/saveuploadfile/", this.voiceFile)

      .then(function (response) {
        console.log("data was sent");
      })

      .catch((error) => {
        console.log("error");
      });
  }
}
</script>

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
    //console.log("result");
    console.log(this.voiceFile);

    if (this.voiceFile == "") {
      axios
        .post("http://127.0.0.1:8000/uploadtest/", "nothing")
        .then((response) => {
          console.log("data was sent");
          console.log(response.data);
          console.log(response.status);
        })

        .catch((error) => {
          console.log("error");
          console.log(error.response);
          //console.log(error.response.status);
        });
    } else {
      axios
        .post("http://127.0.0.1:8000/saveuploadfile/", this.voiceFile)
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

    //=======test用=========
    /*
    axios
      .post("http://127.0.0.1:8000/uploadtest/", "test")
      .then((response) => {
        console.log("data was sent");
        console.log(response.data);
        console.log(response.status);
      })

      .catch((error) => {
        console.log("error");
        console.log(error.response);
        //console.log(error.response.status);
      });
    */
    /*
    axios
      .post("http://127.0.0.1:8000/saveuploadfile/", this.voiceFile)
      .then((response) => {
        console.log("data was sent");
        console.log(response.data);
        console.log(response.status);
      })

      .catch((error) => {
        console.log("error");
        console.log(error.response);
      });
    */
  }
}
</script>

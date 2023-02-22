<template>
  <v-container>
    <v-icon size="large" color="green-darken-2"> mdi-domain </v-icon>
    <v-file-input :accept="extend" label="File input"></v-file-input>
    <v-btn class="ma-2" color="primary"> Submit</v-btn>
  </v-container>
</template>

<script lang="ts">
import { Options, Vue } from "vue-property-decorator";

@Options({})
export default class TestPage extends Vue {
  msg!: string;
  private extend = [".wav", ".mp3"];
}
</script>

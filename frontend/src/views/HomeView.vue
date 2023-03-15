<template>
  <input-header />
  <main-home />
</template>

<script lang="ts">
import { Options, Vue } from "vue-property-decorator";
import HelloWorld from "@/components/HelloWorld.vue";
import MainHome from "@/components/MainHome.vue";
import InputHeader from "@/components/InputHeader.vue";

@Options({
  components: {
    HelloWorld,
    MainHome,
    InputHeader,
  },
})
export default class HomeView extends Vue {}
</script>

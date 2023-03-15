<template>
  <main-home />
</template>

<script lang="ts">
import { Options, Vue } from "vue-property-decorator";
import HelloWorld from "@/components/HelloWorld.vue";
import MainHome from "@/components/MainHome.vue";

@Options({
  components: {
    HelloWorld,
    MainHome,
  },
})
export default class HomeView extends Vue {}
</script>

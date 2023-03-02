<template>
  <hello-world />
</template>

<script lang="ts">
import { Options, Vue } from "vue-property-decorator";
import HelloWorld from "@/components/HelloWorld.vue";

@Options({
  components: {
    HelloWorld,
  },
})
export default class HomeView extends Vue {}
</script>

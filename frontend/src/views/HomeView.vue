<template>
  <div class="p-header">
    <div class="container">
      <p class="p-header_title">VCT</p>
      <div class="p-header_nav">
        <ul class="p-header_nav_list">
          <li><a href="">menu</a></li>
          <li><a href="">menu</a></li>
          <li><a href="">menu</a></li>
          <li><a href="">menu</a></li>
        </ul>
      </div>
    </div>
  </div>
  <hello-world />
</template>

<script lang="ts">
import { defineComponent } from "vue";

// Components
import HelloWorld from "../components/HelloWorld.vue";

export default defineComponent({
  name: "HomeView",

  components: {
    HelloWorld,
  },
});
</script>

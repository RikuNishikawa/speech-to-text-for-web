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

  <test-page />
</template>

<script lang="ts">
import { Options, Vue } from "vue-property-decorator";
import TestPage from "@/components/TestPage.vue"; // @ is an alias to /src

@Options({
  components: {
    TestPage,
  },
})
export default class AboutView extends Vue {}
</script>

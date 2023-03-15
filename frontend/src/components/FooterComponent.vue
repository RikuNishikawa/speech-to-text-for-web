<template>
  <div class="footer py-16 text-white"></div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-property-decorator";

@Options({})
export default class FooterComponent extends Vue {}
</script>
<style scope>
.footer {
  background-color: #666;
}
</style>

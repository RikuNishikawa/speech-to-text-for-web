<template>
  <div class="footer">
    <div>footer領域</div>
  </div>
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

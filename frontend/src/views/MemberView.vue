<template>
  <div class="font">
    <input-header class="position" />
    <member />
  </div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-property-decorator";
import InputHeader from "@/components/InputHeader.vue";
import Member from "@/components/Member.vue"; // @ is an alias to /src

@Options({
  components: {
    Member,
  },
})
export default class MemberView extends Vue {}
</script>

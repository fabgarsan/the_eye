<template>
  <div style="padding: 10px; border: solid 1px black; margin-bottom: 2px">
    <p>This Button will be {{ name }} sent by {{ host }}</p>
    <button @click="onclick">Click</button>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ButtonEvent",
  props: {
    name: String,
    host: String,
    sessionId: String,
    timestamp: String,
  },
  methods: {
    onclick: async function () {
      await axios.post(`${process.env.VUE_APP_API}/events/`, {
        session_id: this.sessionId,
        category: "page interaction",
        name: `Click ${this.name}`,
        data: {
          host: this.host,
          path: "/",
          element: "custom button"
        },
        timestamp: this.timestamp
      });
    }
  }
}
</script>

<style scoped>

</style>
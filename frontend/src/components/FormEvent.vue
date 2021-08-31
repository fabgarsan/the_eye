<template>
  <div style="padding: 10px; border: solid 1px black; margin-bottom: 2px">
    <p>This Form {{ name }} will be sent by {{ host }}</p>
    <form v-on:submit.prevent="sendForm">
      <p>
        First Name:<input type="text" v-model="firstName">
      </p>
      <p>
        Last Name:<input type="text" v-model="lastName">
      </p>
      <p><input type="submit" value="Send"></p>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "FormEvent",
  props: {
    name: String,
    host: String,
    sessionId: String,
    timestamp: String,
  },
  data() {
    return {
      firstName: '',
      lastName: ''
    }
  },
  methods: {
    sendForm: async function () {
      await axios.post(`${process.env.VUE_APP_API}/events/`, {
        session_id: this.sessionId,
        category: "form interaction",
        name: `Submit ${this.name}`,
        data: {
          host: this.host,
          path: "/",
          "form": {
            "first_name": this.firstName,
            "last_name": this.lastName
          }
        },
        timestamp: this.timestamp
      });

      this.firstName = '';
      this.lastName = '';
    },
  },
}
</script>

<style scoped>

</style>
<template>
  <div class="container-fluid" id="app">
    <div class="row">
      <div class="col-12">
        <h1>Testing Dashboard</h1>
      </div>
      <div class="col-12 col-md-4 mb-3">
        <div class="p-3" style="color: red; border: solid black 1px">Set your
          session id:
          <div>
            <input
                style="width: 100%"
                type="text"
                v-model="sessionId">
          </div>
        </div>
      </div>
      <div class="col-12 col-md-4">
        <div class="p-3" style="color: red; border: solid black 1px">Set your host:
          <div>
            <input
                style="width: 100%"
                type="text"
                v-model="host">
          </div>
        </div>
      </div>
      <div class="col-12 col-md-4">
        <div class="p-3" style="color: red; border: solid black 1px">Set your date to send:
          <div>
            <b-form-datepicker v-model="timeStampToSent" value-as-date class="mb-2"></b-form-datepicker>
          </div>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-12 col-md-4">
        <ButtonEvent :host="host" name="Button 1" :session-id="sessionId" :timestamp="timestamp"/>
      </div>
      <div class="col-12 col-md-4">
        <ButtonEvent :host="host" name="Button 2" :session-id="sessionId" :timestamp="timestamp"/>
      </div>
      <div class="col-12 col-md-4">
        <ButtonEvent :host="host" name="Button 3" :session-id="sessionId" :timestamp="timestamp"/>
      </div>
      <div class="col-12 col-md-4">
        <FormEvent :host="host" name="Form 1" :session-id="sessionId" :timestamp="timestamp"/>
      </div>
      <div class="col-12 col-md-4">
        <FormEvent :host="host" name="Form 2" :session-id="sessionId" :timestamp="timestamp"/>
      </div>
    </div>
    <div>
      <ListEvent/>
    </div>
  </div>
</template>

<script>
import ButtonEvent from './components/ButtonEvent.vue';
import FormEvent from './components/FormEvent.vue';
import ListEvent from './components/ListEvent.vue';

export default {
  name: 'App',
  data() {
    return {
      timeStampToSent: new Date(),
      sessionId: "",
      host: "www.consumeraffairs.com",
    }
  },
  components: {
    ButtonEvent,
    FormEvent,
    ListEvent
  },
  computed: {
    timestamp: function () {
      return this.timeStampToSent.toISOString()
    }
  },
  created() {
    this.sessionId = process.env.VUE_APP_SESSION_ID
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

<template>
  <div class="row">
    <div class="col-12 mb-2"><h2>Events</h2></div>
    <div class="col-12">
      <h3>Filters</h3>
      <form v-on:submit.prevent="loadEvents">
        <div class="row">
          <div class="col-12 col-md-3">
            Category:<input style="width: 100%" type="text" v-model="filterCategory">
          </div>
          <div class="col-12 col-md-3">
            Session Id:<input style="width: 100%" type="text" v-model="filterSessionId">
          </div>
          <div class="col-12 col-md-3">
            Date Range:
            <b-form-datepicker v-model="dateFrom" class="mb-2"></b-form-datepicker>
            <b-form-datepicker v-model="dateTo" class="mb-2"></b-form-datepicker>
          </div>
          <div class="col-12 col-md-2">
            <input type="submit" value="Fetch Events">
            <input type="button" @click="clearFilters" value="Clear Filters">
          </div>
        </div>
      </form>
    </div>
    <div class="row">
      <div v-for="event in events" :key="event.id" class="p-2 col-12 col-md-4 col-lg-3 text-center">
        <div class="border border-1 border-primary p-2">
          <h5>Event {{ event.name }} (Nro. {{ event.id }})</h5>
          <p>
            {{ event.data }}
          </p>
          <div>
            Category: {{ event.category }}
          </div>
          <div>
            Time Stamp: {{ event.timestamp }}
          </div>
          <div>
            Session Id: {{ event.session_id }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ListEvent",
  props: {
    host: String
  },
  data() {
    return {
      dateFrom: '',
      dateTo: '',
      events: [],
      filterCategory: '',
      filterSessionId: '',
    }
  },
  methods: {
    clearFilters: function () {
      this.filterSessionId = '';
      this.filterCategory = '';
      this.dateFrom = '';
      this.dateTo = '';
      this.events = [];
    },
    loadEvents: async function () {
      let params = {};
      if (this.filterCategory) {
        params = {...params, category: this.filterCategory}
      }
      if (this.filterSessionId) {
        params = {...params, session__id: this.filterSessionId}
      }
      if (this.dateFrom && this.dateTo) {
        params = {...params, date_from: this.dateFrom, date_to: this.dateTo}
      }
      const result = await axios.get(`${process.env.VUE_APP_API}/events/`, {params});
      this.events = result.data;
    },
  }
}
</script>

<style scoped>

</style>
<template>
  <div>
    <v-chip v-if="live" color="green" text-color="white" small>
      <i class="fa fa-circle mr-2" aria-hidden="true"></i>
      Online
    </v-chip>
    <v-chip v-else color="red" text-color="white" small>
      <i class="fa fa-circle mr-2" aria-hidden="true"></i>
      Offline
    </v-chip>
    <h1 class="mt-1">{{ carName }} - {{ firstname }} {{ lastname }}</h1>
    <i class="fa fa-map-marker mr-2"></i>{{ lat }}
    <i class="fa fa-map-marker mx-2"></i>{{ lon }}
    <i class="fas fa-mountain mx-2"></i>{{ alt }}
    <i class="fas fa-tachometer-alt mx-2"></i> {{ speed }}
    <span>KM/H</span>
  </div>
</template>

<script>
export default {
  props: {
    live: { default: false },
    lat: { default: 52.11323 },
    lon: { default: 12.123 },
    alt: { default: 12.123 },
    speed: { default: 30 },
    carName: {
      default: "Renia"
    },
    firstname: { default: "Adam" },
    lastname: { default: "Smith" }
  }
};
</script>

<style scoped>
@import "https://pro.fontawesome.com/releases/v5.10.0/css/all.css";
</style>

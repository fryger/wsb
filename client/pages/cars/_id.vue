<template>
  <v-container>
    <v-toolbar flat class="rounded-pill " height="50">
      <v-tabs
        v-if="!isMini"
        centered
        slider-color="#FFFFFF"
        color="#55BAB4"
        icons-and-text
      >
        <v-tab :to="`/cars/${$route.params.id}`" exact
          >Overview<v-icon>fa-eye</v-icon></v-tab
        >
        <v-tab :to="`/cars/${$route.params.id}/gauges`"
          >Gauges <v-icon>mdi-gauge</v-icon></v-tab
        >
        <v-tab :to="`/cars/${$route.params.id}/routes`"
          >Routes <v-icon>mdi-map-marker</v-icon></v-tab
        >

        <v-tab :to="`/cars/${$route.params.id}/damages`"
          >Damages <v-icon>fa-car-crash</v-icon></v-tab
        >
        <v-tab :to="`/cars/${$route.params.id}/documents`"
          >Documents <v-icon>mdi-file-document-outline</v-icon></v-tab
        >
        <v-tab :to="`/cars/${$route.params.id}/reminders`"
          >Reminders <v-icon>mdi-alarm</v-icon></v-tab
        >
      </v-tabs>

      <v-menu v-else content-class="elevation-0" :elevation="0">
        <template v-slot:activator="{ on, attrs }">
          <v-btn
            absolute
            right
            large
            color="#55BAB4"
            text
            v-bind="attrs"
            v-on="on"
          >
            <v-icon large>mdi-menu</v-icon>
          </v-btn>
        </template>
        <v-tabs vertical centered color="#55BAB4" icons-and-text>
          <v-tab :to="`/cars/${$route.params.id}`" exact
            >Overview<v-icon>fa-eye</v-icon></v-tab
          >
          <v-tab :to="`/cars/${$route.params.id}/gauges`"
            >Gauges <v-icon>mdi-gauge</v-icon></v-tab
          >
          <v-tab :to="`/cars/${$route.params.id}/routes`"
            >Routes <v-icon>mdi-map-marker</v-icon></v-tab
          >

          <v-tab :to="`/cars/${$route.params.id}/damages`"
            >Damages <v-icon>fa-car-crash</v-icon></v-tab
          >
          <v-tab :to="`/cars/${$route.params.id}/documents`"
            >Documents <v-icon>mdi-file-document-outline</v-icon></v-tab
          >
          <v-tab :to="`/cars/${$route.params.id}/reminders`"
            >Reminders <v-icon>mdi-alarm</v-icon></v-tab
          >
        </v-tabs>
      </v-menu>
    </v-toolbar>
    <div class="mt-4">
      <NuxtChild />
      <Overview v-if="$route.name == 'cars-id'" />
    </div>
  </v-container>
</template>

<script>
import Overview from "../../components/Overview.vue";

export default {
  components: {
    Overview
  },
  data() {
    return {};
  },
  computed: {
    isMini() {
      switch (this.$vuetify.breakpoint.name) {
        case "xs":
          return true;
        case "sm":
          return true;
        case "md":
          return false;
        case "lg":
          return false;
        case "xl":
          return false;
        default:
          return false;
      }
    }
  }
};
</script>

<style scoped>
.v-tabs__item--active {
  color: green;
}
</style>

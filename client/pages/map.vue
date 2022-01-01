<template>
  <v-app>
    <v-container>
      <div id="mapid" style="height: 97vh"></div>
    </v-container>
  </v-app>
</template>

<script>
import { mapGetters, mapActions, mapState } from "vuex";

import Vue from "vue";
import Vuetify from "vuetify";
import CarStatusPopup from "../components/CarStatusPopup.vue";

var DetailPopup = Vue.extend(CarStatusPopup);
DetailPopup.use(Vuetify);

export default {
  computed: {
    ...mapState({
      popoutData: state => state.map.list
    })
  },
  components: {
    CarStatusPopup
  },
  data() {
    return {
      markers: [],
      map: []
    };
  },
  head() {
    return {
      link: [
        {
          rel: "stylesheet",
          href: "https://unpkg.com/leaflet@1.6.0/dist/leaflet.css"
        }
      ]
    };
  },
  watch: {
    popoutData(value, oldValue) {
      if (JSON.stringify(value) !== JSON.stringify(oldValue)) {
        this.initPoints();
      }
    }
  },
  mounted() {
    this.$store.dispatch("map/getLatestStatus");
    this.initMap();
    this.initPoints();
    this.intervaljob = setInterval(() => {
      this.$store.dispatch("map/getLatestStatus");
    }, 3000);
  },
  beforeDestroy() {
    clearInterval(this.intervaljob);
  },
  methods: {
    initMap() {
      this.map = L.map("mapid").setView([53.570007, 10.0104954], 5);
      L.tileLayer(
        "https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}",
        {
          attribution:
            'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
          maxZoom: 18,
          id: "mapbox/streets-v11",
          tileSize: 512,
          zoomOffset: -1,
          accessToken:
            "pk.eyJ1IjoiZnJ5ZzNyIiwiYSI6ImNrdDkxNmwyZjExNWoycHBjY2JoaGRpOHEifQ.sPeP6CgU6f918oFMa2puog"
        }
      ).addTo(this.map);
      //this.markers = L.marker([12, 12]).addTo(this.map);
      // const instance = new DetailPopup({
      // propsData: { type: "primary" }
      //  }).$mount().$el;
      //  this.markers.bindPopup(instance).openPopup();
    },
    initPoints() {
      this.markers.forEach(element => {
        this.map.removeLayer(element);
      });
      this.popoutData.forEach(element => {
        var instance = new DetailPopup({
          propsData: {
            live: false,
            lat: element.gps?.lat,
            lon: element.gps?.lon,
            alt: element.gps?.alt,
            speed: element.gps?.speed,
            carName: element.name,
            firstname: element.driver?.first_name,
            lastname: element.driver?.last_name
          }
        }).$mount().$el;
        var caricon = L.icon({
          iconUrl: require("../assets/3dcaricon.svg"),
          iconSize: [38, 95],
          popupAnchor: [0, -15]
        });
        this.markers.push(
          L.marker([element.gps?.lat || 12, element.gps?.lon || 12], {
            icon: caricon
          })
            .bindPopup(instance, {
              minWidth: 350
            })
            .openPopup()
            .addTo(this.map)
        );
      });
    }
  }
};
</script>

<style scoped></style>

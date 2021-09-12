<template>
  <v-app>
    <v-container>
      <div id="mapid" style="height: 97vh"></div>
    </v-container>
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      map: {}
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
  mounted() {
    this.initMap();
  },
  methods: {
    initMap() {
      var mymap = L.map("mapid").setView([53.570007, 10.0104954], 5);
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
      ).addTo(mymap);
    }
  }
};
</script>

<style scoped></style>

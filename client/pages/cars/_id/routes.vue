<template>
  <v-container>
    <v-row>
      <v-col cols="2"> </v-col>
      <v-col cols="8"
        ><vc-date-picker v-model="date" is-expanded></vc-date-picker
      ></v-col>
      <v-col cols="2"> </v-col>
    </v-row>
    <v-row>
      <v-col cols="12">
        <v-card>
          <div id="mapid" style="height: 53vh"></div>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>
<script>
import { mapState, mapGetters } from "vuex";
export default {
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
  computed: {
    ...mapState({
      points: state => state.gps.points?.map(({ lat, lon }) => [lat, lon])
    })
  },
  data() {
    return {
      polylines: [],
      date: new Date()
    };
  },
  watch: {
    date: function(v) {
      if (v) {
        this.$store.dispatch("gps/getPointsRange", {
          id: this.$route.params.id,
          from: new Date(v.setHours(0, 0, 0)).toISOString(),
          to: new Date(v.setHours(23, 59, 59)).toISOString()
        });
      }
      //

      //this.map.fitBounds(polyline.getBounds());
    },
    points: function(v) {
      this.polylines.forEach(item => this.map.removeLayer(item));
      let gps = v
        .map(k => k.filter(Boolean))
        .filter(obj => !(obj && Object.keys(obj).length === 0));

      var polyline = L.polyline(gps, { color: "#55BEB7", weight: 8 }).addTo(
        this.map
      );

      this.polylines.push(polyline);
      try {
        this.map.fitBounds(polyline.getBounds());
      } catch (error) {}
    }
  },
  methods: {
    initMap() {
      this.map = L.map("mapid").setView([12, 12], 2);

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
    }
  },
  mounted() {
    this.initMap();
  }
};
</script>

<style scoped>
.centered-input >>> input {
  text-align: center;
  font-size: 28px;
}
</style>

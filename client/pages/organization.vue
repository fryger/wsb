<template>
  <div class="organization ma-auto">
    <v-container fluid>
      <v-row class="pa-16">
        <v-col md="4">
          <v-card color="#f8f8f8" height="100%">
            <v-img :src="logo"></v-img>

            <v-list-item class="px-10 pt-10">
              <v-list-item-content>
                <v-list-item-title class="text-h4 font-weight-bold pb-4">
                  Company information:
                </v-list-item-title>
                <v-list-item-title class="text-h5 ">
                  {{ organization }}
                </v-list-item-title>
                <v-list-item-title class="text-h5">
                  NIP: {{ nip }}
                </v-list-item-title>
                <v-list-item-title class="text-h5">
                  {{ street }} {{ streetNum }}, {{ postal }} {{ city }}
                </v-list-item-title>
              </v-list-item-content>
            </v-list-item>
            <v-card-actions>
              <v-btn color="deep-purple lighten-2" text @click="reserve">
                Reserve
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-col>

        <v-col align="center" md="8">
          <v-card color="#f8f8f8">
            <div id="mapid" style="height: 50vh"></div>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
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
  data: () => ({
    organization: "Organization",
    nip: "1112233444",
    city: "City",
    street: "Street",
    streetNum: "00",
    postal: "11222",
    logo: "https://via.placeholder.com/600x200",
    lat: "",
    lon: ""
  }),
  methods: {
    async getOrganization() {
      await this.$axios.get("/organization").then(res => {
        this.organization = res.data[0].name;
        this.nip = res.data[0].nip;
        this.city = res.data[0].city;
        this.street = res.data[0].street;
        this.streetNum = res.data[0].street_num;
        this.postal = res.data[0].postal_code;
        this.logo = res.data[0].logo;

        this.getCords(
          [this.street, this.streetNum, this.city, this.postal].join(" ")
        );
      });
    },
    async getCords(adress) {
      await this.$axios
        .get(
          `https://nominatim.openstreetmap.org/search?format=json&q=${adress}`
        )
        .then(res => {
          this.lat = res.data[0].lat;
          this.lon = res.data[0].lon;
          this.map();
        });
    },
    map() {
      var mymap = L.map("mapid").setView([this.lat, this.lon], 15);
      var marker = L.marker([this.lat, this.lon]).addTo(mymap);
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
  },
  mounted() {
    this.getOrganization();
  }
};
</script>

<style scoped></style>

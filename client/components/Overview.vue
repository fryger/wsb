<template>
  <v-container fluid>
    <v-row>
      <v-col>
        <v-card class="my-8" flat>
          <v-card-title class="text-h2">Information</v-card-title>
        </v-card>
      </v-col>
    </v-row>
    <v-row class="mt-1">
      <v-col cols="12" xl="6">
        <v-card elevation="2" class="rounded-xl" heigth="90vh">
          <v-carousel
            :continuous="false"
            :cycle="cycle"
            hide-delimiter-background
            delimiter-icon="mdi-minus"
            height="auto"
          >
            <v-carousel-item v-for="(slide, i) in slides" :key="i" eager>
              <v-img :src="slide" contain eager></v-img>
            </v-carousel-item>
          </v-carousel>
          <v-card-text class="pa-0">
            <v-row>
              <v-col cols="12" xl="6" class="pb-0">
                <v-btn text x-small tile block color="#388e3c"
                  ><v-icon>mdi-plus</v-icon></v-btn
                ></v-col
              >
              <v-col cols="12" xl="6" class="pb-0">
                <v-btn text x-small tile block color="#ff6659"
                  ><v-icon>mdi-delete</v-icon></v-btn
                >
              </v-col>
            </v-row>
          </v-card-text>
        </v-card>
      </v-col>
      <v-col cols="12" xl="6">
        <v-row justify="center">
          <v-col xl="8">
            <v-row align="center" class="mb-6">
              <v-col cols="11">
                <v-text-field
                  class="mt-6 "
                  outlined
                  flat
                  dense
                  label="Connection Token"
                  :type="showPassword ? 'password' : 'text'"
                  disabled
                  value="'asdasdasdasdasdad'"
                >
                </v-text-field>
              </v-col>
              <v-col cols="1">
                <v-icon @click="showToken">{{ tokenIcon }}</v-icon></v-col
              >
            </v-row>
          </v-col>
          <v-row>
            <v-col
              class="px-12 pa-0"
              cols="12"
              xl="6"
              md="4"
              sm="6"
              v-for="(element, i) in textFieldData"
              :key="i"
              ><v-text-field
                outlined
                dense
                :label="element.label"
              ></v-text-field
            ></v-col>
            <v-col
              class="px-12 pa-0"
              cols="12"
              xl="6"
              md="4"
              sm="6"
              v-for="(element, i) in selectFieldData"
              :key="i + 10"
            >
              <v-select
                outlined
                dense
                :label="element.label"
                :append-icon="element.ico"
                :items="element.type"
              >
              </v-select>
            </v-col>
            <v-col class="px-12 pt-0">
              <v-spacer></v-spacer>
              <v-btn block color="teal"
                >Update info<v-icon>mdi-pen</v-icon></v-btn
              >
            </v-col>
          </v-row>
        </v-row>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-card class="mt-12" flat>
          <v-card-title class="text-h2">Live data</v-card-title>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12" xl="6">
        <v-card class="mt-2" flat>
          <v-card-title class="text-h4">Map</v-card-title>
        </v-card>
        <v-card>
          <div id="mapid" style="height: 300px"></div>
        </v-card>
      </v-col>
      <v-col cols="12" xl="6">
        <v-card class="mt-2" flat>
          <v-card-title class="text-h4">Gauges</v-card-title>
        </v-card>
        <v-row>
          <v-col cols="12" xl="6">
            <apexchart
              width="500"
              type="bar"
              :options="options"
              :series="series"
            ></apexchart>
          </v-col>
          <v-col cols="12" xl="6"> </v-col>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      options: {
        chart: {
          id: "vuechart-example"
        },
        xaxis: {
          categories: [1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998]
        }
      },
      series: [
        {
          name: "series-1",
          data: [30, 40, 45, 50, 49, 60, 70, 91]
        }
      ],
      map: {},
      tokenIcon: "mdi-eye",
      showPassword: true,
      cycle: false,
      slides: [
        "https://ireland.apollo.olxcdn.com/v1/files/eyJmbiI6Ijk4cmc1NWszb2VsdTMtT1RPTU9UT1BMIiwidyI6W3siZm4iOiJ3ZzRnbnFwNnkxZi1PVE9NT1RPUEwiLCJzIjoiMTYiLCJwIjoiMTAsLTEwIiwiYSI6IjAifV19.paKqiX0StQvEOwmN05mUOYzxeUIofTkKeoZdBiB8-oU/image;s=1080x720",
        "https://ireland.apollo.olxcdn.com/v1/files/eyJmbiI6InhidTA0Y3BubnpmNzEtT1RPTU9UT1BMIiwidyI6W3siZm4iOiJ3ZzRnbnFwNnkxZi1PVE9NT1RPUEwiLCJzIjoiMTYiLCJwIjoiMTAsLTEwIiwiYSI6IjAifV19.qFQX8CXi1r_HAVI6Gga_P5Wa2wSRXdM8AaJh7yNTN_w/image;s=1080x720",
        "https://ireland.apollo.olxcdn.com/v1/files/eyJmbiI6InhidTA0Y3BubnpmNzEtT1RPTU9UT1BMIiwidyI6W3siZm4iOiJ3ZzRnbnFwNnkxZi1PVE9NT1RPUEwiLCJzIjoiMTYiLCJwIjoiMTAsLTEwIiwiYSI6IjAifV19.qFQX8CXi1r_HAVI6Gga_P5Wa2wSRXdM8AaJh7yNTN_w/image;s=1080x720",
        "https://ireland.apollo.olxcdn.com/v1/files/eyJmbiI6ImE4YjVsNHJhanltNzMtT1RPTU9UT1BMIiwidyI6W3siZm4iOiJ3ZzRnbnFwNnkxZi1PVE9NT1RPUEwiLCJzIjoiMTYiLCJwIjoiMTAsLTEwIiwiYSI6IjAifV19.vAvTxZ1MjSW0HZkAzr0zOQvTm-nNsuE_WKJgMrphIRA/image;s=1080x720",
        "https://ireland.apollo.olxcdn.com/v1/files/eyJmbiI6IjU1anlpenI2ZGNrazMtT1RPTU9UT1BMIiwidyI6W3siZm4iOiJ3ZzRnbnFwNnkxZi1PVE9NT1RPUEwiLCJzIjoiMTYiLCJwIjoiMTAsLTEwIiwiYSI6IjAifV19.Ufti8NEEI1pIqhUcsHJRsvP5tNwNVsKYn6dhhppXyyE/image;s=1080x720"
      ],
      value: {
        bodyType: "",
        fuelType: "",
        carStatus: "",
        name: "",
        manufacturer: "",
        model: "",
        mileage: "",
        vin: "",
        year: "",
        engine: "",
        driver: "",
        status: "",
        token: "tajemny token"
      },
      textFieldData: [
        { label: "Name", model: "name", rule: "required" },
        { label: "Manufacturer", model: "manufacturer", rule: "required" },
        { label: "Model", model: "model", rule: "required" },
        {
          label: "Model year",
          model: "year",
          rule: "required|modelyear:1800,3000"
        },
        {
          label: "Engine",
          model: "engine",
          rule: "required|numeric|max_value:50"
        },
        { label: "Mileage", model: "mileage", rule: "required|numeric" },
        { label: "VIN", model: "vin", rule: "required|alpha_num" }
      ],
      selectFieldData: [
        {
          label: "Body type",
          ico: "mdi-car-door",
          type: [
            "Hatchback",
            "Sedan",
            "SUV",
            "Sedan",
            "Convertible",
            "Estate",
            "VAN"
          ],
          model: "bodyType",
          rule: "required"
        },
        {
          label: "Fuel type",
          ico: "mdi-gas-station",
          type: ["Petrol", "BIO", "LPG", "Diesel", "Electric", "Hybrid"],
          model: "fuelType",
          rule: "required"
        },
        {
          label: "Status",
          ico: "mdi-heart-pulse",
          type: ["In Use", "Out of order", "Service"],
          model: "status",
          rule: "required"
        },
        {
          label: "Driver",
          ico: "mdi-account",
          type: this.$store.state.driver.list,
          model: "driver",
          rule: ""
        }
      ]
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
    showToken() {
      this.showPassword = !this.showPassword;
      this.tokenIcon = this.showPassword ? "mdi-eye" : "mdi-eye-off";
    },
    initMap() {
      var mymap = L.map("mapid").setView([53.570007, 10.1104954], 13);
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
      L.marker([53.570007, 10.1104954])
        .bindTooltip("Last GPS signal", {
          permanent: true
        })
        .addTo(mymap);
    }
  }
};
</script>

<style scoped>
.innergauge {
  position: absolute;
  left: 50%;
  top: 50%;
  -webkit-transform: translate(-50%, -20%);
  transform: translate(-50%, -20%);
}
p {
  text-align: center;
}

.v-text-field--outlined >>> fieldset {
  border-color: #52b2ab;
}
</style>

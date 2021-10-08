<template>
  <v-container>
    <v-row>
      <v-col cols="12" xl="4">
        <v-card elevation="2">
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
      <v-col cols="12" xl="8">
        <v-card elevation="2" height="100%">
          <v-card-title class="text-h3 mb-6 font-weight-bold"
            >Car information</v-card-title
          >
          <v-card-text>
            <v-row>
              <v-col
                cols="12"
                xl="3"
                md="4"
                sm="6"
                v-for="(element, i) in textFieldData"
                :key="i"
                ><v-text-field
                  :disabled="disabled"
                  dense
                  :label="element.label"
                ></v-text-field
              ></v-col>
              <v-col
                cols="12"
                xl="3"
                md="4"
                sm="6"
                v-for="(element, i) in selectFieldData"
                :key="i + 10"
              >
                <v-select
                  dense
                  :disabled="disabled"
                  :label="element.label"
                  :prepend-icon="element.ico"
                  :items="element.type"
                >
                </v-select>
              </v-col>
              <v-col cols="12" xl="3" md="4" sm="6" align="center">
                <v-text-field
                  dense
                  label="Token"
                  v-model="value.token"
                  :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
                  :type="showPassword ? 'text' : 'password'"
                  @click:append="showPassword = !showPassword"
                >
                </v-text-field>

                <v-btn
                  class="mx-2"
                  fab
                  small
                  absolute
                  bottom
                  style="right: 80px;"
                  @click="disabled = !disabled"
                  ><v-icon>mdi-pencil</v-icon></v-btn
                >
                <v-btn class="mx-2" fab small absolute bottom right
                  ><v-icon>mdi-send</v-icon></v-btn
                >
              </v-col>
            </v-row>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12" xl="4">
        <v-card>
          <div id="mapid" style="height: 300px"></div>
        </v-card>
      </v-col>
      <v-col cols="12" xl="3">
        <v-card height="100%">
          <v-card-subtitle>Driver history</v-card-subtitle>
          <v-card-text>
            <v-timeline>
              <v-timeline-item>
                <template v-slot:icon>
                  <v-avatar>
                    <img src="https://i.pravatar.cc/64" />
                  </v-avatar>
                </template>
                <strong>Krzysztof Fryger</strong>
                <div class="text-caption">
                  24 May 2019
                </div>
                <div class="text-caption">
                  500 000 km
                </div>
              </v-timeline-item>
              <v-timeline-item>
                <template v-slot:icon>
                  <v-avatar size="40">
                    <img src="https://i.pravatar.cc/61" />
                  </v-avatar> </template
                ><strong>Krzysztof Fryger</strong>
                <div class="text-caption">
                  24 May 2019
                </div>
                <div class="text-caption">
                  500 000 km
                </div>
              </v-timeline-item>
              <v-timeline-item>
                <template v-slot:icon>
                  <v-avatar size="40">
                    <img src="https://i.pravatar.cc/63" />
                  </v-avatar>
                </template>
                <strong>Krzysztof Fryger</strong>
                <div class="text-caption">
                  24 May 2019
                </div>
                <div class="text-caption">
                  500 000 km
                </div></v-timeline-item
              >
            </v-timeline>
          </v-card-text>
        </v-card>
      </v-col>
      <v-col cols="12" xl="4">
        <v-card class="fuelcard rounded-lg ">
          <v-img
            class="white--text align-end "
            height="250"
            src="https://images.all-free-download.com/images/graphicthumb/traffic_at_night_184569.jpg"
          >
            <v-card-title
              ><v-avatar tile size="90"
                ><v-img
                  contain
                  src="https://upload.wikimedia.org/wikipedia/sco/d/d2/BP_Helios_logo.svg"
                ></v-img></v-avatar
              ><v-spacer></v-spacer>
              <p>Fuel Card</p>
            </v-card-title>
            <v-card-text class="mt-2">
              <v-row>
                <v-col
                  class="d-flex justify-center"
                  cols="12"
                  xl="12"
                  style="font-size:40px; background-color:rgba(0,0,0,0.4); "
                >
                  <div>533674 585844 106011</div></v-col
                >
                <v-col cols="12" xl="12" class="text-h6">
                  <v-row>
                    <v-col cols="12" xl="6">
                      <div>Ecol-Unicon Sp z o.o.</div>
                      <div>GWE 19423</div>
                    </v-col>
                    <v-col cols="12" xl="6">
                      <div class="mt-2 mr-4">
                        <p class="text-h5 text-right ">
                          2702
                        </p>
                      </div>
                    </v-col>
                  </v-row>
                </v-col>
              </v-row>
            </v-card-text>
          </v-img>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12" xl="2">
        <VueSvgGauge
          :start-angle="-110"
          :end-angle="110"
          value="80"
          separatorThickness="5"
          :separator-step="20"
          :scale-interval="10"
          :inner-radius="80"
          :gaugeColor="[
            { offset: 0, color: 'red' },
            { offset: 100, color: 'yellow' }
          ]"
        >
          <div>
            <div class="innergauge">
              <p class="mb-0">AVG Speed</p>
              <p class="mb-0">67 Km/h</p>
            </div>
          </div>
        </VueSvgGauge>
      </v-col>
      <v-col cols="12" xl="4">
        <v-sheet class="v-sheet--offset mx-auto" color="#52B2AB" elevation="12">
          <v-sparkline
            :labels="labels"
            :value="values"
            color="white"
            line-width="2"
            padding="16"
          ></v-sparkline>
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import Driver from "../../../components/Driver.vue";

export default {
  components: {
    Driver
  },
  data() {
    return {
      labels: ["12am", "3am", "6am", "9am", "12pm", "3pm", "6pm", "9pm"],
      values: [200, 675, 410, 390, 310, 460, 250, 240],
      map: {},
      disabled: true,
      showPassword: false,
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
      ],
      colors: [
        "green",
        "secondary",
        "yellow darken-4",
        "red lighten-2",
        "orange darken-1"
      ],
      cycle: false,
      slides: [
        "https://ireland.apollo.olxcdn.com/v1/files/eyJmbiI6Ijk4cmc1NWszb2VsdTMtT1RPTU9UT1BMIiwidyI6W3siZm4iOiJ3ZzRnbnFwNnkxZi1PVE9NT1RPUEwiLCJzIjoiMTYiLCJwIjoiMTAsLTEwIiwiYSI6IjAifV19.paKqiX0StQvEOwmN05mUOYzxeUIofTkKeoZdBiB8-oU/image;s=1080x720",
        "https://ireland.apollo.olxcdn.com/v1/files/eyJmbiI6InhidTA0Y3BubnpmNzEtT1RPTU9UT1BMIiwidyI6W3siZm4iOiJ3ZzRnbnFwNnkxZi1PVE9NT1RPUEwiLCJzIjoiMTYiLCJwIjoiMTAsLTEwIiwiYSI6IjAifV19.qFQX8CXi1r_HAVI6Gga_P5Wa2wSRXdM8AaJh7yNTN_w/image;s=1080x720",
        "https://ireland.apollo.olxcdn.com/v1/files/eyJmbiI6InhidTA0Y3BubnpmNzEtT1RPTU9UT1BMIiwidyI6W3siZm4iOiJ3ZzRnbnFwNnkxZi1PVE9NT1RPUEwiLCJzIjoiMTYiLCJwIjoiMTAsLTEwIiwiYSI6IjAifV19.qFQX8CXi1r_HAVI6Gga_P5Wa2wSRXdM8AaJh7yNTN_w/image;s=1080x720",
        "https://ireland.apollo.olxcdn.com/v1/files/eyJmbiI6ImE4YjVsNHJhanltNzMtT1RPTU9UT1BMIiwidyI6W3siZm4iOiJ3ZzRnbnFwNnkxZi1PVE9NT1RPUEwiLCJzIjoiMTYiLCJwIjoiMTAsLTEwIiwiYSI6IjAifV19.vAvTxZ1MjSW0HZkAzr0zOQvTm-nNsuE_WKJgMrphIRA/image;s=1080x720",
        "https://ireland.apollo.olxcdn.com/v1/files/eyJmbiI6IjU1anlpenI2ZGNrazMtT1RPTU9UT1BMIiwidyI6W3siZm4iOiJ3ZzRnbnFwNnkxZi1PVE9NT1RPUEwiLCJzIjoiMTYiLCJwIjoiMTAsLTEwIiwiYSI6IjAifV19.Ufti8NEEI1pIqhUcsHJRsvP5tNwNVsKYn6dhhppXyyE/image;s=1080x720"
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
    initMap() {
      var mymap = L.map("mapid").setView([53.570007, 10.1104954], 14);
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
@import url("https://fonts.googleapis.com/css2?family=PT+Sans&display=swap");

.fuelcard {
  font-family: "PT Sans", sans-serif;
  color: white;
  text-shadow: 2px 2px #000;
}
.innergauge {
  position: absolute;
  left: 50%;
  top: 50%;
  -webkit-transform: translate(-50%, 0%);
  transform: translate(-50%, 0%);
}
</style>

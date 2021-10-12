<template>
  <v-container fluid>
    <v-dialog hide-overlay :value="alert" width="400px">
      <v-alert
        v-for="item in alertData"
        :key="item"
        class="ma-0"
        type="error"
        transition="fade-transition"
      >
        {{ item }}
      </v-alert>
    </v-dialog>
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
            v-model="carouselIndex"
            :continuous="false"
            :cycle="cycle"
            hide-delimiter-background
            delimiter-icon="mdi-minus"
            height="auto"
          >
            <v-carousel-item v-for="slide in slides" :key="slide.id" eager>
              <v-img :src="slide.url" contain eager></v-img>
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
                <v-btn
                  text
                  x-small
                  tile
                  block
                  color="#ff6659"
                  @click="removePicture"
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
                  :value="car.token"
                >
                </v-text-field>
              </v-col>
              <v-col cols="1">
                <v-icon @click="showToken">{{ tokenIcon }}</v-icon></v-col
              >
            </v-row>
          </v-col>
          <ValidationObserver ref="carForm">
            <v-form>
              <v-row>
                <v-col
                  class="px-12 pa-0"
                  cols="12"
                  xl="6"
                  md="4"
                  sm="6"
                  v-for="(element, i) in textFieldData"
                  :key="i"
                >
                  <ValidationProvider :rules="element.rule" v-slot="{ errors }">
                    <v-text-field
                      outlined
                      dense
                      v-model="value[element.model]"
                      :error-messages="errors"
                      :label="element.label"
                    ></v-text-field>
                  </ValidationProvider>
                </v-col>
                <v-col
                  class="px-12 pa-0"
                  cols="12"
                  xl="6"
                  md="4"
                  sm="6"
                  v-for="(element, i) in selectFieldData"
                  :key="i + 10"
                >
                  <ValidationProvider v-slot="{ errors }" :rules="element.rule">
                    <v-select
                      outlined
                      dense
                      :label="element.label"
                      :append-icon="element.ico"
                      :items="element.type"
                      :error-messages="errors"
                      v-model="value[element.model]"
                      name="element"
                      item-text="username"
                      return-object
                    >
                    </v-select>
                  </ValidationProvider>
                </v-col>
                <v-col class="px-12 pt-0">
                  <v-spacer></v-spacer>
                  <v-btn block color="teal" @click="submit"
                    >Update info<v-icon>mdi-pen</v-icon></v-btn
                  >
                </v-col>
              </v-row>
            </v-form>
          </ValidationObserver>
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
      <v-col cols="12" xl="3"><Chart chartTitle="Speed" /> </v-col>
      <v-col cols="12" xl="3"><Chart chartTitle="RPM" /> </v-col>
      <v-col cols="12" xl="3"> <Chart chartTitle="Oil temperature"/></v-col>
      <v-col cols="12" xl="3"><Chart chartTitle="Coolant temperature"/></v-col>
    </v-row>
    <v-row>
      <v-col cols="12">
        <v-card flat>
          <v-card-title class="text-h4">Map</v-card-title>
        </v-card>
        <v-card>
          <div id="mapid" style="height: 500px"></div>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { ValidationProvider, ValidationObserver } from "vee-validate";
import Chart from "./Chart.vue";
export default {
  components: {
    ValidationProvider,
    ValidationObserver,
    Chart
  },
  created() {
    this.$store.dispatch("car/getCar", this.$route.params.id);
    this.$store.dispatch("car/getPictures", this.$route.params.id);
  },
  computed: {
    slides() {
      const arr = this.$store.state.car.gallery;
      let output = [];
      arr.forEach(element => {
        output.push({
          id: element["id"],
          url: "http://localhost:8000" + element["file"]
        });
      });
      return output;
    },
    car() {
      const car = this.$store.state.car.list;
      this.value.bodyType = car.body;
      this.value.fuelType = car.fuel;
      this.value.status = car.status;
      this.value.name = car.name;
      this.value.manufacturer = car.manufacturer;
      this.value.mileage = car.mileage;
      this.value.vin = car.vin;
      this.value.year = car.year;
      this.value.engine = car.engine;
      this.value.driver = car.driver;
      this.value.model = car.model;
      return car;
    }
  },
  data() {
    return {
      carouselIndex: "",
      map: {},
      tokenIcon: "mdi-eye",
      showPassword: true,
      cycle: false,

      alert: false,
      alertData: {},
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
          rule: "required|max_value:50"
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
            "VAN",
            "Coupe"
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
          type: ["In use", "Free", "Broken", "Service", "Transport"],
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
    removePicture() {
      this.$axios
        .delete(
          `cars/${this.$route.params.id}/gallery/${
            this.slides[this.carouselIndex]?.id
          }`
        )
        .then()
        .catch()
        .then(this.$store.dispatch("car/getPictures", this.$route.params.id));
    },
    async submit() {
      const isValid = await this.$refs.carForm.validate();
      let data = {
        body: this.value.bodyType,
        status: this.value.status,
        fuel: this.value.fuelType,
        driver: this.value.driver?.id,
        name: this.value.name,
        manufacturer: this.value.manufacturer,
        model: this.value.model,
        mileage: this.value.mileage,
        vin: this.value.vin,
        year: this.value.year,
        engine: this.value.engine
      };
      if (isValid) {
        this.$axios
          .put(`cars/${this.$route.params.id}/`, data)
          .then()
          .catch(error => {
            if (error.response) {
              console.log(error.response);
              try {
                let alertData = [];
                JSON.stringify(error.response.data, (key, value) => {
                  if (key === "0") alertData.push(value);
                  return value;
                });
                this.alertData = alertData;
              } catch (e) {}
              this.alert = true;
              console.log(this.alertData);
              setTimeout(() => (this.alert = false), 5000);
            }
          })
          .then(this.$store.dispatch("car/getCar", this.$route.params.id));
      }
    },
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
p {
  text-align: center;
}

.v-text-field--outlined >>> fieldset {
  border-color: #52b2ab;
}
</style>

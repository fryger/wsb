<template>
  <v-container>
    <v-row>
      <v-icon slot="prependIcon" class="pr-3" large>mdi-magnify</v-icon>
      <v-text-field label="Search" height="50" v-model="search"></v-text-field>
    </v-row>
    <v-row>
      <v-btn
        @click="dialog = true"
        color="green"
        elevation="1"
        class="ma-2"
        rounded
        outlined
        ><v-icon left dark>mdi-plus</v-icon> Add car
      </v-btn>
    </v-row>
    <v-row class=" mt-12">
      <v-layout child-flex>
        <v-data-table
          :headers="headers"
          :items="cars"
          class="elevation-1"
          hide-default-footer
          width="100%"
          disable-pagination
          @click:row="handleClick"
        >
          <template v-slot:[`item.status`]="{ item }">
            <v-chip :color="getColor(item.status)" dark>
              {{ item.status }}
            </v-chip>
          </template>
          <template v-slot:[`item.fuel`]="{ item }">
            <v-icon left :color="fuelColor(item.fuel)">
              {{ fuelIcon(item.fuel) }}
            </v-icon>
            {{ item.fuel }}
          </template>
          <template v-slot:[`item.mileage`]="{ item }">
            {{ numberWithSpaces(item.mileage) }}
          </template>
          <template v-slot:[`item.driver`]="{ item }">
            {{ getDriverById(item.driver) }}
          </template>
        </v-data-table>
      </v-layout>
    </v-row>
    <!-- Add car form -->
    <v-navigation-drawer
      v-model="dialog"
      absolute
      right
      width="500"
      style="max-height:100vh; position: fixed;"
    >
      <AddCarForm />
    </v-navigation-drawer>
  </v-container>
</template>

<script>
//import UserReg from "../../components/UserReg.vue";
import AddCarForm from "../../components/AddCarForm.vue";
import Driver from "../../components/Driver.vue";
import { mapGetters, mapActions } from "vuex";

export default {
  components: {
    Driver,
    AddCarForm
  },
  data() {
    return {
      dialog: false,
      search: "",
      headers: [
        { text: "Body", value: "body", align: "center" },
        { text: "Name", align: "start", value: "name" },
        { text: "Manufacturer", value: "manufacturer", align: "center" },
        { text: "Model", value: "model", align: "center" },
        { text: "Engine", value: "engine", align: "center" },
        { text: "Fuel", value: "fuel", align: "center" },
        { text: "Model year", value: "year", align: "center" },
        { text: "Mileage (km)", value: "mileage", align: "center" },
        { text: "VIN", value: "vin", align: "center" },
        { text: "Driver", value: "driver", align: "center" },
        { text: "Status", value: "status", align: "center" }
      ]
    };
  },
  methods: {
    handleClick(row) {
      console.log(row);
      this.$router.push(`cars/${row.id}`);
    },
    getColor(status) {
      return status == "In Use"
        ? "green"
        : status == "Out of order"
        ? "red"
        : "blue";
    },
    numberWithSpaces(x) {
      return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, " ");
    },

    fuelColor(x) {
      switch (x) {
        case "Petrol":
          return "green";
          break;
        case "BIO":
          return "blue";
          break;
        case "Diesel":
          return "black";
          break;
        case "Electric":
          return "yellow";
          break;
        case "LPG":
          return "red";
          break;
        case "Hybrid":
          return "lime";
          break;
      }
    },
    fuelIcon(x) {
      switch (x) {
        case "Petrol":
          return "mdi-gas-station";
          break;
        case "BIO":
          return "fa-leaf";
          break;
        case "Diesel":
          return "fa-oil-can";
          break;
        case "Electric":
          return "mdi-lightning-bolt-circle";
          break;
        case "LPG":
          return "fa-burn";
          break;
        case "Hybrid":
          return "fa-battery-half";
          break;
      }
    }
  },

  created() {
    this.$store.dispatch("cars/getCars");
  },
  computed: {
    ...mapGetters({ getDriverById: "driver/idDriver" }),
    cars() {
      return this.$store.state.cars.list;
    }
  }
};
</script>

<style scoped></style>

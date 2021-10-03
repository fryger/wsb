<template>
  <v-card height="100%" color="#f8f8f8" class="d-flex flex-column">
    <v-card-title class="justify-center text-h3 pt-10 mb-4"
      >New vehicle</v-card-title
    >
    <v-card-text class="px-12">
      <v-form>
        <v-text-field
          v-for="(element, i) in textFieldData"
          :key="i"
          outlined
          dense
          :label="element.label"
          v-model="value[element.model]"
        >
        </v-text-field>
        <v-select
          v-for="(element, i) in selectFieldData"
          :key="i"
          outlined
          dense
          :label="element.label"
          :prepend-icon="element.ico"
          :items="element.type"
          v-model="value[element.model]"
        ></v-select>
      </v-form>
    </v-card-text>
    <v-spacer></v-spacer>
    <v-card-actions>
      <v-btn
        class="mx-2 btn-edit"
        small
        text
        color="error"
        @click="dialog = false"
        ><v-icon dark>
          mdi-close
        </v-icon>
      </v-btn>
    </v-card-actions>
    <v-btn block color="success">Create</v-btn>
  </v-card>
</template>

<script>
export default {
  data() {
    return {
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
        engine: ""
      },
      textFieldData: [
        { label: "Name", model: "name" },
        { label: "Manufacturer", model: "manufacturer" },
        { label: "Model", model: "model" },
        { label: "Model year", model: "year" },
        { label: "Engine", model: "engine" },
        { label: "Mileage", model: "mileage" },
        { label: "VIN", model: "vin" }
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
          model: "bodyType"
        },
        {
          label: "Fuel type",
          ico: "mdi-gas-station",
          type: ["Petrol", "BIO", "LPG", "Diesel", "Electric", "Hybrid"],
          model: "fuelType"
        },
        {
          label: "Status",
          ico: "mdi-heart-pulse",
          type: ["In Use", "Out of order", "Service"],
          model: "carStatus"
        }
      ]
    };
  }
};
</script>

<style scoped>
.btn-edit {
  position: absolute;
  right: -8px;
  top: 0;
  z-index: 1;
}
</style>

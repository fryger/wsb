<template>
  <v-card height="100%" class="d-flex flex-column ">
    <v-alert
      v-for="item in alertData"
      :key="item"
      :value="alert"
      class="ma-0"
      type="error"
      transition="fade-transition"
    >
      {{ item }}
    </v-alert>

    <v-card-title class="justify-center text-h3 pt-10 mb-4"
      >New vehicle</v-card-title
    >
    <v-card-text class="px-12">
      <ValidationObserver ref="carForm">
        <v-form>
          <ValidationProvider
            v-for="(element, i) in textFieldData"
            :key="i"
            :rules="element.rule"
            v-slot="{ errors }"
          >
            <v-text-field
              outlined
              dense
              :label="element.label"
              :error-messages="errors"
              v-model="value[element.model]"
            >
            </v-text-field>
          </ValidationProvider>
          <ValidationProvider
            v-for="(element, i) in selectFieldData"
            :key="i + 10"
            v-slot="{ errors }"
            :rules="element.rule"
          >
            <v-select
              outlined
              dense
              :error-messages="errors"
              :label="element.label"
              :prepend-icon="element.ico"
              :items="element.type"
              v-model="value[element.model]"
              name="element"
              item-text="username"
              return-object
            ></v-select>
          </ValidationProvider>
        </v-form>
      </ValidationObserver>
    </v-card-text>
    <v-spacer></v-spacer>
    <v-card-actions>
      <v-btn
        class="mx-2 btn-edit"
        small
        text
        color="error"
        v-on:click="$emit('close-dialog')"
        ><v-icon dark>
          mdi-close
        </v-icon>
      </v-btn>
      <v-btn block large color="success" @click="submit">Create</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import { ValidationProvider, ValidationObserver } from "vee-validate";

export default {
  components: {
    ValidationProvider,
    ValidationObserver
  },
  created() {
    this.$store.dispatch("driver/getDriver");
  },
  methods: {
    async submit() {
      const isValid = await this.$refs.carForm.validate();
      let data = {
        body: this.value.bodyType,
        status: this.value.status,
        fuel: this.value.fuelType,
        driver: this.value.driver.id,
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
          .post("cars", data)
          .then(response => this.$emit("close-dialog"))
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
          });
      }
    }
  },
  data() {
    return {
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
        status: ""
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

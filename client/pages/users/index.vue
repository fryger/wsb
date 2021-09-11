<template>
  <v-container>
    <v-row>
      <v-icon slot="prependIcon" class="pr-3" large>mdi-magnify</v-icon>
      <v-text-field label="Search" height="50"></v-text-field>
    </v-row>
    <v-row>
      <v-btn
        @click="dialog = true"
        color="green"
        elevation="1"
        class="ma-2"
        rounded
        outlined
        ><v-icon left dark>mdi-plus</v-icon> Add driver
      </v-btn>
    </v-row>
    <v-row class="ma-4 mt-12">
      <Driver
        v-for="driver in drivers"
        :key="driver.id"
        :name="driver.first_name"
        :lastName="driver.last_name"
        :nick="driver.username"
      />
    </v-row>
    <!-- Add driver form -->
    <v-dialog
      transition="fade-transition"
      max-width="800"
      style="z-index:9999;"
      v-model="dialog"
    >
      <v-card>
        <v-card-title class="justify-center text-h3 mb-4"
          >Register new driver</v-card-title
        >
        <UserReg v-on:close-dialog="dialog = false" url="/drivers" />
        <v-card-action>
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
        </v-card-action>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
import UserReg from "../../components/UserReg.vue";
import Driver from "../../components/Driver.vue";

export default {
  components: {
    Driver
  },
  data() {
    return {
      dialog: false
    };
  },
  created() {
    this.$store.dispatch("driver/getDriver");
  },
  computed: {
    drivers() {
      return this.$store.state.driver.list;
    }
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

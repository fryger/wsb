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
    <v-navigation-drawer v-model="dialog" absolute right width="500">
      <v-card height="100%" color="#f8f8f8">
        <v-card-title class="justify-center text-h3 pt-10 mb-4"
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
    </v-navigation-drawer>
  </v-container>
</template>

<script>
import UserReg from "../../components/UserReg.vue";
import Driver from "../../components/Driver.vue";
import { mapGetters, mapActions } from "vuex";

export default {
  components: {
    Driver
  },
  data() {
    return {
      dialog: false,
      search: ""
    };
  },
  created() {
    this.$store.dispatch("driver/getDriver");
  },
  computed: {
    ...mapGetters({ searchDriver: "driver/searchDriver" }),
    drivers() {
      return this.search == ""
        ? this.$store.state.driver.list
        : this.searchDriver(this.search.toLowerCase());
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

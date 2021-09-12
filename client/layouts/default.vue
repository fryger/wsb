<template>
  <v-app>
    <v-navigation-drawer
      app
      permanent
      mini-variant="mini"
      :mini-variant.sync="mini"
    >
      <v-list>
        <v-list-item link class="px-2">
          <v-list-item-avatar>
            <v-img
              src="https://afa.org.sg/wp-content/uploads/2014/05/icon-user-default-copy.png"
            ></v-img>
          </v-list-item-avatar>
          <v-list-item-content>
            <v-list-item-title class="text-h6">
              {{ username }}
            </v-list-item-title>
            <v-list-item-subtitle>{{ email }}</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </v-list>
      <v-list shaped>
        <v-list-item-group v-model="selectedItem" color="#ff964f">
          <v-list-item
            v-for="([icon, text, href], i) in items"
            :key="i"
            link
            class="px-2"
            :to="href"
          >
            <v-list-item-icon>
              <v-icon>{{ icon }}</v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title>{{ text }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>

    <v-main>
      <Nuxt />
    </v-main>
  </v-app>
</template>

<script>
export default {
  data: () => ({
    selectedItem: "",
    username: "",
    email: "",
    organization: "",
    access: "",
    items: [
      ["mdi-view-dashboard-variant", "Dashboard", "/dashboard"],
      ["mdi-domain", "Organization", "/organization"],
      ["mdi-map", "Map", "/map"],
      ["mdi-account", "Drivers", "/users"],
      ["mdi-car", "Cars", "/cars"]
    ]
  }),
  mounted() {
    this.username = this.$auth.$state.user[0].username;
    this.email = this.$auth.$state.user[0].email;
    this.organization = this.$auth.$state.user[0].organization;
    this.access =
      this.$auth.$state.user[0].organization_permission == "9"
        ? "Admin"
        : "Driver";
  },

  methods: {
    async logout() {
      await this.$auth.logout();

      this.$router.push("/login");
    }
  },
  computed: {
    mini() {
      switch (this.$vuetify.breakpoint.name) {
        case "xs":
          return true;
        case "sm":
          return true;
        case "md":
          return true;
        case "lg":
          return false;
        case "xl":
          return false;
      }
    }
  }
};
</script>

<style>
html {
  overflow-y: auto;
}
</style>

<template>
  <v-app>
    <v-navigation-drawer
      app
      dark
      permanent
      mini-variant="mini"
      :mini-variant.sync="mini"
    >
      <v-list-item v-if="this.mini == false" align="center" justify="center">
        <v-list-item-content>
          <v-list-item-title class="text-h4">
            {{ organization }}
          </v-list-item-title>
          <v-list-item-subtitle>{{ access }}</v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
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
        <v-list-item-content
          ><v-btn block elevation="2" small @click="logout">
            Logout</v-btn
          ></v-list-item-content
        >
      </v-list>
      <v-divider></v-divider>
      <v-list rounded>
        <v-list-item-group v-model="selectedItem" color="accent">
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
      <v-container fluid>
        <Nuxt />
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  data: () => ({
    //mini: true,
    selectedItem: "",
    username: "",
    email: "",
    organization: "",
    access: "",
    items: [
      ["mdi-view-dashboard-variant", "Dashboard", "/dashboard"],
      ["mdi-domain", "Organization", "/organization"],
      ["mdi-map", "Map", "/map"]
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

<style></style>

<template>
  <v-app>
    <v-dialog hide-overlay :value="alert" width="400px">
      <v-alert class="mb-0" type="error" transition="fade-transition">
        Wrong credentials!!
      </v-alert>
    </v-dialog>
    <div class="center-me">
      <v-card class="pa-12 " min-width="500px">
        <v-responsive :aspect-ratio="1 / 1">
          <v-form ref="form">
            <v-container>
              <v-card-title class="justify-center text-h2 mb-4"
                >Log In</v-card-title
              >
              <v-row>
                <v-col cols="12" md="12">
                  <v-text-field
                    v-model="login"
                    label="Login"
                    :rules="[rules.required]"
                    required
                  ></v-text-field>
                </v-col>
              </v-row>
              <v-row>
                <v-col cols="12" md="12">
                  <v-text-field
                    v-model="password"
                    label="Password"
                    type="password"
                    :rules="[rules.required]"
                    required
                  ></v-text-field>
                </v-col>
              </v-row>

              <v-row class="ab">
                <v-col cols="12" md="12">
                  <v-btn
                    @click="loginHandler"
                    block
                    color="primary"
                    elevation="1"
                    outlined
                    x-large
                    >Login</v-btn
                  >
                </v-col>
              </v-row>
            </v-container>
          </v-form>
        </v-responsive>
      </v-card>
    </div>
  </v-app>
</template>

<script>
export default {
  head() {
    return {
      title: "Login page"
    };
  },
  data: () => ({
    alert: false,
    login: "",
    password: "",
    rules: {
      required: v => !!v || "Fields required"
    }
  }),
  methods: {
    async loginHandler() {
      if (this.$refs.form.validate()) {
        const data = { username: this.login, password: this.password };
        try {
          const response = await this.$auth.loginWith("local", { data: data });
          await this.$auth.setUserToken(
            response.data.access,
            response.data.refresh
          );
        } catch (e) {
          let errorCode = e.response.status;
          if (errorCode == 401) {
            this.alert = true;
            setTimeout(() => (this.alert = false), 2000);
          }
        }
      }
    }
  },
  layout: "loginLayout"
};
</script>

<style scoped>
v-dialog {
  position: sticky;
  top: 0;
}

body,
html {
  height: 100%;
  display: grid;
}

.center-me {
  margin: auto;
}

.ab {
  width: 100%;
  position: absolute;
  bottom: 1%;
}
</style>

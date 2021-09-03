<template>
  <v-app>
    <v-dialog hide-overlay :value="alert" width="400px">
      <v-alert
        v-for="item in alertData"
        :key="item"
        class="mt-2"
        type="error"
        transition="fade-transition"
      >
        {{ item }}
      </v-alert>
    </v-dialog>
    <div class="center-me">
      <v-card class="pa-12 float-left ma-10" min-width="500px">
        <v-responsive :aspect-ratio="1 / 1">
          <v-form ref="form">
            <v-container>
              <v-card-title class="justify-center text-h2 mb-4">
                Register user</v-card-title
              >
              <v-row>
                <v-col cols="12" md="12">
                  <v-text-field
                    v-model="name"
                    label="Name"
                    :error-messages="nameErrors"
                    @input="$v.name.$touch()"
                    @blur="$v.name.$touch()"
                    required
                  ></v-text-field>
                </v-col>
              </v-row>
              <v-row>
                <v-col cols="12" md="12">
                  <v-text-field
                    v-model="lastName"
                    label="Last name"
                    :error-messages="lastNameErrors"
                    @input="$v.lastName.$touch()"
                    @blur="$v.lastName.$touch()"
                    required
                  ></v-text-field>
                </v-col>
              </v-row>
              <v-row>
                <v-col cols="12" md="12">
                  <v-text-field
                    v-model="email"
                    label="Email"
                    :error-messages="emailErrors"
                    @input="$v.email.$touch()"
                    @blur="$v.email.$touch()"
                    required
                  ></v-text-field>
                </v-col>
              </v-row>
              <v-row>
                <v-col cols="12" md="12">
                  <v-text-field
                    v-model="login"
                    label="Username"
                    :error-messages="loginErrors"
                    @input="$v.login.$touch()"
                    @blur="$v.login.$touch()"
                    required
                  ></v-text-field>
                </v-col>
              </v-row>
              <v-row>
                <v-col cols="12" md="6">
                  <v-text-field
                    v-model="password"
                    label=" Password"
                    :type="showPassword ? 'text' : 'password'"
                    :error-messages="passwordErrors"
                    @input="$v.password.$touch()"
                    @blur="$v.password.$touch()"
                    prepend-icon="mdi-lock"
                    :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
                    @click:append="showPassword = !showPassword"
                    required
                  ></v-text-field>
                </v-col>
                <v-col cols="12" md="6">
                  <v-text-field
                    v-model="confirmPassword"
                    label="Retype password"
                    :type="showPassword ? 'text' : 'password'"
                    :error-messages="confirmPasswordErrors"
                    @input="$v.confirmPassword.$touch()"
                    @blur="$v.confirmPassword.$touch()"
                    prepend-icon="mdi-lock"
                    :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
                    @click:append="showPassword = !showPassword"
                    required
                  ></v-text-field>
                </v-col>
              </v-row>

              <v-row class="button">
                <v-col cols="12" md="12">
                  <v-btn
                    @click="register"
                    block
                    color="primary"
                    elevation="1"
                    outlined
                    x-large
                    >Register User and Organization</v-btn
                  >
                </v-col>
              </v-row>
            </v-container>
          </v-form>
        </v-responsive>
      </v-card>
      <v-card class="pa-12 float-left ma-10" min-width="500px">
        <v-responsive :aspect-ratio="1 / 1">
          <v-form ref="form">
            <v-container>
              <v-card-title class="justify-center text-h2 mb-4"
                >Organization</v-card-title
              >
              <v-row>
                <v-col cols="12" md="12">
                  <v-text-field
                    label="Name"
                    v-model="orgName"
                    :error-messages="orgNameErrors"
                    @input="$v.orgName.$touch()"
                    @blur="$v.orgName.$touch()"
                    required
                  ></v-text-field>
                </v-col>
              </v-row>
              <v-row>
                <v-col cols="12" md="12">
                  <v-text-field
                    label="NIP"
                    v-model="nip"
                    :error-messages="nipErrors"
                    @input="$v.nip.$touch()"
                    @blur="$v.nip.$touch()"
                    required
                  ></v-text-field>
                </v-col>
              </v-row>
              <v-row>
                <v-col cols="12" md="8">
                  <v-text-field
                    label="Street"
                    v-model="street"
                    :error-messages="streetErrors"
                    @input="$v.street.$touch()"
                    @blur="$v.street.$touch()"
                    required
                  ></v-text-field>
                </v-col>

                <v-col cols="12" md="4">
                  <v-text-field
                    label="Nr."
                    v-model="streetNum"
                    :error-messages="streetNumErrors"
                    @input="$v.streetNum.$touch()"
                    @blur="$v.streetNum.$touch()"
                    required
                  ></v-text-field>
                </v-col>
              </v-row>
              <v-row>
                <v-col cols="12" md="8">
                  <v-text-field
                    label="Citi"
                    v-model="citi"
                    :error-messages="citiErrors"
                    @input="$v.citi.$touch()"
                    @blur="$v.citi.$touch()"
                    required
                  ></v-text-field>
                </v-col>

                <v-col cols="12" md="4">
                  <v-text-field
                    label="Postal"
                    v-model="postal"
                    :error-messages="postalErrors"
                    @input="$v.postal.$touch()"
                    @blur="$v.postal.$touch()"
                    required
                  ></v-text-field>
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
import { validationMixin } from "vuelidate";
import {
  required,
  minLength,
  email,
  alpha,
  alphaNum,
  sameAs,
  numeric,
  maxLength
} from "vuelidate/lib/validators";

export default {
  mixins: [validationMixin],
  validations: {
    name: { required, minLength: minLength(4) },
    lastName: { required, minLength: minLength(4) },
    email: { required, email },
    login: { required, alphaNum },
    password: { required, minLength: minLength(6) },
    confirmPassword: { sameAsPassword: sameAs("password") },
    orgName: { required },
    nip: {
      required,
      numeric,
      minLength: minLength(10),
      maxLength: maxLength(10)
    },
    citi: { required, alpha },
    postal: {
      required,
      numeric,
      minLength: minLength(5),
      maxLength: maxLength(5)
    },
    street: { required, alpha },
    streetNum: { required }
  },
  computed: {
    orgNameErrors() {
      const errors = [];
      if (!this.$v.orgName.$dirty) return errors;
      !this.$v.orgName.required && errors.push("Name is required.");
      return errors;
    },
    nipErrors() {
      const errors = [];
      if (!this.$v.nip.$dirty) return errors;
      !this.$v.nip.numeric &&
        errors.push("NIP name should contain only numbers");
      !this.$v.nip.minLength && errors.push("NIP must be 10 characters long.");
      !this.$v.nip.maxLength && errors.push("NIP must be 10 characters long.");
      !this.$v.nip.required && errors.push("NIP is required.");
      return errors;
    },
    postalErrors() {
      const errors = [];
      if (!this.$v.postal.$dirty) return errors;
      !this.$v.postal.numeric &&
        errors.push("Postal name should contain only numbers");
      !this.$v.postal.minLength &&
        errors.push("Postal must be 5 characters long.");
      !this.$v.postal.maxLength &&
        errors.push("Postal must be 5 characters long.");
      !this.$v.postal.required && errors.push("Postal is required.");
      return errors;
    },
    citiErrors() {
      const errors = [];
      if (!this.$v.citi.$dirty) return errors;
      !this.$v.citi.alpha &&
        errors.push("Citi name should contain only alphabet characters");
      !this.$v.citi.required && errors.push("Citi is required.");
      return errors;
    },
    streetErrors() {
      const errors = [];
      if (!this.$v.street.$dirty) return errors;
      !this.$v.street.alpha &&
        errors.push("Street name should contain only alphabet characters");
      !this.$v.street.required && errors.push("Street is required.");
      return errors;
    },
    streetNumErrors() {
      const errors = [];
      if (!this.$v.streetNum.$dirty) return errors;
      !this.$v.streetNum.required && errors.push("Number is required.");
      return errors;
    },
    nameErrors() {
      const errors = [];
      if (!this.$v.name.$dirty) return errors;
      !this.$v.name.minLength &&
        errors.push("Name must be at least 4 characters long.");
      !this.$v.name.required && errors.push("Name is required.");
      return errors;
    },
    lastNameErrors() {
      const errors = [];
      if (!this.$v.lastName.$dirty) return errors;
      !this.$v.lastName.minLength &&
        errors.push("Last name must be at least 4 characters long.");
      !this.$v.lastName.required && errors.push("Last name is required.");
      return errors;
    },
    emailErrors() {
      const errors = [];
      if (!this.$v.email.$dirty) return errors;
      !this.$v.email.email && errors.push("Must be valid e-mail");
      !this.$v.email.required && errors.push("E-mail is required");
      return errors;
    },
    loginErrors() {
      const errors = [];
      if (!this.$v.login.$dirty) return errors;
      !this.$v.login.alphaNum &&
        errors.push("Login shoud not contain special characters.");
      !this.$v.login.required && errors.push("Login is required.");
      return errors;
    },
    passwordErrors() {
      const errors = [];
      if (!this.$v.password.$dirty) return errors;
      !this.$v.password.minLength &&
        errors.push("Password must be at least 6 characters long");
      !this.$v.password.required && errors.push("Password is required");
      return errors;
    },
    confirmPasswordErrors() {
      const errors = [];
      if (!this.$v.confirmPassword.$dirty) return errors;
      !this.$v.confirmPassword.sameAsPassword &&
        errors.push("Password must be at least 6 characters long");
      return errors;
    }
  },
  head() {
    return {
      title: "Login page"
    };
  },
  data: () => ({
    alert: false,
    alertData: {},
    showPassword: false,
    name: "",
    lastName: "",
    email: "",
    login: "",
    password: "",
    confirmPassword: "",
    orgName: "",
    nip: "",
    street: "",
    streetNum: "",
    citi: "",
    postal: "",
    rules: {
      required: v => !!v || "Fields required"
    }
  }),
  methods: {
    async register() {
      this.$v.$touch();
      if (!this.$v.$invalid) {
        const organization = {
          name: this.orgName,
          nip: this.nip,
          city: this.citi,
          street: this.street,
          street_num: this.streetNum,
          postal_code: this.postal
        };
        const data = {
          username: this.login,
          password: this.password,
          email: this.email,
          first_name: this.name,
          last_name: this.lastName,
          organization: organization
        };

        const res = await this.$axios.post("/register", data).catch(error => {
          if (error.response) {
            console.log(error.response);
            try {
              this.alertData = [
                error.response.data["username"][0],
                error.response.data["email"][0],
                error.response.data["organization"]["nip"][0],
                error.response.data["organization"]["name"][0]
              ];
              this.alertData = this.alertData.filter(function(element) {
                return element !== undefined;
              });
            } catch (e) {
              console.log(e);
            }

            this.alert = true;
            setTimeout(() => (this.alert = false), 3000);
            console.log(this.alertData);
          }
        });
        this.$router.push("/");
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

.button {
  width: 100%;
}
</style>

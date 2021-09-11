<template>
  <div>
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

    <v-form ref="form">
      <v-container>
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
              >Register</v-btn
            >
          </v-col>
        </v-row>
      </v-container>
    </v-form>
  </div>
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
    confirmPassword: { sameAsPassword: sameAs("password") }
  },
  computed: {
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
  props: {
    url: ""
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
    confirmPassword: ""
  }),
  methods: {
    async register() {
      this.$v.$touch();
      if (!this.$v.$invalid) {
        const data = {
          username: this.login,
          password: this.password,
          email: this.email,
          first_name: this.name,
          last_name: this.lastName
        };

        const res = await this.$axios
          .post(this.url, data)
          .then(res => {
            this.$emit("close-dialog");
            this.$store.dispatch("driver/getDriver");
          })
          .catch(error => {
            if (error.response) {
              try {
                let alertData = [];
                JSON.stringify(error.response.data, (key, value) => {
                  if (key === "0") alertData.push(value);
                  return value;
                });
                this.alertData = alertData;
              } catch (e) {}
              this.alert = true;
              setTimeout(() => (this.alert = false), 5000);
            }
          })
          .then();
      }
    }
  }
};
</script>

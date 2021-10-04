import Vue from "vue";
import * as VeeValidate from "vee-validate";
import { extend } from "vee-validate";
import {
  required,
  between,
  numeric,
  alpha_num,
  max_value
} from "vee-validate/dist/rules";

Vue.use(VeeValidate, {});

extend("required", {
  ...required,
  message: "This field is required"
});

extend("modelyear", {
  ...between,
  message: "Provide valid model year"
});

extend("numeric", {
  ...numeric,
  message: "This field must be numeric"
});

extend("alpha_num", {
  ...alpha_num,
  message: "This field cannot contain special characters"
});

extend("max_value", {
  ...max_value,
  message: "Engine size cannot be greater than 50"
});

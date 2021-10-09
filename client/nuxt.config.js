import colors from "vuetify/es5/util/colors";

export default {
  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    titleTemplate: "%s - Tracky",
    title: "Tracky",
    htmlAttrs: {
      lang: "en"
    },
    meta: [
      { charset: "utf-8" },
      { name: "viewport", content: "width=device-width, initial-scale=1" },
      { hid: "description", name: "description", content: "" },
      { name: "format-detection", content: "telephone=no" }
    ],
    link: [{ rel: "icon", type: "image/x-icon", href: "/favicon.ico" }]
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: ["@fortawesome/fontawesome-free/css/all.css"],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [
    { src: "~plugins/leaflet.js", ssr: false },
    { src: "~/plugins/vee-validate.js", ssr: true },
    { src: "~/plugins/vue-svg-gauge.js", ssr: false },
    { src: "~/plugins/v-calendar.js", ssr: false }
  ],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    // https://go.nuxtjs.dev/vuetify
    "@nuxtjs/vuetify"
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/axios
    "@nuxtjs/axios",
    "@nuxtjs/auth-next"
  ],

  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  axios: {
    baseURL: "http://localhost:8000/api"
  },

  auth: {
    strategies: {
      local: {
        scheme: "refresh",
        localStorage: {
          prefix: "auth."
        },
        token: {
          prefix: "access.",
          property: "access",
          maxAge: 86400,
          type: "Bearer"
        },
        refreshToken: {
          prefix: "refresh.",
          property: "refresh",
          data: "refresh",
          maxAge: 60 * 60 * 24 * 15
        },
        user: {
          property: "",
          autoFetch: true
        },
        endpoints: {
          login: { url: "/token", method: "post" },
          refresh: { url: "/token/refresh", method: "post" },
          user: { url: "/profile", method: "get" },
          logout: { url: "/logout", method: "post" }
        }
      }
    }
  },

  // Vuetify module configuration: https://go.nuxtjs.dev/config-vuetify
  vuetify: {
    customVariables: ["~/assets/variables.scss"],
    theme: {
      dark: false,
      themes: {
        dark: {
          primary: colors.blue.darken2,
          accent: colors.grey.darken3,
          secondary: colors.amber.darken3,
          info: colors.teal.lighten1,
          warning: colors.amber.base,
          error: colors.deepOrange.accent4,
          success: colors.green.accent3
        }
      }
    }
  },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {
    transpile: ["vee-validate"]
  }
};

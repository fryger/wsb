<template>
  <div class="organization ma-auto">
    <v-container fluid>
      <v-row class="pa-16">
        <v-col md="4">
          <v-hover v-slot="{ hover }">
            <v-card color="#f8f8f8" height="100%" class="org-card">
              <v-img :src="logo"></v-img>

              <v-list-item class="px-10 pt-10">
                <v-list-item-content>
                  <v-list-item-title class="text-h4 font-weight-bold pb-4">
                    Company information:
                  </v-list-item-title>
                  <v-list-item-title class="text-h5 ">
                    {{ organization }}
                  </v-list-item-title>
                  <v-list-item-title class="text-h5">
                    NIP: {{ nip }}
                  </v-list-item-title>
                  <v-list-item-title class="text-h5">
                    {{ street }} {{ streetNum }}, {{ postal }} {{ city }}
                  </v-list-item-title>
                </v-list-item-content>
              </v-list-item>
              <v-btn
                class="mx-2 btn-edit"
                fab
                dark
                small
                color="secondary"
                v-show="hover"
                v-if="access"
                @click="dialog = true"
              >
                <v-icon dark>
                  mdi-pencil-outline
                </v-icon>
              </v-btn>
            </v-card>
          </v-hover>
        </v-col>
        <v-col align="center" md="8">
          <v-card color="#f8f8f8">
            <div id="mapid" style="height: 50vh"></div>
          </v-card>
        </v-col>
      </v-row>
      <v-row class="px-16">
        <v-col>
          <div class="text-center"></div>
        </v-col>
        <v-col>
          <v-dialog
            transition="fade-transition"
            max-width="600"
            style="z-index:9999;"
            v-model="dialog"
          >
            <template>
              <v-card>
                <v-card-title>
                  <span class="text-5">Update company information</span>
                </v-card-title>
                <v-form>
                  <v-card-text>
                    <v-container>
                      <v-row>
                        <v-col>
                          <v-text-field></v-text-field>
                        </v-col>
                        <v-col cols="12" sm="12">
                          <v-file-input
                            chips
                            truncate-length="50"
                            accept="image/*"
                          ></v-file-input>
                        </v-col>
                      </v-row>
                    </v-container>
                  </v-card-text>
                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="blue darken-1" text @click="dialog = false">
                      Close
                    </v-btn>
                    <v-btn color="blue darken-1" text>
                      Save
                    </v-btn>
                  </v-card-actions>
                </v-form>
              </v-card>
            </template>
          </v-dialog></v-col
        >
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {
  head() {
    return {
      link: [
        {
          rel: "stylesheet",
          href: "https://unpkg.com/leaflet@1.6.0/dist/leaflet.css"
        }
      ]
    };
  },
  data: () => ({
    dialog: false,
    access: false,
    organization: "Organization",
    nip: "1112233444",
    city: "City",
    street: "Street",
    streetNum: "00",
    postal: "11222",
    logo: "https://via.placeholder.com/600x200",
    lat: "",
    lon: ""
  }),
  methods: {
    async getOrganization() {
      await this.$axios.get("/organization").then(res => {
        this.organization = res.data[0].name;
        this.nip = res.data[0].nip;
        this.city = res.data[0].city;
        this.street = res.data[0].street;
        this.streetNum = res.data[0].street_num;
        this.postal = res.data[0].postal_code;
        this.logo = res.data[0].logo;

        this.getCords(
          [this.street, this.streetNum, this.city, this.postal].join(" ")
        );
        this.form();
      });
    },
    async getCords(adress) {
      await this.$axios
        .get(
          `https://nominatim.openstreetmap.org/search?format=json&q=${adress}`
        )
        .then(res => {
          this.lat = res.data[0].lat;
          this.lon = res.data[0].lon;
          this.map();
        });
    },
    map() {
      var mymap = L.map("mapid", {
        zoom: 15
      }).setView([this.lat, this.lon]);

      var marker = L.marker([this.lat, this.lon]).addTo(mymap);

      L.tileLayer(
        "https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}",
        {
          attribution:
            'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
          maxZoom: 18,
          id: "mapbox/streets-v11",
          tileSize: 512,
          zoomOffset: -1,
          accessToken:
            "pk.eyJ1IjoiZnJ5ZzNyIiwiYSI6ImNrdDkxNmwyZjExNWoycHBjY2JoaGRpOHEifQ.sPeP6CgU6f918oFMa2puog"
        }
      ).addTo(mymap);
    }
  },
  mounted() {
    this.getOrganization();
    this.access = this.$auth.$state.user[0].organization_permission == "9";
  },
  created() {}
};
</script>

<style scoped>
.org-card {
  position: relative;
}
.btn-edit {
  position: absolute;
  right: -25px;
  top: -15px;
  z-index: 1;
}
</style>

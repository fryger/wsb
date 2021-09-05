<template>
  <div class="organization ma-auto">
    <v-container fluid>
      <v-row class="pa-16">
        <v-col md="4">
          <v-card color="#f8f8f8" height="100%">
            <v-img
              src="https://retencja.pl/wp-content/themes/retencja/dist/images/retencja-logo.svg"
            ></v-img>

            <v-list-item class="pa-16">
              <v-list-item-content>
                <v-list-item-title class="text-h4 font-weight-bold ">
                  Retencja
                </v-list-item-title>
                <v-list-item-title class="text-h6">
                  NIP: 321456777
                </v-list-item-title>
                <v-list-item-title class="text-h6">
                  Łąkowa 41, 84-240 Reda
                </v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-card>
        </v-col>

        <v-col align="center" md="8">
          <v-card color="#f8f8f8">
            <div id="map-wrap" style="height: 50vh">
              <no-ssr>
                <l-map :zoom="13" :center="[55.9464418, 8.1277591]">
                  <l-tile-layer
                    url="http://{s}.tile.osm.org/{z}/{x}/{y}.png"
                  ></l-tile-layer>
                  <l-marker :lat-lng="[55.9464418, 8.1277591]"></l-marker>
                </l-map>
              </no-ssr>
            </div>
          </v-card>
        </v-col>
      </v-row>
      <v-spacer></v-spacer
    ></v-container>
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
  }
};
</script>

<style scoped></style>

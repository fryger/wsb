<template>
  <v-container fluid>
    <v-row class="my-1">
      <v-col cols="12" xl="8">
        <v-card elevation="2" color="#55BAB4">
          <v-card-text>
            <v-carousel
              :continuous="false"
              :cycle="cycle"
              hide-delimiter-background
              delimiter-icon="mdi-minus"
              height="auto"
            >
              <v-carousel-item v-for="(slide, i) in slides" :key="i" eager>
                <v-img :src="slide" contain eager></v-img>
              </v-carousel-item>
            </v-carousel>
          </v-card-text>
        </v-card>
      </v-col>
      <v-col cols="12" xl="3">
        <v-card><v-card-title>ASD</v-card-title></v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      cycle: false,
      slides: [
        "https://ireland.apollo.olxcdn.com/v1/files/eyJmbiI6Ijk4cmc1NWszb2VsdTMtT1RPTU9UT1BMIiwidyI6W3siZm4iOiJ3ZzRnbnFwNnkxZi1PVE9NT1RPUEwiLCJzIjoiMTYiLCJwIjoiMTAsLTEwIiwiYSI6IjAifV19.paKqiX0StQvEOwmN05mUOYzxeUIofTkKeoZdBiB8-oU/image;s=1080x720",
        "https://ireland.apollo.olxcdn.com/v1/files/eyJmbiI6InhidTA0Y3BubnpmNzEtT1RPTU9UT1BMIiwidyI6W3siZm4iOiJ3ZzRnbnFwNnkxZi1PVE9NT1RPUEwiLCJzIjoiMTYiLCJwIjoiMTAsLTEwIiwiYSI6IjAifV19.qFQX8CXi1r_HAVI6Gga_P5Wa2wSRXdM8AaJh7yNTN_w/image;s=1080x720",
        "https://ireland.apollo.olxcdn.com/v1/files/eyJmbiI6InhidTA0Y3BubnpmNzEtT1RPTU9UT1BMIiwidyI6W3siZm4iOiJ3ZzRnbnFwNnkxZi1PVE9NT1RPUEwiLCJzIjoiMTYiLCJwIjoiMTAsLTEwIiwiYSI6IjAifV19.qFQX8CXi1r_HAVI6Gga_P5Wa2wSRXdM8AaJh7yNTN_w/image;s=1080x720",
        "https://ireland.apollo.olxcdn.com/v1/files/eyJmbiI6ImE4YjVsNHJhanltNzMtT1RPTU9UT1BMIiwidyI6W3siZm4iOiJ3ZzRnbnFwNnkxZi1PVE9NT1RPUEwiLCJzIjoiMTYiLCJwIjoiMTAsLTEwIiwiYSI6IjAifV19.vAvTxZ1MjSW0HZkAzr0zOQvTm-nNsuE_WKJgMrphIRA/image;s=1080x720",
        "https://ireland.apollo.olxcdn.com/v1/files/eyJmbiI6IjU1anlpenI2ZGNrazMtT1RPTU9UT1BMIiwidyI6W3siZm4iOiJ3ZzRnbnFwNnkxZi1PVE9NT1RPUEwiLCJzIjoiMTYiLCJwIjoiMTAsLTEwIiwiYSI6IjAifV19.Ufti8NEEI1pIqhUcsHJRsvP5tNwNVsKYn6dhhppXyyE/image;s=1080x720"
      ]
    };
  }
};
</script>

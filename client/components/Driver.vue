<template>
  <!--<v-col cols="12" lg="4" md="6" sm="12" class="mt-2">-->
  <v-card
    :class="themeDark ? '' : ' ma-2'"
    :elevation="themeDark ? '0' : '1'"
    :dark="themeDark"
    :color="themeDark ? '#2d3748' : ''"
  >
    <v-card-text class="text-center">
      <v-row align="center" justify="center">
        <v-col cols="2">
          <v-avatar size="60">
            <v-img class="elevation-6" alt="" :src="picture"></v-img>
          </v-avatar>
        </v-col>
        <v-col cols="4">
          <span class="ml-2 text-subtitle-2 font-weight-black"
            >{{ name }} {{ lastName }}
          </span>
        </v-col>
        <v-col cols="6">
          <v-chip
            v-if="permission == 9"
            color="orange"
            label
            text-color="white"
            class="ml-6"
          >
            <v-icon left>
              fa-crown
            </v-icon>
            Company Admin
          </v-chip>
          <v-chip v-else color="cyan" label text-color="white" class="ml-6">
            <v-icon left>
              fa-car
            </v-icon>
            User
          </v-chip>
        </v-col>
      </v-row>
    </v-card-text>
  </v-card>
  <!--  </v-col>-->
</template>

<script>
export default {
  props: {
    themeDark: {
      default: false
    },
    name: {
      default: "John"
    },
    lastName: {
      default: "Smith"
    },
    nick: {
      default: "jsmith"
    },
    email: {
      default: "john@example.com"
    },
    permission: {
      default: 0
    },
    picture: {
      default: require("../assets/driver_profile.svg")
    }
  }
};
</script>

<style scoped></style>

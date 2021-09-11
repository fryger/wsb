<template>
  <v-col cols="12" lg="4" md="6" sm="12" class="mt-2">
    <v-card>
      <v-row>
        <v-col>
          <v-card-title class="ml-2 pa-0">
            <v-list-item-avatar height="60" width="60" color="grey darken-3">
              <v-img class="elevation-6" alt="" :src="picture"></v-img>
            </v-list-item-avatar>
            <v-list-item-content>
              <v-list-item-title class="headline"
                >{{ name }} {{ lastName }}</v-list-item-title
              >
              <v-list-item-subtitle class="caption">{{
                nick
              }}</v-list-item-subtitle>
            </v-list-item-content>
          </v-card-title>
        </v-col>
      </v-row>
    </v-card>
  </v-col>
</template>

<script>
export default {
  props: {
    name: {
      default: "John"
    },
    lastName: {
      default: "Smith"
    },
    nick: {
      default: "jsmith"
    },
    picture: {
      default:
        "https://avataaars.io/?avatarStyle=Transparent&topType=ShortHairShortCurly&accessoriesType=Prescription02&hairColor=Black&facialHairType=Blank&clotheType=Hoodie&clotheColor=White&eyeType=Default&eyebrowType=DefaultNatural&mouthType=Default&skinColor=Light"
    }
  }
};
</script>

<style scoped></style>

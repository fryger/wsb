<template>
  <v-container>
    <v-row justify="center">
      <v-expansion-panels popout>
        <v-expansion-panel class="mt-2" v-for="(item, i) in 50" :key="i">
          <v-expansion-panel-header>
            <template v-slot:default="{ open }">
              <v-row no-gutters>
                <v-col cols="1">
                  <span class="font-weight-bold text-subtitle-1">
                    {{ title }}</span
                  >
                  <v-divider></v-divider>
                </v-col>
                <v-col cols="2" class="text--secondary">
                  <v-fade-transition leave-absolute>
                    <span v-if="open" key="0"> </span>
                    <span v-else key="1">
                      <v-icon>mdi-earth</v-icon> {{ street }}, {{ city }}
                    </span>
                  </v-fade-transition>
                </v-col>
                <v-col cols="2" class="text--secondary">
                  <v-fade-transition leave-absolute>
                    <span v-if="open" key="0"> </span>
                    <span v-else key="1">
                      <v-icon>mdi-calendar</v-icon>{{ date }}
                    </span>
                  </v-fade-transition>
                </v-col>
              </v-row>
            </template>
          </v-expansion-panel-header>
          <v-expansion-panel-content>
            <v-row>
              <v-col cols="8">
                <v-card elevation="12" class="mx-auto">
                  <v-carousel v-model="model">
                    <v-carousel-item src="https://i.imgur.com/iJG7nFY.jpg">
                    </v-carousel-item>
                    <v-carousel-item
                      src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Car_crash_1.jpg/1024px-Car_crash_1.jpg"
                    ></v-carousel-item>
                  </v-carousel>
                </v-card>
              </v-col>
              <v-col cols="4">
                <v-card elevation="6" class="mx-auto" style="height:100%">
                  <v-card-text class="text-subtitle-1 font-weight-medium">
                    <p>
                      <v-icon>mdi-calendar</v-icon> When happend: {{ date }}
                    </p>
                    <p>
                      <v-icon>mdi-earth</v-icon> Where happend: {{ street }},
                      {{ city }}
                    </p>
                    <p><v-icon>mdi-account</v-icon> Driver: {{ driver }}</p>
                    <p>
                      <v-icon>fa-user-friends</v-icon> Whose fault: {{ fault }}
                    </p>
                    <p><v-icon>mdi-wrench</v-icon> Repaired: {{ repaired }}</p>
                    <p><v-icon>mdi-tools</v-icon> Repaired where: {{ shop }}</p>
                    <p>
                      <v-icon>mdi-shield-car</v-icon> Insurance number:
                      {{ insurance }}
                    </p>
                    <p>
                      <v-icon>mdi-image-broken-variant</v-icon> Damages:
                      {{ damages }}
                    </p>
                    <p>
                      <v-icon>mdi-pencil</v-icon> Description:
                      {{ description }}
                    </p>
                  </v-card-text>
                </v-card>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-chip class="ma-2" outlined color="teal">
                  <v-avatar left>
                    <v-icon>fa-file-word</v-icon>
                  </v-avatar>
                  Declaration of guilt
                </v-chip>
                <v-chip class="ma-2" outlined color="orange">
                  <v-avatar left>
                    <v-icon>fa-file-word</v-icon>
                  </v-avatar>
                  Police note
                </v-chip>
                <v-chip class="ma-2" outlined color="brown">
                  <v-avatar left>
                    <v-icon>fa-file-pdf</v-icon>
                  </v-avatar>
                  Insurance company statment
                </v-chip>
              </v-col>
            </v-row>
          </v-expansion-panel-content>
        </v-expansion-panel>
      </v-expansion-panels>
    </v-row>
  </v-container>
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
  data() {
    return {
      title: "Car accident",
      date: new Date().toDateString(),
      street: "Głowackiego 28",
      city: "Gdańsk",
      driver: "John Smith",
      fault: "Driver",
      repaired: "Yes",
      shop: "Auto-Awis Sp. z o.o.",
      insurance: "2002213/123/233",
      damages: "Dented driver side rear fender, broken reflective lamp",
      description:
        "On monday 12/04/2000 black Ford Mondeo hit and run fleet Skoda Fabia. Car was repaired next day.",
      model: 0
    };
  }
};
</script>

<style scoped></style>

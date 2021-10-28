<template>
  <v-container>
    <v-row justify="center">
      <v-expansion-panels popout>
        <v-expansion-panel class="mt-2" v-for="(item, i) in 5" :key="i">
          <v-expansion-panel-header>
            <template v-slot:default="{ open }">
              <v-row no-gutters>
                <v-col cols="1">
                  {{ title }}
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
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim
            ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
            aliquip ex ea commodo consequat.
          </v-expansion-panel-content>
        </v-expansion-panel>
      </v-expansion-panels>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      title: "Car accident",
      date: new Date().toDateString(),
      street: "Głowackiego",
      city: "Gdańsk"
    };
  }
};
</script>

<style scoped></style>

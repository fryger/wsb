<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="12" lg="4" md="7" sm="12">
        <div class="text-h4">Add new reminder</div>
        <v-text-field label="Name"></v-text-field>
        <v-textarea label="Description" rows="3" auto-grow></v-textarea>
        <v-row>
          <v-menu
            dark
            ref="menu"
            v-model="menu2"
            :close-on-content-click="false"
            :nudge-right="40"
            :return-value.sync="time"
            transition="scale-transition"
            offset-y
            max-width="290px"
            min-width="290px"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-text-field
                class="pa-3"
                v-model="time"
                label="Time"
                readonly
                v-bind="attrs"
                v-on="on"
              ></v-text-field>
            </template>
            <v-time-picker
              format="24hr"
              v-if="menu2"
              v-model="time"
              full-width
              @click:minute="$refs.menu.save(time)"
            ></v-time-picker>
          </v-menu>
        </v-row>
        <v-row>
          <v-col>
            <v-date-picker
              class="ma-4"
              color="#363636"
              v-model="picker"
              landscape
            ></v-date-picker
          ></v-col>
        </v-row>
        <v-row>
          <v-col><v-checkbox label="SMS" color="#55bab4"></v-checkbox></v-col>
          <v-col><v-checkbox label="Email" color="#55bab4"></v-checkbox></v-col>
        </v-row>
        <v-switch label="Repetetive" color="#55bab4"></v-switch>
        <v-btn block outlined color="#55bab4" dark
          ><span class="text-body-1 font-weight-bold">SET</span
          ><v-icon class="pl-2">mdi-alarm</v-icon></v-btn
        >
      </v-col>
      <v-col cols="12" lg="8" md="5" sm="12" class="pa-12">
        <v-row>
          <v-card class="ma-2" width="300" v-for="index in 7" :key="index">
            <v-btn
              depressed
              text
              absolute
              color="red"
              style="height:13px; left:236px;"
              ><v-icon x-small>fa-times</v-icon></v-btn
            >

            <v-card-title>Change oil</v-card-title>
            <v-card-subtitle>{{ new Date() }}</v-card-subtitle>
            <v-card-text>
              Castrol 5w-30, Filtron filters
            </v-card-text>
            <span class="ma-4">Notifications</span>
            <v-divider></v-divider>
            <v-card-actions class="mt-1">
              <v-chip class="mr-2" label color="#55bab4" outlined>
                <v-icon left>
                  fa-sms
                </v-icon>
                SMS
              </v-chip>
              <v-chip class="mr-2" label color="#55bab4" outlined>
                <v-icon left>
                  fa-envelope
                </v-icon>
                EMAIL
              </v-chip>
              <v-chip class="mr-2" label color="#55bab4" outlined>
                <v-icon left>
                  fa-redo-alt
                </v-icon>
                REPETETIVE
              </v-chip>
            </v-card-actions>
          </v-card>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      picker: new Date().toISOString().substr(0, 7),
      time: null,
      menu2: false,
      modal2: false
    };
  }
};
</script>

<style scoped></style>

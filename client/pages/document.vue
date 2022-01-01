<template>
  <v-container>
    <v-row>
      <v-icon slot="prependIcon" class="pr-3" large>mdi-magnify</v-icon>
      <v-text-field label="Search" height="50" v-model="search"></v-text-field>
    </v-row>
    <v-row>
      <v-btn
        @click="dialog = true"
        color="green"
        elevation="1"
        class="ma-2"
        rounded
        outlined
        ><v-icon left dark>mdi-plus</v-icon> Add document
      </v-btn>
    </v-row>
    <v-row class=" mt-12">
      <v-layout child-flex>
        <v-data-table
          :headers="headers"
          :items="cars"
          class="elevation-1"
          hide-default-footer
          width="100%"
          disable-pagination
          @click:row="handleClick"
        >
          <template v-slot:[`item.status`]="{ item }">
            <v-chip :color="getColor(item.status)" dark>
              {{ item.status }}
            </v-chip>
          </template>
          <template v-slot:[`item.fuel`]="{ item }">
            <v-icon left :color="fuelColor(item.fuel)">
              {{ fuelIcon(item.fuel) }}
            </v-icon>
            {{ item.fuel }}
          </template>
          <template v-slot:[`item.mileage`]="{ item }">
            {{ numberWithSpaces(item.mileage) }}
          </template>
          <template v-slot:[`item.driver`]="{ item }">
            {{ getDriverById(item.driver) }}
          </template>
        </v-data-table>
      </v-layout>
    </v-row>
    <!-- Add car form -->
    <v-navigation-drawer
      v-model="dialog"
      absolute
      right
      width="500"
      style="max-height:100vh; position: fixed;"
    >
      <AddCarForm v-on:close-dialog="dialog = false" />
    </v-navigation-drawer>
  </v-container>
</template>
</template>

<script>
export default {
    data() {
    return {
      dialog: false,
      search: ""
      }}
};
</script>

<style scoped></style>

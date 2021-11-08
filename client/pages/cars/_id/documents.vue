<template>
  <v-container>
    <v-row class="mb-6">
      <v-icon slot="prependIcon" class="pr-3" large>mdi-magnify</v-icon>
      <v-text-field label="Search" height="50" v-model="search"></v-text-field>
    </v-row>
    <v-data-table
      hide-default-footer
      :headers="headers"
      :items="docs"
      :items-per-page="5"
      class="elevation-1"
    >
      <template v-slot:item.extension="{ item }">
        <v-icon>{{ extIcon(item.extension) }}</v-icon>
      </template>
      <template v-slot:item.actions="{ item }">
        <v-icon>
          mdi-delete
        </v-icon>
      </template>
    </v-data-table>
  </v-container>
</template>

<script>
export default {
  methods: {
    extIcon(name) {
      return name == "pdf" ? "fa-file-pdf" : "fa-file";
    }
  },
  data() {
    return {
      icon: "fa-file-pdf",
      headers: [
        { text: "Type", value: "extension", width: "5%" },
        { text: "Name", value: "name" },
        { text: "Description", value: "description" },
        { text: "Created", value: "date" },
        { text: "Action", value: "actions", sortable: false, width: "5%" }
      ],
      docs: [
        {
          extension: "pdf",
          name: "Vehicle identification card",
          description: "Car card",
          date: new Date()
            .toJSON()
            .slice(0, 10)
            .replace(/-/g, "/")
        }
      ]
    };
  }
};
</script>

<style scoped></style>

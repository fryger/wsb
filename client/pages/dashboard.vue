<template>
  <v-container>
    <p class="text-h1 mb-12">Dashboard</p>
    <v-row>
      <v-col cols="12" lg="3">
        <v-card height="100%">
          <v-card-title>Cars status </v-card-title>
          <v-divider class="mx-6"></v-divider>
          <v-card-text>
            <apexchart
              ref="chart"
              type="polarArea"
              :options="options"
              :series="options.series"
            ></apexchart>
          </v-card-text>
        </v-card>
      </v-col>
      <v-col cols="12" lg="6">
        <v-card height="300px">
          <v-card-title>Overall mileage growth </v-card-title>
          <v-card-subtitle>
            <v-select
              style="width:80px;"
              :items="['Month', 'Year']"
              label="By"
            ></v-select>
          </v-card-subtitle>
          <v-divider class="mx-6"></v-divider>
          <v-card-text>
            <apexchart
              height="100%"
              ref="char"
              type="area"
              :options="option"
              :series="option.series"
            ></apexchart>
          </v-card-text>
        </v-card>
      </v-col>
      <v-col cols="12" lg="3">
        <v-card height="100%">
          <v-card-title>Cars count </v-card-title>
          <v-divider class="mx-6"></v-divider>
          <v-card-text class="text-center my-12">
            <span class="text-h1 ">5</span>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12" lg="3">
        <v-card height="100%">
          <v-card-title>Cars production year</v-card-title>
          <v-divider class="mx-6"></v-divider>
          <v-card-text>
            <apexchart
              ref="chart"
              type="donut"
              :options="options2"
              :series="options2.series"
            ></apexchart>
          </v-card-text>
        </v-card>
      </v-col>
      <v-col cols="12" lg="3">
        <v-card min-height="300px" height="100%">
          <v-card-title>Drivers count </v-card-title>
          <v-divider class="mx-6"></v-divider>
          <v-card-text class="text-center my-12">
            <span class="text-h1 ">4</span>
          </v-card-text>
        </v-card>
      </v-col>
      <v-col cols="12" lg="6">
        <v-card min-height="300px" height="100%">
          <v-card-title>Fuel cost</v-card-title>
          <v-divider class="mx-6"></v-divider>
          <v-card-text class="text-center my-12">
            <v-row align="center" justify="center">
              <v-col cols="12" lg="3">
                <p>
                  <v-icon class="mb-4" color="green" size="60"
                    >mdi-gas-station</v-icon
                  >
                  <span class="text-h4">95</span>
                </p>
                <p class="text-h3">
                  {{ fuel.petrol95 }}
                </p>
              </v-col>
              <v-divider vertical></v-divider>
              <v-col cols="12" lg="3">
                <p>
                  <v-icon class="mb-4" color="green" size="60"
                    >mdi-gas-station</v-icon
                  >
                  <span class="text-h4">98</span>
                </p>
                <p class="text-h3">
                  {{ fuel.petrol98 }}
                </p>
              </v-col>
              <v-divider vertical></v-divider>
              <v-col cols="12" lg="3">
                <v-icon class="mb-8" color="black" size="60"
                  >fa fa-oil-can</v-icon
                >
                <p class="text-h3">
                  {{ fuel.diesel }}
                </p>
              </v-col>
              <v-divider vertical></v-divider>
              <v-col cols="12" lg="3">
                <v-icon class="mb-8" color="red" size="60"
                  >mdi-fire-circle</v-icon
                >
                <p class="text-h3">
                  {{ fuel.lpg }}
                </p>
              </v-col>
            </v-row>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      fuel: {
        petrol95: "5.75",
        petrol98: "6.03",
        diesel: "5.78",
        lpg: "3.19"
      },
      option: {
        series: [
          {
            name: "↑ Kilometers",
            data: [
              1730021,
              1235555,
              2221313,
              3221313,
              981313,
              4321313,
              100000,
              342131
            ]
          }
        ],
        colors: ["#55BEB7"],
        chart: {
          type: "area",
          height: "100%",
          zoom: {
            enabled: false
          }
        },
        dataLabels: {
          enabled: false
        },
        stroke: {
          curve: "smooth"
        },

        labels: [
          "January",
          "February",
          "March",
          "April",
          "May",
          "June",
          "July",
          "August",
          "September",
          "October",
          "November",
          "December"
        ],

        legend: {
          horizontalAlign: "left"
        }
      },
      options: {
        series: [1, 2, 1, 1],
        labels: ["In Service", "In Use", "Broken", "Free"],
        chart: {
          type: "polarArea"
        },
        stroke: {
          colors: ["#fff"]
        },
        yaxis: {
          show: false
        },
        fill: {},
        responsive: [
          {
            breakpoint: 480,
            options: {
              chart: {
                width: 200
              },
              legend: {
                position: "bottom"
              }
            }
          }
        ]
      },
      options2: {
        series: [10, 55, 4, 2],
        labels: ["2018", "2017", "2010", "2014"],
        chart: {
          type: "donut"
        },
        stroke: {
          colors: ["#fff"]
        },
        yaxis: {
          show: false
        },
        fill: {},
        responsive: [
          {
            breakpoint: 480,
            options: {
              chart: {
                width: 200
              },
              legend: {
                position: "bottom"
              }
            }
          }
        ]
      }
    };
  }
};
</script>

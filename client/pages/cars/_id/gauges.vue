<template>
  <v-container>
    <v-row>
      <v-col cols="12" xl="6">
        <vc-date-picker
          class="my-4"
          v-model="range"
          :model-config="modelConfig"
          is-range
          is-expanded
          :attributes="attrs"
        />
      </v-col>
      <v-col cols="12" xl="6">
        <Driver />
      </v-col>
    </v-row>
    <v-row>
      <v-col
        cols="12"
        xl="2"
        md="4"
        sm="6"
        v-for="(element, i) in gauge"
        :key="i"
      >
        <div style=" width: 90%;">
          <VueSvgGauge
            :start-angle="-110"
            :end-angle="110"
            :value="element.value"
            :max="element.max"
            :separatorThickness="5"
            :separator-step="0"
            :scale-interval="element.max / 10"
            :inner-radius="80"
            :gaugeColor="[
              { offset: 0, color: 'red' },
              { offset: 100, color: 'yellow' }
            ]"
          >
            <div>
              <div class="innergauge ">
                <p class="mb-0">{{ element.title }}</p>
                <p class="mb-0">{{ element.value }} {{ element.unit }}</p>
              </div>
            </div>
          </VueSvgGauge>
        </div>
      </v-col>
    </v-row>

    <v-row>
      <v-col cols="12" xl="4">
        <v-list
          shaped
          dense
          style="max-height: 40vh"
          class="mt-4 overflow-y-auto new-scroll"
        >
          <v-list-item-title>REPORTS</v-list-item-title>
          <v-list-item-group v-model="selectedItem" color="primary" multiple>
            <v-list-item
              v-for="(item, i) in items"
              :key="i"
              :value="item.value"
            >
              <v-list-item-content>
                <v-list-item-title v-text="item.text"></v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list-item-group>
        </v-list>
      </v-col>
      <v-col cols="12" xl="8">
        <v-sheet
          class="mt-4 v-sheet--offset mx-auto"
          color="#52B2AB"
          elevation="4"
        >
          <apexchart
            height="380px"
            ref="chart"
            type="line"
            :options="options"
            :series="values"
          ></apexchart>
        </v-sheet>
      </v-col>
    </v-row>
    <div style="display: none">
      {{ speed }}, {{ rpm }}, {{ throttle }} {{ engineload }}
    </div>
  </v-container>
</template>

<script>
import Driver from "../../../components/Driver.vue";
import { mapState } from "vuex";
export default {
  created() {
    this.$store.dispatch("gps/getPointsRange", {
      id: this.$route.params.id,
      from: new Date().toISOString(),
      to: new Date().toISOString()
    });
  },
  computed: {
    ...mapState({
      gps: state => state.gps.points
    }),
    speed() {
      let result = this.gps.map(i => i.kph);
      return (
        (this.gauge[0].value =
          parseInt(result.reduce((a, b) => a + b, 0) / result.length) || 0),
        (this.gauge[1].value = Math.max(...result, 0) || 0)
      );
    },
    rpm() {
      let result = this.gps.map(i => i.rpm);
      return (this.gauge[2].value = Math.max(...result, 0) || 0);
    },
    throttle() {
      let result = this.gps.map(i => i.throttle);
      return (this.gauge[3].value =
        parseInt(result.reduce((a, b) => a + b, 0) / result.length) || 0);
    },
    engineload() {
      let result = this.gps.map(i => i.engineload);
      return (
        (this.gauge[4].value = Math.max(...result, 0) || 0),
        (this.gauge[5].value =
          parseInt(result.reduce((a, b) => a + b, 0) / result.length) || 0)
      );
    }
  },
  data() {
    return {
      options: {
        chart: {
          background: "#52B2AB",

          type: "line",
          zoom: {
            enabled: true
          }
        },

        grid: {
          show: false
        },
        colors: [
          "#FFFFFF",
          "#F44336",
          "#E91E63",
          "#9C27B0",
          "#ebc83d",
          "#badf55",
          "#3D5B59",
          "#b06dad",
          "#e96060",
          "#FFAEBC",
          "#A0E7E5",
          "#B4F8C8",
          "#FBE7C6",
          "#B99095"
        ],
        xaxis: {
          labels: {
            show: false
          },
          axisTicks: {
            show: false
          },
          tooltip: {
            enabled: false
          },
          axisBorder: {
            show: false
          }
        },
        yaxis: {
          show: false
        },
        export: {
          csv: {
            headerCategory: "Date"
          }
        }
      },
      attrs: [
        {
          bar: {
            style: {
              backgroundColor: "brown"
            }
          },
          popover: {
            label: "Krzysztof Fryger"
          },
          dates: { start: new Date(), end: new Date() }
        }
      ],
      range: {
        start: new Date(),
        end: new Date()
      },
      modelConfig: {
        start: {
          timeAdjust: "00:00:00"
        },
        end: {
          timeAdjust: "23:59:59"
        }
      },
      gauge: [
        { title: "Avg Speed", unit: "KM/H", value: 0, max: 300 },
        { title: "Top Speed", unit: "KM/H", value: 0, max: 300 },
        { title: "Top RPM", unit: "RPM", value: 0, max: 9000 },
        { title: "Avg Throtle postion", unit: "%", value: 0, max: 100 },
        { title: "Top Engine Load", unit: "%", value: 0, max: 100 },
        { title: "Avg Engine Load", unit: "%", value: 0, max: 100 }
      ],
      values: [{ data: [0, 0] }],
      selectedItem: [3],
      items: [
        {
          text: "Engine Load",
          value: { name: "engineload", unit: "Engine Load - %" }
        },
        {
          text: "Coolant Temp",
          value: { name: "colanttemp", unit: "Coolant Temp - °" }
        },
        {
          text: "Fuel Pressure",
          value: { name: "fuelpressure", unit: "Fuel Pressure - BAR" }
        },
        {
          text: "Mainfold Pressure",
          value: { name: "mainfoldpressure", unit: "Mainfold Pressure - BAR" }
        },
        { text: "RPM", value: { name: "rpm", unit: "RPM" } },
        { text: "Speed", value: { name: "kph", unit: "Speed - KM/H" } },
        // { text: "Timing Advance", value: { name: "", unit: "" } },
        {
          text: "MAF Rate",
          value: { name: "mafrate", unit: "MAF Rate - G/S" }
        },
        {
          text: "Intake Air Temp",
          value: { name: "intakeairtemp", unit: "Intake Air Temp - °" }
        },
        { text: "Throttle", value: { name: "throttle", unit: "Throttle - %" } },
        {
          text: "Fuel Level",
          value: { name: "fuellevel", unit: "Fuel Level - %" }
        },
        // { text: "EVAP Pressure", value: { name: "", unit: "" } },
        { text: "ABS Load", value: { name: "absload", unit: "ABS Load - %" } },
        { text: "Oil Temp", value: { name: "oiltemp", unit: "Oil Temp - °" } },
        { text: "Fuel Rate", value: { name: "fuelrate", unit: "Fuel Rate" } }
        // { text: "Fuel Inject Timing", value: { name: "", unit: "" } },
        //{ text: "Ambient Temp", value: { name: "", unit: "" } }
      ]
    };
  },
  watch: {
    selectedItem: function(v) {
      let values = [];

      v.forEach(e => {
        let result = this.gps.map(i => ({
          x: new Date(Date.parse(i["datetime"])).toUTCString(),
          y: i[e.name]
        }));

        values.push({
          name: e.unit,
          data: result.length == 0 ? [0, 0] : result
        });
      });

      this.values = values;
    },

    range: function(v) {
      this.$store.dispatch("gps/getPointsRange", {
        id: this.$route.params.id,
        from: new Date(v.start).toISOString(),
        to: new Date(v.end).toISOString()
      });
      this.selectedItem = [];
    }
  }
};
</script>

<style scoped>
.innergauge {
  position: absolute;
  left: 50%;
  top: 50%;
  -webkit-transform: translate(-50%, -20%);
  transform: translate(-50%, -20%);
}
p {
  text-align: center;
}
.new-scroll::-webkit-scrollbar {
  width: 15px;
}
.new-scroll::-webkit-scrollbar-track {
  background: #e6e6e6;
  border-left: 1px solid #dadada;
}
.new-scroll::-webkit-scrollbar-thumb {
  background: #b0b0b0;
  border: solid 3px #e6e6e6;
  border-radius: 7px;
}
</style>

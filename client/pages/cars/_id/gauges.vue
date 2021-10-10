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
      <v-col cols="12" xl="6"> </v-col>
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
            separatorThickness="5"
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
          <v-header>REPORTS</v-header>
          <v-list-item-group v-model="selectedItem" color="primary">
            <v-list-item v-for="(item, i) in items" :key="i">
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
          <v-sparkline
            height="100"
            :labels="labels"
            :value="values"
            color="white"
            line-width="2"
            padding="16"
          ></v-sparkline>
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
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
          dates: { start: new Date(2019, 0, 14), end: new Date(2019, 0, 18) }
        }
      ],
      labels: ["12am", "3am", "6am", "9am", "12pm", "3pm", "6pm", "9pm"],
      values: [200, 675, 410, 390, 310, 460, 250, 240],
      selectedItem: 1,
      items: [
        { text: "Engine Load" },
        { text: "Coolant Temp" },
        { text: "Fuel Pressure" },
        { text: "Mainfold Pressure" },
        { text: "RPM" },
        { text: "Speed" },
        { text: "Timing Advance" },
        { text: "MAF Rate" },
        { text: "Intake Air Temp" },
        { text: "Throttle" },
        { text: "Fuel Level" },
        { text: "EVAP Pressure" },
        { text: "ABS Load" },
        { text: "Oil Temp" },
        { text: "Fuel Rate" },
        { text: "Fuel Inject Timing" },
        { text: "Ambient Temp" }
      ],
      gauge: [
        { title: "Avg Speed", unit: "KM/H", value: 60, max: 300 },
        { title: "Top Speed", unit: "KM/H", value: 212, max: 300 },
        { title: "Top RPM", unit: "RPM", value: 4777, max: 9000 },
        { title: "Avg Throtle postion", unit: "%", value: 30, max: 100 },
        { title: "Top Engine Load", unit: "%", value: 15, max: 100 },
        { title: "Avg Engine Load", unit: "%", value: 15, max: 100 }
      ],
      range: {
        start: new Date(2020, 0, 6),
        end: new Date(2020, 0, 9)
      },
      modelConfig: {
        start: {
          timeAdjust: "00:00:00"
        },
        end: {
          timeAdjust: "23:59:59"
        }
      }
    };
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

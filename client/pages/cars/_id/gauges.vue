<template>
  <v-container>
    <v-row>
      <v-col cols="12" xl="6">
        <v-calendar
          ref="calendar"
          v-model="value"
          :weekdays="weekday"
          type="month"
          :events="events"
          :event-overlap-mode="mode"
          :event-overlap-threshold="30"
          :event-color="getEventColor"
          @change="getEvents"
        ></v-calendar>
      </v-col>
      <v-col cols="12" xl="6"></v-col>
    </v-row>
    <v-row>
      <v-col cols="12" xl="2">
        <div style=" width: 90%;">
          <VueSvgGauge
            :start-angle="-110"
            :end-angle="110"
            value="80"
            separatorThickness="5"
            :separator-step="20"
            :scale-interval="10"
            :inner-radius="80"
            :gaugeColor="[
              { offset: 0, color: 'red' },
              { offset: 100, color: 'yellow' }
            ]"
          >
            <div>
              <div class="innergauge">
                <p class="mb-0">AVG Speed</p>
                <p class="mb-0">67 Km/h</p>
              </div>
            </div>
          </VueSvgGauge>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data() {
    return {};
  }
};
</script>

<style scoped>
.innergauge {
  position: absolute;
  left: 50%;
  top: 50%;
  -webkit-transform: translate(-50%, 0%);
  transform: translate(-50%, 0%);
}
</style>

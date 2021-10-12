<template>
  <apexchart
    ref="chart"
    type="line"
    :options="options"
    :series="series"
  ></apexchart>
</template>

<script>
export default {
  props: {
    chartTitle: {
      default: "Title"
    },
    chartColor: {
      default: "#FF1654"
    }
  },
  data() {
    return {
      options: {
        animations: {
          enabled: true,
          easing: "linear",
          dynamicAnimation: {
            speed: 1000
          }
        },
        tooltip: {
          x: {
            show: false
          }
        },
        grid: {
          show: false
        },
        title: {
          text: this.chartTitle,
          align: "left",
          margin: 10,
          offsetX: 10,
          offsetY: 0,
          floating: false,
          style: {
            fontSize: "18px",
            fontWeight: "bold"
          }
        },

        markers: {
          size: 3
        },
        colors: [this.chartColor],
        stroke: {
          curve: "smooth"
        },
        chart: {
          id: this.title
        },
        xaxis: {
          categories: [""],
          tooltip: {
            enabled: false
          }
        },

        yaxis: {
          axisTicks: {
            show: true
          }
        }
      },
      series: [
        {
          name: "KM/H",
          data: [
            30,
            40,
            45,
            50,
            49,
            60,
            70,
            91.2,
            400,
            123,
            12313,
            12313,
            1231321,
            123,
            123,
            12312333,
            444
          ]
        }
      ]
    };
  }
};
</script>

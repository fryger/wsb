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
    },
    unit: {
      default: "Unit"
    },
    data: {
      default: [0]
    }
  },
  watch: {
    data: function(newVal, oldVal) {
      this.arr.push(newVal[0]);
      this.arr = this.arr.filter(item => item);
      this.arr = this.arr.slice(-10);
      this.$refs.chart.updateSeries([
        {
          data: this.arr
        }
      ]);
    }
  },
  data() {
    return {
      arr: [],
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
          size: 0
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
          name: this.unit,
          data: this.arr
        }
      ]
    };
  }
};
</script>

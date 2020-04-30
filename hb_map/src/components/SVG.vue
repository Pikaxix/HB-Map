<template>
  <div class="container">
    <div class="mapcontainer">
      <svg class="bodymap">
        <path
          v-for="(item,index) in path"
          fill="#EDE097"
          stroke="#EDE097"
          :d="item.d"
          stroke-width="1"
          opacity="0.4"
          :transform="item.transform"
          :id="item.id"
          :key="item.id"
          @mouseenter="svgenter(item.id)"
          @mouseout="svgout(item.id,index)"
        />
      </svg>
      <b-tooltip
        v-for="item in path"
        :key="item.id"
        :target="item.id"
        placement="bottom"
        triggers="hover"
      >
        <p>{{ item.titletip }}</p>
      </b-tooltip>
    </div>
    <div class="barcontainer">
      <GChart
        type="BarChart"
        :data="chartData"
        :options="chartOptions"
        :events="chartEvents"
        ref="gChart"
      />
    </div>
  </div>
</template>

<script>
export default {
  name: 'socrec',
  data () {
    return {
      IsShow: true,
      default_style: 'opacity: 0.4',
      default_opacity: 0.2,
      path: [
        {
          id: '1',
          titletip: '1',
          d:
            'M422.73,790.55a16.37,16.37,0,0,1,3.82.54v1.09c1.65,2.41.94,9.2,1.63,12.55a11.1,11.1,0,0,0,6.55,1.63c3-2.58,7.65-7.5,12.54-7.63.44,1.48.33,3.55,1.64,4.36,1.17,1.09,2.5,1.13,4.91,1.09,2.14-2.14,6.82-6.76,10.36-7.09.57,1.17.81,4.71,1.64,6a4.57,4.57,0,0,0,3.27,1.64c.56-.44.15-.2,1.09-.55v-.54c-3.07-2.47-1.54-7.59-2.18-11.46a9.36,9.36,0,0,0-3.27-1.09c-1.06.88-2.61.82-3.82,1.64-3.92,2.66-3.87,8.22-10.36,7.09-.93-2.13-1.94-4.82-3.28-6.55-4.69,1.09-5.37,4.29-8.18,7.09l-3.82,2.73a21.74,21.74,0,0,1-4.91-.54c-.86-4.15-.38-12.24-4.36-13.64-1.22-.76-1.79-.3-3.27,0Z',
          stroke: '#001',
          fiil: '#EDE097',
          opacity: '',
          transform: 'translate(-360.24 -530.91)'
        }

      ],
      chartData: [
        ['Element', 'Density', { role: 'style' }, { role: 'annotation' }],
        ['Copper', 8.94, '#b87333', 'Cu'],
        ['Silver', 10.49, 'silver', 'Ag'],
        ['Gold', 19.30, 'gold', 'Au'],
        ['Platinum', 21.45, 'color: #e5e4e2', 'Pt']
      ],
      chartOptions: {
        chart: {
          title: 'Google Charts In Vue.js',
          subtitle: 'Sales, Expenses, and Profit: 2014-2017'
        }
      },
      chartEvents: {
        onmousenover: () => {
          const barchart = this.$refs.gChart.chartObject
          const selection = barchart.getSelection()
          const onSelectionMeaasge =
            selection.length !== 0 ? 'row was selected' : 'row was diselected'
          alert(onSelectionMeaasge)
        }
      }
    }
  },
  methods: {
    svgenter (svgid) {
      var id = document.getElementById(svgid)
      id.style.opacity = 1
    },
    svgout (svgid, index) {
      var id = document.getElementById(svgid)
      id.style.opacity = this.path[index].opacity
    }
  }
}
</script>

<style lang="less" scoped>
.mapcontainer {
  border-style: dashed;
  border-width: 5px;
  border-color: #8b8a8a;
  margin: 0 auto;
  width: 300px;
  height: 500px;
  background: url("../assets/img/body_map.png") no-repeat;
  background-size: 270px 480px;
  .bodymap {
    width: 400px;
    height: 600px;
    position: relative;
    top: 12.5%;
    left: 14.5%;
    float:left;
  }
}
</style>

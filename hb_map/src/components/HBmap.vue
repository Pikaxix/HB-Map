<template>
  <el-main class="HBmap">
    <div class="intro">
      <div>
        <h3>Interactive Bodymap</h3>
        <div style=" padding:10px;">
          <h6>All of the XXXX available samples In our database:</h6>
        </div>
      </div>
    </div>
    <el-divider></el-divider>
    <div class="main-container">
      <div class="mapcontainer">
        <svg class="bodymap">
          <path
            v-for="item in bodysites"
            :fill="item.fill"
            stroke="#4898ff"
            :d="item.d"
            stroke-width="1"
            :opacity="item.opacity"
            :transform="item.transform"
            :id="item.id"
            :key="item.id"
            @mouseenter="svgenter(item.site)"
            @mouseout="svgout(item.site)"
          />
        </svg>
        <b-tooltip
          v-for="item in bodysites"
          :key="item.id"
          :target="item.id"
          placement="bottom"
          triggers="hover"
        >
          <p>{{ item.titletip }}</p>
        </b-tooltip>
      </div>
      <div class="chart-box">
        <div class="home-chart">
          <span class="origin">0</span>
          <div class="x-data">
            <ul>
              <li>
                <span>50</span>
              </li>
              <li>
                <span>100</span>
              </li>
              <li>
                <span>150</span>
              </li>
              <li>
                <span>200</span>
              </li>
            </ul>
          </div>
          <div class="y-data">
            <ul :id="item.site" v-for="(item,index) in bodysites" :key="index" :class="item.id">
              <li>
                <div class="name">{{item.site}}</div>
                <div class="value">
                  <span
                    class="normal-line"
                    v-bind:title="item.normal"
                    @mouseenter="svgenter(item.site)"
                    @mouseout="svgout(item.site)"
                    :style="{
                      width:(item.normal/2)+'%',
                      opacity:item.opacity}"
                  ></span>
                </div>
              </li>
              <li>
                <div class="value">
                  <span
                    class="abnormal-line"
                    v-bind:title="item.abnormal"
                    @mouseenter="svgenter(item.site)"
                    @mouseout="svgout(item.site)"
                    :style="{
                      width:(item.abnormal/2)+'%',
                      opacity:item.opacity}"
                  ></span>
                </div>
              </li>
            </ul>
          </div>
        </div>
        <img src="../assets/img/mark.png" height="55px%" width="100px" class="mark">
      </div>
    </div>
  </el-main>
</template>

<script>
export default {
  data () {
    return {
      total_sum: 0,
      buf_opacity: '0',
      bodysites: {
        rectum: {
          d:
            'M457.64,811.82c-6.56-0.42-11.25-1.56-10.91,6.55c-1.58,1.96-1.26,3.92-1.09,6.55c1.51,1.3,0.69,2.13,1.64,3.27c1.05,1.28,7.09,0.61,9.27,0.55c0-0.18,0-0.36,0-0.55c0.18,0,0.36,0,0.55,0C457.8,821.96,458.09,818.36,457.64,811.82z',
          fill: '#ffd8d8',
          opacity: '0',
          transform: 'translate(-359 -532.3)'
        },
        nose: {
          d:
            'M448.36,548.36c1.09,0,2.18,0,3.27,0c0.07-3.86-0.33-11.13-2.18-13.64C449.09,539.27,448.73,543.82,448.36,548.36z',
          fill: '#589fff',
          opacity: '0',
          transform: 'translate(-359 -532.3)'
        },
        oral: {
          d:
            'M441.82,562.55c5.45,0,10.91,0,16.36,0c-0.15,4.2-2.14,8.71-5.45,9.82c-2.08,1.69-4.11,0.63-6.55,0C444.26,569.36,442.19,567.29,441.82,562.55z',
          fill: '#eaa0ff',
          opacity: '0',
          transform: 'translate(-359 -532.3)'
        },
        esophagus: {
          d:
            'M443.45,587.09c1.45,0,2.91,0,4.36,0c1.51,2.87,1.16,8.59,1.09,13.09c1.42,2.25,1.11,19.32,1.09,22.91c-0.18,0-0.36,0-0.55,0c0,0.18,0,0.36,0,0.55c-1.45,0.18-2.91,0.36-4.36,0.55c-0.5-1.45-0.57-3.78-0.55-6c-1.26-2.02-0.52-7.35-0.55-10.36C443.95,601.43,443.4,594.21,443.45,587.09z',
          fill: '#bc40e0',
          opacity: '0',
          transform: 'translate(-359 -532.3)'
        },
        upper_respiratory_tract: {
          d:
            'M451.64,587.09c1.45,0,2.91,0,4.36,0c1.51,2.87,1.16,8.59,1.09,13.09c1.42,2.25,1.11,19.32,1.09,22.91c-0.18,0-0.36,0-0.55,0c0,0.18,0,0.36,0,0.55c-1.45,0.18-2.91,0.36-4.36,0.55c-0.5-1.45-0.57-3.78-0.55-6c-1.26-2.02-0.52-7.35-0.55-10.36C452.13,601.43,451.58,594.21,451.64,587.09z',
          fill: '#edb2e9',
          opacity: '0',
          transform: 'translate(-359 -532.3)'
        },
        blood: {
          d:
            'M520.91,765.45c-.12-12,4.78-18.92,7.64-27.27l.54-24a107.65,107.65,0,0,0-2.73-35.45c-1.39-5.33-.58-10-2.18-14.73-2.31-6.91-5.72-14.25-9.82-19.64-2.1-2.76-8.35-5-9.27-7.09h2.18l8.18,6.55c4.41,5.85,7.93,13.68,10.37,21.27q2.17,13.36,4.36,26.73c.18,2.36.37,4.73.55,7.09.6,1.4,2.6,3.37,3.27,4.91,2.54,5.89,3.18,12.45,3.27,20.73h-1.09v-3.82c-1-1.7.05-4.7-.54-7.09a73.89,73.89,0,0,0-4.37-12.55h-.54v16.36c-2.1,3.32-.55,13.38-.55,18,0,6.81-1.48,27.6.55,32.19,2.49,5.66,7.24,8.36,7.63,17.45h-.54V784c-1.57-2.3-1.52-5.52-2.73-8.18-.93-2.05-2.73-4.29-3.82-6.55h-.54v1.09q1.37,7.1,2.72,14.19c2.56,7.8,9.4,13.36,9.82,22.36h-.54v-1.09a20.46,20.46,0,0,1-3.28-6.55h-.54c.08,2.71.78,6.3,0,7.64a89.88,89.88,0,0,1-.55-9.27c0-1.17-3.75-6.56-4.36-8.73h-1.09V796c1,1.37,1.41,6.34.54,7.64-2.28-20.2-4.73-38.55-4.9-62.19H528V742c-.88.94-4.59,9.3-3.82,11.45s2.39,3.53,2.73,7.1h-.55V760a16.48,16.48,0,0,1-2.18-5.45h-.54v.54c-1.55,2.06-2,7.66-1.09,10.36Z',
          fill: '#ffd07a',
          opacity: '0',
          transform: 'translate(-359 -532.3)'
        },
        lung: {
          d:
            'M435.27,643.27c11.58,0.18,10.36,19.35,10.36,31.09c0,20.75-2.88,25.55-15.27,33.82c-2.65,1.77-8.51,6.28-14.18,4.36c-6.42-2.17-5.23-13.81-3.27-20.73C417.99,673.86,423.85,655.04,435.27,643.27zM463.64,644.91c2.63,0.33,6.3-0.22,9.27,1.09c13.1,5.78,17.09,22.91,20.73,38.73c1.57,6.82,1.63,22.07-1.64,27.27c-5.85,9.33-21.34,7.34-25.09-2.73c-2.49-6.69,1.85-11.64,2.18-17.45c-1.98-1.47-3.44-4.01-5.45-5.45c-4.57-3.27-9.88-4.71-10.91-11.45c-1-6.6,5.46-9.65,7.09-13.64c0.18-3.64,0.36-7.27,0.55-10.91c0.55-1.45,1.09-2.91,1.64-4.36C462.69,645.65,463.13,645.41,463.64,644.91z',
          fill: '#ffbd7a',
          opacity: '0',
          transform: 'translate(-359 -532.3)'
        },
        liver: {
          d:
            'M460.36,709.82c-5,2.92-24-1.25-30.54,1.09-7.25,2.58-10.16,9.37-12,17.45-1.49,6.54.72,11.07,6,11.46,1.61-1.26,4.13-1.08,6-2.18a37,37,0,0,0,9.27-8.73c1.58-2.19,3.61-9.79,5.46-10.91v3.82a13.75,13.75,0,0,0-2.19,4.91H444c6.14-4.13,18.63-6.45,19.09-15.82A13.86,13.86,0,0,0,460.36,709.82Z',
          fill: '#ffbf4c',
          opacity: '0',
          transform: 'translate(-359 -532.3)'
        },
        stomach: {
          d:
            'M443.45,756.73h2.19c.9-4.62,1.44-8.4,7.63-8.18,2.62,2.28,5.69,2.32,9.82,3.27,15.05,3.47,20.44-13.39,17.46-25.64-2.83-1.84-3.56-2.45-7.64-2.18-1.85,2.48-5.41,5.71-10.91,4.36-1.27-.31-1.54-1-2.73-.54a5.15,5.15,0,0,0-1.63,2.18h1.09c1.48,1.09,4.87.58,6.54,1.64.53.77.54,1.78.55,3.27-2.64,3.06-4.23,7-8.18,8.73-4.7,2-10.13-1.09-12,3.81C444.17,749.36,443.64,753.78,443.45,756.73Z',
          fill: '#ff73f6',
          opacity: '0',
          transform: 'translate(-359 -532.3)'
        },
        pancreas: {
          d:
            'M453.27,756.73c-.47.35-1.71.73-2.18,1.09-2.08.68-2.13,1.1-2.18,3.82,1.53.82,2.71,1.11,5.45,1.09,3-3.14,15.19,1.2,19.64-1.64C465.87,761.26,459.36,759,453.27,756.73Z',
          fill: '#ffa658',
          opacity: '0',
          transform: 'translate(-359 -532.3)'
        },
        skin: {
          d:
            'M370.91,772c-6.05,6.18-9.85,15.39-7.09,27.27a8.39,8.39,0,0,0,2.73.55c.55-.44.14-.2,1.09-.55,4.42-6.91,8.5-15.17,6-26.18a3.25,3.25,0,0,1-1.09-1.09Z',
          fill: '#737cff',
          opacity: '0',
          transform: 'translate(-359 -532.3)'
        },
        colon: {
          d:
            'M459.82,811.82c0.23,2.55,0.78,4.81,0,7.09c3.58,0.37,7.1,3.01,12,1.64c2.93-0.82,13.76-5.98,15.27-8.18c0.73-2.18,1.45-4.36,2.18-6.55c1.97-3.43,4.31-6.3,4.91-11.45c-2.82-2.51-2.41-3.84-2.18-8.73c-2-1.35-2.41-2.78-5.45-3.27c0.05-1.69,0.08-3.45-0.55-4.36c-0.49-1.46-0.56-1.41-1.64-2.18c-1.93-1.49-3.84-0.52-6.55-1.64c-0.66-0.27-1.92-1.91-2.73-2.18c-6.72-2.3-11.62,2.77-14.73,4.36c-2.25,1.15-4.04-2.14-7.09-1.09c-0.36,0.12-0.98,1.58-1.09,1.64c-1.46,0.73-6.73-1.28-8.18-1.64c-4.13-1-11.72,2.97-12.55,2.18c-1.8-0.64-2.76-2.17-4.36-2.73c-4.68-1.63-11.93-0.21-13.64,2.73c-1.08,1.85-0.02,3.72-0.55,4.91c-0.91,0.73-1.82,1.45-2.73,2.18c-1.08,1.64-2.74,6.57-1.64,9.82c0.13,0.39,1.54,1.38,1.64,1.64c1.08,2.97-1.99,6.06-2.18,9.27c0.18,0,0.36,0,0.55,0c1.94-1.64,8.43-1.17,9.82-3.27c3.91-5.6-3.58-16.13,7.09-16.36c5.2,3.9,11.24-0.23,15.82-1.09c0.6,1.72,1.15,1.62,2.18,2.73c3.49,0.1,8.06,0.56,11.45-1.09c0.66-0.32,1.89-1.99,2.73-2.18c2.96-0.68,4.25,3.11,7.64,2.18c2.54-0.7,3.61-3.19,6.55-3.82c1.12,3.04,5.34,2.7,8.73,3.27c0.51,2.65,1.62,2.27,2.18,4.91c-2.6,2.96,0.04,9.56-0.55,13.09c-2.1,0.75-4.36,0.99-6,2.18c-0.18,0.55-0.36,1.09-0.55,1.64c-2.02,1.33-5.23,0.4-7.09,1.64c-1.18,0.79-2.69,4.52-3.82,4.91C464.02,814.24,461.38,812.07,459.82,811.82z',
          fill: '#64d0ff',
          opacity: '0',
          transform: 'translate(-359 -532.3)'
        },
        ileum: {
          d:
            'M422.73,790.55a16.37,16.37,0,0,1,3.82.54v1.09c1.65,2.41.94,9.2,1.63,12.55a11.1,11.1,0,0,0,6.55,1.63c3-2.58,7.65-7.5,12.54-7.63.44,1.48.33,3.55,1.64,4.36,1.17,1.09,2.5,1.13,4.91,1.09,2.14-2.14,6.82-6.76,10.36-7.09.57,1.17.81,4.71,1.64,6a4.57,4.57,0,0,0,3.27,1.64c.56-.44.15-.2,1.09-.55v-.54c-3.07-2.47-1.54-7.59-2.18-11.46a9.36,9.36,0,0,0-3.27-1.09c-1.06.88-2.61.82-3.82,1.64-3.92,2.66-3.87,8.22-10.36,7.09-.93-2.13-1.94-4.82-3.28-6.55-4.69,1.09-5.37,4.29-8.18,7.09l-3.82,2.73a21.74,21.74,0,0,1-4.91-.54c-.86-4.15-.38-12.24-4.36-13.64-1.22-.76-1.79-.3-3.27,0Z',
          fill: '#ff73a0',
          opacity: '0',
          transform: 'translate(-360.24 -530.91)'
        },
        cecum: {
          d:
            'M411.27,812.36c-0.19,2.03-0.92,3.45,0,4.91c0.84,2.69,2.36,2.89,6,2.73c0.56-0.44,0.15-0.19,1.09-0.55c0.47-0.8,0.99-1.56,1.64-2.18c0.26-5.36,0.23-8.15-1.64-12c-3.39-0.23-7.41,0.23-10.36,1.64c0.55,1.82,1.09,3.64,1.64,5.45C410.18,812.36,410.73,812.36,411.27,812.36z',
          fill: '#ffb5a0',
          opacity: '0',
          transform: 'translate(-359 -532.3)'
        },
        cervix: {
          d:
            'M453.82,862.55c-2.79,0.35-5.39,0.35-8.18,0c-0.26-7.87-3.3-18.13-9.27-19.64c-5.47,4.57-19.8,1.37-19.64-6.55c0.96-0.59,1.97-1.37,2.73-2.18c2.18-0.18,4.36-0.36,6.55-0.55c3.6,1.12,4.65,3.65,10.36,3.82c2.58-4.04,13.73-8.26,21.27-4.91c1.77,0.78,2.3,2.5,4.36,3.27c2.81-2.58,7.82-3.81,13.09-3.82c2.37,2.15,3.85,1.68,3.82,6.55c-0.44,0.56-0.19,0.15-0.55,1.09c-4.95,2.9-10.97,4.18-18.55,3.27C457,848.89,454.25,853.55,453.82,862.55z',
          fill: '#ff9f73',
          opacity: '0',
          transform: 'translate(-359 -536.3)'
        },
        urethra: {
          d:
            'M446.73,854.36c-0.04,2.95,0.3,5.48,1.09,7.64c1.12-0.39,2.55-0.54,4.36-0.55c0.18-2.36,0.36-4.73,0.55-7.09C450.73,854.36,448.73,854.36,446.73,854.36z',
          fill: '#fe9f73',
          opacity: '0',
          transform: 'translate(-359 -532.3)'
        },
        vagina: {
          d:
            'M445.64,863.64c4.75-0.04,9.64,0.24,13.64,0.55c0.67,1.24,0.89,1.23,1.09,3.27c-0.55,0.18-1.09,0.36-1.64,0.55c-4.67,3.43-13.94,1.79-19.09,0.55c-0.34-0.96-0.11-0.53-0.55-1.09c0-0.36,0-0.73,0-1.09C440.79,865.48,443.92,864.84,445.64,863.64z',
          fill: '#ff6f6f',
          opacity: '0',
          transform: 'translate(-359 -532.3)'
        }
      }
    }
  },
  created () {
    this.getbodysites()
  },
  methods: {
    svgenter (svgid) {
      this.buf_opacity = this.bodysites[svgid].opacity
      this.bodysites[svgid].opacity = 1
    },
    svgout (svgid) {
      this.bodysites[svgid].opacity = this.buf_opacity
    },
    getbodysites () {
      this.axios
        .get('bodysites')
        .then(res => {
          for (var i = 0; i < res.data.bodysites.length; i++) {
            this.bodysites[res.data.bodysites[i].site].site =
              res.data.bodysites[i].site
            this.bodysites[res.data.bodysites[i].site].titletip =
              res.data.bodysites[i].site
            this.bodysites[res.data.bodysites[i].site].opacity =
              (res.data.bodysites[i].normal / res.data.total_sum) * 5
            this.bodysites[res.data.bodysites[i].site].normal =
              res.data.bodysites[i].normal
            this.bodysites[res.data.bodysites[i].site].abnormal =
              res.data.bodysites[i].abnormal
            this.bodysites[res.data.bodysites[i].site].disease =
              res.data.bodysites[i].disease
            this.bodysites[res.data.bodysites[i].site].id =
              res.data.bodysites[i].id
          }
          this.total_sum = res.data.total_sum
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error(error);
        })
    }
  }
}
</script>

<style lang="less">
.HBmap {
  padding: 0px 0px 0px 0px;
}
.intro {
  background-color: #cccccc;
}
.mapcontainer {
  border-style: dashed;
  border-width: 5px;
  border-color: #8b8a8a;
  margin: 0 auto;
  width: 300px;
  height: 500px;
  float: left;
  background: url("../assets/img/body_map.png") no-repeat;
  background-size: 270px 480px;
  .bodymap {
    width: 400px;
    height: 600px;
    position: relative;
    top: 12.5%;
    left: 14.5%;
    float: left;
  }
}
.chart-box {
  background-color: #6699cc;
  width: 70%;
  height: 500px;
  float: right;
  .mark{
    position: relative;
    left: 1%;
    top:2%;
    background-color: #6699cc;
  }
  .home-chart {
    position: relative;
    left: 30%;
    top: 5%;
    width: 65%;
    border-left: 1px solid #cd9ec1;
    border-bottom: 1px solid #cd9ec1;
    position: relative;
    .origin {
      font-size: 12px;
      color: #fff;
      position: absolute;
      left: -5px;
      bottom: -20px;
    }
    .x-data {
      position: absolute;
      width: 90%;
      height: 100%;
      left: 0;
      bottom: 0;
      ul {
        width: 100%;
        height: 100%;
        padding: 0;
        margin: 0;
        li {
          float: left;
          list-style: none;
          width: 25%;
          height: 100%;
          border-right: 1px solid rgba(255, 255, 255, 0.24);
          position: relative;
          span {
            font-size: 12px;
            color: #fff;
            position: absolute;
            right: -13px;
            bottom: -20px;
          }
        }
      }
    }
    .y-data {
      min-height: 10px;
      ul {
        padding: 0;
        margin: 0;
        li {
          width: 100%;
          height: 5px;
          list-style: none;
          position: relative;
          padding: 2px 0;
          margin-bottom: 8px;
          .name {
            font-size: 12px;
            color: #fff;
            line-height: 18px;
            position: absolute;
            width: 150px;
            top: 0;
            left: -155px;
          }
          .value {
            width: 100%;
            height: 10px;
            .normal-line {
              display: block;
              height: 100%;
              background: #99cc99;
              border-radius: 0 24px 24px 0;
            }
            .abnormal-line {
              display: block;
              height: 100%;
              background: #cc99cc;
              border-radius: 0 24px 24px 0;
            }
          }
        }
      }
    }
  }
}
</style>

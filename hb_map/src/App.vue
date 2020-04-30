<template>
  <el-container class="homecontainer">
    <!-- Herader -->
    <el-header height="100px;">
      <div class="logobox">
        <div class="logo">
          <img src="../src/assets/img/logo.png" height="40px%" width="40px">
          <span style="font-size:30px;font-weight:bold;">HB Map </span>
          <span style="font-size:15px;font-weight:bold;">A Website for XXXX</span>
        </div>
      </div>
      <div class="menu-box">
        <el-menu
          class="menu"
          :default-active="$route.path"
          mode="horizontal"
          background-color="#669999"
          text-color="#FFFFFF"
          active-text-color="#FFFFFF"
          router
        >
          <el-menu-item index="/">Home</el-menu-item>
          <el-menu-item index="/HBmap">HB Map</el-menu-item>
          <el-menu-item index="/broswer">Broswer</el-menu-item>
          <el-submenu index="3">
            <template slot="title">Functions</template>
            <el-menu-item index="/motherboard">S1</el-menu-item>
            <el-menu-item index="/2-2">S2</el-menu-item>
            <el-menu-item index="/2-3">S3</el-menu-item>
          </el-submenu>
          <el-menu-item index="/help">Help</el-menu-item>
        </el-menu>
      </div>
    </el-header>
    <!-- Main -->
    <el-main >
      <router-view></router-view>
    </el-main>
    <!-- Footer -->
    <!-- <el-footer>Footer</el-footer> -->
  </el-container>
</template>

<script>
export default {}
</script>

<style lang="less" scoped>

.el-header {
  padding: 0;
  .logobox {
    height: 50px;
    background-color: #6699CC;
    .logo {
      width: 400px;
      position: relative;
      left: 37%;
    }
  }
  .menu-box {
    height: 62px;
    background-color: #669999;
    .menu {
      width: 600px;
      position: relative;
      left: 29%;
      el-menu {
        .el-menu-item {
          font-size: 17px;
        }
        /deep/ .el-submenu .el-submenu__title {
          font-size: 17px;
        }
      }
    }
  }
}
</style>

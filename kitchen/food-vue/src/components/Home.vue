<template>
  <div v-resize="changeNav">
    <mu-linear-progress style="position: fixed;" v-if="progress"></mu-linear-progress>
    <div>
      <template v-if="show.login">
        <Login @goMain="goMain" @openColorSnackbar="openColorSnackbar" @closeColorProgressbar="closeColorProgressbar"
               @openColorProgressbar="openColorProgressbar" @goRegistration="goRegistration"></Login>
      </template>

      <template v-else-if="show.register">
        <Registration @goMain="goMain" @openColorSnackbar="openColorSnackbar"
                      @closeColorProgressbar="closeColorProgressbar"
                      @openColorProgressbar="openColorProgressbar" @auth="auth"></Registration>
      </template>

      <template v-else>
        <div>

          <div :class="[progress ? 'app-progress' : '', open_drawer ? 'draw-move': 'draw-return']">
            <mu-appbar style="width: 100%; text-align: right; position: fixed" color="primary">
              <mu-button icon slot="left" @click="open_drawer = !open_drawer">
                <mu-icon value="menu"></mu-icon>
              </mu-button>
              <div :class="[open_drawer ? 'app-move': 'app-return']">
                Genius Plaza
              </div>
            </mu-appbar>
          </div>
        </div>
        <mu-container :class="[progress ? 'app-progress' : '', open_drawer ? 'draw-move': 'draw-return']">
          <mu-container style="padding-top: 80px;">
            <Ingredients v-if="show.ingredients" @closeColorProgressbar="closeColorProgressbar"
               @openColorProgressbar="openColorProgressbar" @openColorSnackbar="openColorSnackbar"></Ingredients>
            <!--          <Products v-if="show.products" @openColorSnackbar="openColorSnackbar"></Products>-->
            <!--          <Order v-if="show.order" :order_num="order_num"></Order>-->
          </mu-container>
        </mu-container>

        <div>                           <!--left bar-->
          <mu-drawer @change="changeNav" width="256" :docked="docked" :open.sync="open_drawer"
                     style="transition: all .25s; background-color: #424242;">
            <br>
            <h1 style="text-align: center; color: #e0e0e0">Dashboard</h1>
            <br>
            <mu-list>

              <mu-list-item button @click="" :ripple="true">
                <mu-list-item-action>
                  <mu-icon value="dashboard" color="grey300"></mu-icon>
                </mu-list-item-action>
                <mu-list-item-title style="color: #e0e0e0">Recipes</mu-list-item-title>
              </mu-list-item>

              <mu-list-item button @click="goIngredients" :ripple="true">
                <mu-list-item-action>
                  <mu-icon value="shopping_cart" color="grey300"></mu-icon>
                </mu-list-item-action>
                <mu-list-item-title style="color: #e0e0e0">Ingredients</mu-list-item-title>
              </mu-list-item>

              <mu-list-item button @click="" :ripple="true">
                <mu-list-item-action>
                  <mu-icon value="tablet_android" color="grey300"></mu-icon>
                </mu-list-item-action>
                <mu-list-item-title style="color: #e0e0e0">Users</mu-list-item-title>
              </mu-list-item>

            </mu-list>
            <mu-divider></mu-divider>
            <br>
            <br>

            <mu-list>
              <mu-list-item button :ripple="true">
                <mu-icon value="power_settings_new" color="grey300"></mu-icon>
                <mu-list-item-title style="margin-left: 20px; color: #e0e0e0" @click='logout'>Exit
                </mu-list-item-title>
                <mu-list-item-action>
                </mu-list-item-action>
              </mu-list-item>
            </mu-list>
          </mu-drawer>
        </div>                           <!--left bar-->

      </template>

      <mu-snackbar position='top' color="success" :open.sync="snackbar">
        <mu-icon left value="info"></mu-icon>
        {{ snackbar_message }}
        <mu-button flat slot="action" color="#fff" @click="snackbar = false">Close</mu-button>
      </mu-snackbar>
    </div>
  </div>
</template>

<script>
  import Login from "./Login";
  import Registration from "./Registration";
  import Ingredients from "./Ingredients";

  export default {
    name: "Home",
    components: {
      Login,
      Registration,
      Ingredients,
    },
    data() {
      return {
        docked: true,
        open_drawer: true,
        width: '',
        show: {
          register: false,
          login: false,
          ingredients: false,
          products: false,
          order_list: false,
          order: false,
        },
        snackbar: false,
        snackbar_message: '',
        timeout: 3000,
        progress: false,
        progress_timeout: 1100,
      }
    },
    created() {
      this.auth();
    },
    mounted() {
      this.width = window.innerWidth;
    },
    methods: {
      changeNav() {
        this.width = window.innerWidth;
        if (this.width > 800) {
          this.docked = true;
          this.open_drawer = true;
        } else {
          this.docked = false;
          this.open_drawer = false;
        }
      },
      auth() {
        this.show.login = !sessionStorage.getItem('auth_token');
      },
      openColorSnackbar(snack_mes) {
        this.snackbar = true;
        this.snackbar_message = snack_mes;
        setTimeout(() => {
          this.snackbar = false;
        }, this.timeout);
      },
      openColorProgressbar() {
        this.progress = true;
      },
      closeColorProgressbar() {
        setTimeout(() => {
          this.progress = false;
        }, this.progress_timeout);
      },
      logout() {
        sessionStorage.removeItem('auth_token');
        window.location = '/';
      },
      goMain() {
        this.show.login = false;
        this.show.register = false;
        this.show.order_list = true;
      },
      goRegistration() {
        this.show.login = false;
        this.show.register = true;
      },
      goIngredients() {
        this.show.ingredients = true;
        this.show.products = false;
        this.show.order_list = false;
        this.show.order = false;
      },
    }
  }

</script>

<style scoped>
  .app-progress {
    padding-top: 4px;
  }

  .draw-move {
    transition: all .25s;
    margin-left: 256px;
  }

  .draw-return {
    transition: all .25s;
    margin-left: 0;
  }

  .app-move {
    transition: all .25s;
    margin-right: 256px;
  }

  .app-return {
    transition: all .25s;
    margin-right: 0px;
  }

</style>

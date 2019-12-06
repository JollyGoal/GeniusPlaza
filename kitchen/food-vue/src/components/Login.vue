<template>
  <div>
    <mu-container>
      <br>
      <mu-row justify-content="center">
        <mu-form :model="form" style="background-color: #424242;" label-width="100" class="mu-demo-form">
          <mu-container justify-content="center" style="text-align: center; padding-left: 10px;">
            <h1>Sign In</h1>
            <mu-container>
              <mu-form-item prop="username" label="Username" style="width: 60%">
                <mu-text-field v-model="form.login"></mu-text-field>
              </mu-form-item>
              <mu-form-item prop="password" label="Password" style="width: 60%">
                <mu-text-field type="password" v-model="form.password" prop="password"
                               :action-icon="visibility ? 'visibility_off' : 'visibility'"
                               :action-click="() => (visibility = !visibility)"
                               :type="visibility ? 'text' : 'password'"></mu-text-field>
              </mu-form-item>
              <mu-container>
                <span>Still don't have an account?<a @click="goRegistration"> Register now!</a></span>
              </mu-container>
            </mu-container>
            <mu-container style="padding-bottom: 26px;">
              <br>
              <mu-button color="primary" @click="setLogin">Enter</mu-button>
            </mu-container>
          </mu-container>
        </mu-form>
      </mu-row>

      <mu-snackbar position='top-start' color="error" :open.sync="snackbar">
        <mu-icon left value="error"></mu-icon>
        {{snackbar_message}}
        <mu-button flat slot="action" color="#fff" @click="snackbar = false">Close</mu-button>
      </mu-snackbar>

    </mu-container>
  </div>
</template>

<script>
  import $ from 'jquery'

  export default {
    name: "Login",
    data() {
      return {
        form: {
          login: '',
          password: '',
        },
        visibility: false,
        snack_mes_logged: 'Welcome back!',
        snackbar: false,
        snackbar_message: '',
        timeout: 3000,
      }
    },
    methods: {
      setLogin() {
        this.$emit('openColorProgressbar');
        $.ajax({
          url: 'http://127.0.0.1:8000/auth/token/login/',
          type: 'POST',
          data: {
            username: this.form.login,
            password: this.form.password
          },
          success: (response) => {
            sessionStorage.setItem('auth_token', response.auth_token);
            this.goMain();
          },
          error: (response) => {
            this.$emit('closeColorProgressbar');
            if (response.status === 400) {
              this.openAlertSnackbar('Login or password incorrect');
            } else {
              this.openAlertSnackbar(Object.values(response.responseJSON)[0][0]);
            }
          }
        })
      },
      openAlertSnackbar(snack_mes) {
        this.snackbar = true;
        this.snackbar_message = snack_mes;
        setTimeout(() => {
          this.snackbar = false;
        }, this.timeout);
      },
      goMain() {
        this.$emit('goMain');
        this.$emit('openColorSnackbar', this.snack_mes_logged);
        this.$emit('closeColorProgressbar');
      },
      goRegistration() {
        this.$emit('goRegistration');
      }
    }
  }
</script>

<style scoped>
  .mu-demo-form {
    width: 100%;
    max-width: 500px;
  }

  a {
    cursor: pointer;
  }
</style>

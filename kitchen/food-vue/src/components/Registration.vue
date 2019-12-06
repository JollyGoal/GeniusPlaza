<template>
  <mu-flex justify-content="center" fill style="text-align: left; margin-top: 20px;">
    <mu-form ref="form" :model="validateForm" class="mu-demo-form">
      <mu-container justify-content="center" style="padding-left: 20px;">
        <br>
        <h1 style="text-align: center;">Sign Up</h1>
        <mu-form-item style="width: 60%" label="Email" help-text="Email address length must not be greater than 150"
                      prop="email"
                      :rules="emailRules">
          <mu-text-field v-model="validateForm.email" prop="email"></mu-text-field>
        </mu-form-item>
        <br>
        <mu-form-item style="width: 60%" label="Name" help-text="First name length must not be greater than 150"
                      prop="first_name"
                      :rules="usernameRules">
          <mu-text-field v-model="validateForm.first_name" prop="first_name"></mu-text-field>
        </mu-form-item>
        <br>
        <mu-form-item style="width: 60%" label="Surname" help-text="Last name length must not be greater than 150"
                      prop="last_name"
                      :rules="usernameRules">
          <mu-text-field v-model="validateForm.last_name" prop="last_name"></mu-text-field>
        </mu-form-item>
        <br>
        <mu-form-item style="width: 60%" label="Username" help-text="Username length must not be greater than 150"
                      prop="username"
                      :rules="usernameRules">
          <mu-text-field v-model="validateForm.username" prop="username"></mu-text-field>
        </mu-form-item>
        <br>
        <mu-form-item style="width: 60%" label="Password" prop="password" :rules="passwordRules">
          <mu-text-field type="password" v-model="validateForm.password" prop="password"
                         :action-icon="visibility ? 'visibility_off' : 'visibility'"
                         :action-click="() => (visibility = !visibility)"
                         :type="visibility ? 'text' : 'password'"></mu-text-field>
          <span style="margin-top: 10px; font-size: 12px; font-weight: 400;">
            <ul>
              <li>Your password must contain at least 8 characters.</li>
              <li>Your password shouldn't be too similar to your username.</li>
              <li>Your password shouldn't be a commonly used password.</li>
            </ul>
          </span>
        </mu-form-item>
        <br>
        <mu-form-item>
          <mu-button color="primary" @click="submit">submit</mu-button>
          <mu-button @click="clear">reset</mu-button>
        </mu-form-item>
      </mu-container>
    </mu-form>
    <mu-snackbar position='top-start' color="error" :open.sync="snackbar">
      <mu-icon left value="error"></mu-icon>
      {{snackbar_message}}
      <mu-button flat slot="action" color="#fff" @click="snackbar = false">Close</mu-button>
    </mu-snackbar>

  </mu-flex>

</template>

<script>
  import $ from 'jquery';

  export default {
    data() {
      return {
        usernameRules: [
          {validate: (val) => !!val, message: 'This field must be filled in'},
          {validate: (val) => val.length <= 150, message: 'Username length must not be greater than 150'}
        ],
        emailRules: [
          {validate: (val) => !!val, message: 'Email address must be filled in'},
          {validate: (val) => val.length <= 250, message: 'Email address length must not be greater than 250'}
        ],
        passwordRules: [
          {validate: (val) => !!val, message: 'Password must be filled in'},
          {
            validate: (val) => val.length >= 8 && val.length <= 150,
            message: ' '
          }
        ],
        validateForm: {
          username: '',
          password: '',
          email: '',
          first_name: '',
          last_name: '',
        },
        visibility: false,
        snack_mes_registered: 'Welcome to my website!',
        timeout: 3000,
        snackbar: false,
        snackbar_message: '',
      }
    },
    methods: {
      submit() {
        this.$refs.form.validate().then((result) => {
          console.log('form valid: ', result);
          if (result) {
            this.$emit('openColorProgressbar');
            $.ajax({
              url: 'http://localhost:8000/api/register/',
              type: 'POST',
              data: {
                username: this.validateForm.username,
                password: this.validateForm.password,
                email: this.validateForm.email,
                first_name: this.validateForm.first_name,
                last_name: this.validateForm.last_name,
              },
              success: (response) => {
                $.ajax({
                  url: 'http://127.0.0.1:8000/auth/token/login/',
                  type: 'POST',
                  data: {
                    username: this.validateForm.username,
                    password: this.validateForm.password
                  },
                  success: (response) => {
                    sessionStorage.setItem('auth_token', response.auth_token);
                    this.goMain();
                  },
                  error: (response) => {
                    this.$emit('closeColorProgressbar');
                    console.log(response);
                    this.openAlertSnackbar(Object.values(response.responseJSON)[0][0]);
                  }
                })
              },
              error: (response) => {
                console.log(response);
                this.$emit('closeColorProgressbar');
                this.openAlertSnackbar(Object.values(response.responseJSON)[0][0]);
              }
            })
          }
        });
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
        this.$emit('auth');
        this.$emit('openColorSnackbar', this.snack_mes_registered);
        this.$emit('closeColorProgressbar');
      },
      clear() {
        this.$refs.form.clear();
        this.validateForm = {
          username: '',
          password: '',
        };
      }
    }
  };
</script>
<style>
  .mu-demo-form {
    width: 100%;
    max-width: 500px;
    background-color: #424242;
  }

</style>

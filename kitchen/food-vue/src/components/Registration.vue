<template>
  <mu-flex justify-content="center" fill style="text-align: left; margin-top: 20px;">
    <mu-form ref="form" :model="validateForm" class="mu-demo-form">
      <mu-container>
        <br>
        <h1 style="text-align: center;">Sign Up</h1>
        <mu-form-item label="Email" help-text="Email address length must not be greater than 150" prop="email"
                      :rules="emailRules">s
          <mu-text-field v-model="validateForm.email" prop="email"></mu-text-field>
        </mu-form-item>
        <br>
        <mu-form-item label="Username" help-text="Username length must not be greater than 150" prop="username"
                      :rules="usernameRules">
          <mu-text-field v-model="validateForm.username" prop="username"></mu-text-field>
        </mu-form-item>
        <br>
        <mu-form-item label="Password" prop="password" :rules="passwordRules">
          <mu-text-field type="password" v-model="validateForm.password" prop="password" :action-icon="visibility ? 'visibility_off' : 'visibility'" :action-click="() => (visibility = !visibility)" :type="visibility ? 'text' : 'password'"></mu-text-field>
          <span style="margin-top: 10px; font-size: 12px; font-weight: 400;">
            <ul>
              <li>Your password can't be too similar to your username.</li>
              <li>Your password must contain at least 8 characters.</li>
              <li>Your password can't be a commonly used password.</li>
              <li>Your password can't be entirely numeric.</li>
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
                    {validate: (val) => !!val, message: 'Username must be filled in'},
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
                },
                visibility: false,
                snack_mes_registered: 'Welcome to our website! We have sent you an email!',
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
                        $.ajax({
                            url: 'http://localhost:8000/api/register/',
                            type: 'POST',
                            data: {
                                username: this.validateForm.username,
                                password: this.validateForm.password,
                                email: this.validateForm.email,
                            },
                            success: (response) => {
                                console.log(response);
                                $.ajax({
                                    url: 'http://127.0.0.1:8000/api/register/',
                                    type: 'GET',
                                    data: {
                                        email: this.validateForm.email,
                                        username: this.validateForm.username,
                                    },
                                    success: (response) => {
                                        console.log(response)
                                    }
                                });
                                $.ajax({
                                    url: 'http://127.0.0.1:8000/auth/token/login/',
                                    type: 'POST',
                                    data: {
                                        username: this.validateForm.username,
                                        password: this.validateForm.password
                                    },
                                    success: (response) => {
                                        sessionStorage.setItem('auth_token', response.data.attributes.auth_token);
                                        this.goMain();
                                    },
                                    error: (response) => {
                                            console.log(response);
                                            this.openAlertSnackbar(response.responseJSON.errors['0']['detail']);
                                    }
                                })
                            },
                            error: (response) => {
                                console.log(response);
                                this.openAlertSnackbar(response.responseJSON.errors['0']['detail']);
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
    max-width: 460px;
    box-shadow: 3px 5px 6px #cccccc;
    background-color: #ffffff;
  }


</style>

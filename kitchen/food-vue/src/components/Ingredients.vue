<template>

</template>

<script>
  import $ from 'jquery'

  export default {
    name: "Ingredients",
    data() {
      return {
        nameRules: [
          {validate: (val) => !!val, message: 'Ingredient name must be filled in'},
          {validate: (val) => val.length <= 100, message: 'Ingredient name length must not be greater than 100'}
        ],
        priceRules: [
          {validate: (val) => !!val, message: 'Data must be filled in'},
          {validate: (val) => val > 0, message: 'Value can not be negative or zero'},
        ],
        ingredients: [],
        sort: {
          name: '',
          order: 'asc',
        },
        form: {
          name: '',
          price: '',
        },
        openSimple: false,
        snack_mes_added: 'Product was successfully ADDED!',
        columns: [
          {title: 'Name', name: 'name'},
          {title: 'Price $', name: 'price', align: 'center', sortable: true},
        ],
        snackbar_message: '',
        snackbar: false,
      }
    },
    created() {
      $.ajaxSetup({
        headers: {
          'Authorization': 'Token ' + sessionStorage.getItem('auth_token')
        },
      });
      this.loadIngredients();
    },
    methods: {
      loadIngredients() {
        this.$emit('openColorProgressbar');
        $.ajax({
          url: 'http://localhost:8000/api/ingredients/',
          type: 'GET',
          success: (response) => {
            this.$emit('closeColorProgressbar');
            this.ingredients = response.data;
            console.log(response.data);
          },
          error: (response) => {
            this.$emit('closeColorProgressbar');
            console.log(response);
            this.openAlertSnackbar(Object.values(response.responseJSON)[0][0]);
          }
        })
      },
      AddIngredient() {
        this.$refs.form.validate().then((result) => {
          console.log('form valid: ', result);
          if (result) {
            this.$emit('openColorProgressbar');
            $.ajax({
              url: 'http://localhost:8000/api/ingredients/',
              type: 'POST',
              data: {
                name: this.form.name,
                price: this.form.price,
              },
              success: (response) => {
                this.$emit('closeColorProgressbar');
                this.loadIngredients();
                this.closeSimpleDialog();
                this.$emit('openColorSnackbar', this.snack_mes_added);
              },
              error: (response) => {
                this.$emit('closeColorProgressbar');
                this.closeSimpleDialog();
                this.openAlertSnackbar(Object.values(response.responseJSON)[0][0]);
              }
            });
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
      openSimpleDialog() {
        this.openSimple = true;
      },
      closeSimpleDialog() {
        this.openSimple = false;
      },
      handleSortChange({name, order}) {
        this.ingredients = this.ingredients.sort((a, b) => order === 'asc' ? a[name] - b[name] : b[name] - a[name]);
      },
    },
  }
</script>

<style scoped>

</style>

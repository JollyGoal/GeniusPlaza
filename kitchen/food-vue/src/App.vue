<template>
  <div id="app">
    <link rel="stylesheet" href="https://cdn.bootcss.com/material-design-icons/3.0.1/iconfont/material-icons.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700,400italic">
    <router-view/>
  </div>
</template>

<script>
import theme from 'muse-ui/lib/theme';


theme.add('teal', {
  primary: '#1976d2',
  secondary: '#ff4081',
  success: '#4caf50',
  warning: '#fdd835',
  info: '#2196f3',
  error: '#f44336',
  track: '#757575',
  text: {
    primary: '#fff',
    secondary: 'rgba(255, 255, 255, 0.7)',
    alternate: '#303030',
    disabled: 'rgba(255, 255, 255, 0.3)',
    hint: 'rgba(255, 255, 255, 0.3)'
  },
  divider: 'rgba(255, 255, 255, 0.3)',
  background: {
    paper: '#424242',
    chip: '#616161',
    default: '#303030',
  },
}, 'dark');

theme.use('dark');
export default {
  name: 'App'
}
</script>

<style>
  #id {
    background-color: #303030;
  }
</style>

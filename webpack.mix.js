// webpack.mix.js
let mix = require('laravel-mix');

mix.sass('resources/scss/styles.scss', 'static/css/styles.min.css')

mix.js('resources/js/foundation.js', 'static/js');
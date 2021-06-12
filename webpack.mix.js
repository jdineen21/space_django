// webpack.mix.js
let mix = require('laravel-mix');

mix.copy('node_modules/motion-ui/dist/motion-ui.min.css', 'static/css');
mix.copy('node_modules/jquery/dist/jquery.min.js', 'static/js');

mix.sass('resources/assets/sass/foundation.scss', 'static/css');
mix.js('resources/assets/js/foundation.js', 'static/js');
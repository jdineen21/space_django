// // /**
// //  * First we will load all of this project's JavaScript dependencies which
// //  * includes React and other helpers. It's a great starting point while
// //  * building robust, powerful web applications using React + Laravel.
// //  */

// //require('./bootstrap');

import React from 'react';
import ReactDOM from 'react-dom';
import VerticalSlider from './VerticalSlider';
import 'react-responsive-carousel/lib/styles/carousel.min.css';

document.addEventListener('DOMContentLoaded', function() {
    if (document.getElementById('vertical_slider')) {
        ReactDOM.render(<VerticalSlider />, document.getElementById('vertical_slider'));
    }
});
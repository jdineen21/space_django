
// var active = 0;

// window.addEventListener('load', function() {
//     var container = document.getElementsByClassName("images")[0];
//     var flickr = document.getElementsByClassName("flickr_image");

//     var heights = [];
//     for (var i = 0; i < flickr.length; i++) {
//         heights.push(flickr[i].scrollHeight);
//     }

//     var max_height = Math.max(...heights);

//     console.log(max_height);

//     // Set container maxHeight to max_height
//     container.style.height = max_height+"px";

//     // Swap first max_height image to top
//     var i = heights.indexOf(max_height);
//     flickr[i].parentNode.insertBefore(flickr[i], flickr[0]);

//     flickr[0].style.display = "block";
//     flickr[0].style.maxHeight = max_height+"px";
//     for (var i = 1; i < flickr.length; i++) {
//         flickr[i].style.display = "none";
//         flickr[i].style.maxHeight = max_height+"px";
//     }

//     //flickr[0].style.maxHeight = max_height+"px";
//     //flickr[0].style.display = "block";
//     // for (var i = 0; i < flickr.length; i++) {
//     //     flickr[i].style.minHeight = max_height;
//     // }

//     document.getElementById("up_arrow").addEventListener("click", function() {
//         console.log("up");
//     });

//     document.getElementById("down_arrow").addEventListener("click", function() {
//         console.log("down");
//         flickr[active].style.maxHeight = 0;
//         //flickr[active].style.display = "none";

//         active += 1;
//         if (active >= flickr.length) {
//             active = 0;
//         }

//         //flickr[active].style.display = "block";
//         flickr[active].style.maxHeight = max_height+"px";
//     });
// });
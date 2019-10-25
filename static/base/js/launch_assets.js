

window.addEventListener('load', function() {
    var container = document.getElementsByClassName("launch_assets")[0];
    var flickr = document.getElementsByClassName("flickr_image");

    var heights = [];
    for (var i = 0; i < flickr.length; i++) {
        heights.push(flickr[i].scrollHeight);
    }

    var max_height = Math.max(...heights);

    console.log(max_height);

    // Set container maxHeight to max_height
    container.style.maxHeight = max_height+"px";

    // Swap first max_height image to top
    var i = heights.indexOf(max_height);
    flickr[i].parentNode.insertBefore(flickr[i], flickr[0]);

    console.log(container.scroll.length = 835);
});
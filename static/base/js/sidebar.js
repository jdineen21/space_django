
hidden = true
function slideMenu(id) {
    if (hidden) {
        document.getElementById("sidebar").style.left = "0";
        // document.getElementById("content").style.paddingLeft = "10em";
        hidden = false;
    } else {
        document.getElementById("sidebar").style.left = "-10em";
        // document.getElementById("content").style.paddingLeft = "0";
        hidden = true;
    }
}
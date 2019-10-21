
hidden = true
function slideMenu(id) {
    if (hidden) {
        document.getElementById("dropdown").style.left = "0";
        document.getElementById("content").style.paddingLeft = "10em";
        hidden = false;
    } else {
        document.getElementById("dropdown").style.left = "-10em";
        document.getElementById("content").style.paddingLeft = "0";
        hidden = true;
    }
}
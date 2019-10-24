
var acc = document.getElementsByClassName("accordion");
var i;

console.log(acc);

document.addEventListener('DOMContentLoaded', function() {
    for (i = 0; i < acc.length; i++) {
        acc[i].addEventListener("click", function() {
            this.classList.toggle("active");
            var panel = this.nextElementSibling;
            if (panel.style.maxHeight) {
                panel.style.maxHeight = null;
            } else {
                panel.style.maxHeight = panel.scrollHeight + "px";
            } 
        });
    }
});

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
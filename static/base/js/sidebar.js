
var acc = document.getElementsByClassName("accordion");

document.addEventListener('DOMContentLoaded', function() {
    for (var i = 0; i < acc.length; i++) {
        acc[i].addEventListener("click", function() {
            var panel;

            this.classList.toggle("active");
            panel = this.nextElementSibling;
            if (panel.style.maxHeight) {
                panel.style.maxHeight = null;
            } else {
                panel.style.maxHeight = panel.scrollHeight + "px";
            }

            var act = document.getElementsByClassName("active");
            for (var i = 0; i < act.length; i++) {
                if (act[i] != this) {
                    panel = act[i].nextElementSibling;
                    if (panel.style.maxHeight) {
                        panel.style.maxHeight = null;
                    } else {
                        panel.style.maxHeight = panel.scrollHeight + "px";
                    }
                    act[i].classList.toggle("active");
                }
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
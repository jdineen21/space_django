
var acc = document.getElementsByClassName("accordion");

document.addEventListener('DOMContentLoaded', function() {
    var sidebar = document.getElementById("sidebar");
    var sidebarTransform = document.getElementById("sidebar").style.transform;

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
    
    hidden = true
    document.getElementById("menu_burger").addEventListener("click", function() {
        if (hidden) {
            sidebar.style.transform = "translateX(0)";
            // document.getElementById("content").style.paddingLeft = "10em";
            hidden = false;
        } else {
            sidebar.style.transform = sidebarTransform;
            // document.getElementById("content").style.paddingLeft = "0";
            hidden = true;
        }
    });
});
try {
    window.$ = window.jQuery = require('jquery');

    require('foundation-sites');

    $(function() {
        $(document).foundation();
    });

} catch (e) {}
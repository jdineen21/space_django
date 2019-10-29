document.addEventListener('DOMContentLoaded', function() {
    var i = new ol.interaction.MouseWheelZoom();
    
    if (document.getElementById('launchpad')) {
        var location = JSON.parse(document.getElementById('launchpad').textContent).location;
    }

    var oldFn = i.handleEvent;
    i.handleEvent = function(e) {
        var type = e.type;
        if (type !== "wheel" && type !== "wheel" ) {
            return true;
        }
        
        if (!e.originalEvent.ctrlKey) {
            return true
        }

        oldFn.call(this,e);
    }

    var baseLayer = new ol.layer.Tile({
        visible: true,
        preload: Infinity,
        source: new ol.source.BingMaps({
            // We need a key to get the layer from the provider. 
            // Sign in with Bing Maps and you will get your key (for free)
            key: 'Ap9VqFbJYRNkatdxt3KyzfJxXN_9GlfABRyX3k_JsQTkMQLfK_-AzDyJHI5nojyP',
            imagerySet: 'Aerial', // or 'Road', 'AerialWithLabels', etc.
            // use maxZoom 19 to see stretched tiles instead of the Bing Maps
            // "no photos at this zoom level" tiles
            maxZoom: 19
        })
    });
    
    var map = new ol.Map({ 
        interactions: ol.interaction.defaults({mouseWheelZoom: false}).extend([i]),
        layers: [baseLayer],
        target: 'map', 
        controls: ol.control.defaults({ 
            attributionOptions: /** @type {olx.control.AttributionOptions} */ ({
                collapsible: false
            })
        }),
        view: new ol.View({ 
            center: ol.proj.fromLonLat([location.longitude, location.latitude]),
            zoom: 15
        })
    });
});
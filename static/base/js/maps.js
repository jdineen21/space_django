document.addEventListener('DOMContentLoaded', function() {
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
        layers: [baseLayer],
        target: 'map', 
        controls: ol.control.defaults({ 
            attributionOptions: /** @type {olx.control.AttributionOptions} */ ({
                collapsible: false
            })
        }),
        view: new ol.View({ 
            center: ol.proj.fromLonLat([-120.610829, 34.632093]),
            zoom: 15
        })
    });
});
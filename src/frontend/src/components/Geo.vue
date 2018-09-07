<template>
    <div id="full_div">
        <div>
            <h3>Shanxi Province, China</h3>
        </div>
        <div id="map">
        <l-map style="height: 100%" :zoom="zoom" :center="center">
            <l-tile-layer :url="url" :attribution="attribution">
            </l-tile-layer>
            <l-geo-json :geojson="coors.geojson" :options="coors.options">
            </l-geo-json>
        </l-map>
        </div>
    </div>
</template>

<script>

	import Vue from 'vue';
	import { LMap, LTileLayer, LGeoJson } from 'vue2-leaflet';
	import {default as data} from "../assets/person_geo.js";
    import PopupContent from './PopupContent';

    function onEachFeature(feature, layer) {
      let popupContent = Vue.extend(PopupContent);
      let popup = new popupContent({ propsData: { type: feature.geometry.type, text: feature.properties.popupContent }});
      layer.bindPopup(popup.$mount().$el);
    }

	export default {
    	name: "shanxiMap",
		components: {
			LMap,
			LTileLayer,
            LGeoJson
		},
		data () {
			return {
				zoom: 7,
                center: [35.026413, 111.007530],
                url: 'https://api.tiles.mapbox.com/v4/mapbox.light/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWJvdWNoYXVkIiwiYSI6ImNpdTA5bWw1azAyZDIyeXBqOWkxOGJ1dnkifQ.qha33VjEDTqcHQbibgHw3w',
				attribution:'&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
                coors: {
					geojson: data.coords,
                    options: {
                      style: function (feature) {
                        return feature.properties && feature.properties.style;
                      },
                      onEachFeature: onEachFeature,
                      pointToLayer: function (feature, latlng) {
                        return L.circleMarker(latlng, {
                          radius: 8,
                          fillColor: "#ff7800",
                          color: "#000",
                          weight: 1,
                          opacity: 1,
                          fillOpacity: 0.8
                        });
                      }
                    }
                }
			}
		}
	}
</script>

<style>

    @import "../../node_modules/leaflet/dist/leaflet.css";

    #full_div {
        position: absolute;
        overflow-x: auto;
        top: 170px;
        right: 30px;
        left: 30px;
        bottom: 0;
        padding-left: 10px;
        padding-right: 10px;
    }

    #map {
        position: absolute;
        overflow-x: auto;
        top: 80px;
        right: 30px;
        left: 30px;
        bottom: 20px;
        border: 3px solid green;
    }

</style>
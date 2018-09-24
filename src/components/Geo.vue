<template>
    <div>
        <div id="map-window">
            <h3>Shanxi Province, China</h3>
            <div id="map">
                <l-map style="height: 100%" :zoom="zoom" :center="center">
                    <l-tile-layer :url="url" :attribution="attribution">
                    </l-tile-layer>
                    <l-geo-json :geojson="coors.geojson" :options="coors.options" >
                    </l-geo-json>
                </l-map>
            </div>
        </div>
        <div id="results-box">
            <div id="tableWrapper">
                <table class="table">
                    <tbody>
                    <tr v-for="(row, index) in pointData">
                        ayy lmoa
                    </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>

<script>

	import { LMap, LTileLayer, LGeoJson } from 'vue2-leaflet';
	import {default as data} from "../assets/person_geo.js";

    function pushData(f) {
    	let coords = [f.latlng.lng, f.latlng.lat];
    	let pt = findPoint(coords);
    	console.log(pt);
		}

	function onEachFeature(feature, layer) {
		layer.on({
          click: pushData
        });
	}

	function findPoint(coords) {
    	for (let i = 0; i < data.coords.features.length; i++) {
            if (coords === data.coords.features[i].geometry.coordinates) {
            	return data.coords.features[i];
            }
        }
        return "Hey"
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
						pointToLayer: function (feature, latlng) {
							return L.circleMarker(latlng, {
								radius: 8,
								fillColor: "#ff7800",
								color: "#000",
								weight: 1,
								opacity: 1,
								fillOpacity: 0.8
							});
						},
                        onEachFeature: onEachFeature
					}
				},
				pointData: []
			}
		},
		methods: {
			hello(coord) {
				alert(coord.geometry.type);
			}
		}
	}
</script>

<style>

    @import "../../node_modules/leaflet/dist/leaflet.css";

    #results-box {
        position: absolute;
        top: 950px;
        bottom: 20px;
        padding-left: 50px;
        padding-right: 50px;
    }

    #map-window {
        position: absolute;
        overflow-x: auto;
        top: 170px;
        right: 30px;
        left: 30px;
        bottom: 20px;
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
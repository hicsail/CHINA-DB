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
        <div id="filter-window">
            <b>Time range:</b>
            <div id="slider-window">
                <vue-slider v-model="sliderVals.value" v-bind="sliderVals">

                </vue-slider>
            </div>
        </div>
        <div id="results-box">
            <b>Results:</b>
            <li v-for="d in pointData">
                ayy lmoa
            </li>
        </div>
    </div>
</template>

<script>

	import { LMap, LTileLayer, LGeoJson } from 'vue2-leaflet';
    import vueSlider from 'vue-slider-component'
	import {default as data} from "../assets/geo.js";

	function findPoint(coords) {
		for (let i = 0; i < data.coords.features.length; i++) {
			if (coords[0] === data.coords.features[i].geometry.coordinates[0]
              && coords[1] === data.coords.features[i].geometry.coordinates[1]) {
				return data.coords.features[i];
			}
		}
	}

	export default {
		name: "shanxiMap",
		components: {
			LMap,
			LTileLayer,
			LGeoJson,
            vueSlider
		},
		data () {
			return {
				sliderVals:
                  {
                    min: 1600,
                    max: 1950,
                    value: [1600, 1600],
                    formatter: "{value}",
                    mergeFormatter: "{value1} ~ {value2}",
                    tooltip: "always",
                    enableCross: false
                  },
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
						onEachFeature: this.onEachFeature
					}
				},
				pointData: []
			}
		},
		methods: {
			hello(coord) {
				alert(coord.geometry.type);
			},
            onEachFeature(feature, layer) {
				layer.on({
                  click: this.pushData
                });
            },
            pushPoints(pt)
            {
            	this.pointData.push(pt);
            },
            pushData(f) {
              let coords = [f.latlng.lng, f.latlng.lat];
              let pt = findPoint(coords);
              this.pointData = [];
              this.pushPoints(pt)
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
        right: 300px;
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

    #filter-window {
        position: absolute;
        overflow-x: auto;
        top: 250px;
        right: 30px;
        left: 970px;
        bottom: 40px;
        padding-left: 10px;
        padding-right: 10px;
        border: 3px solid green;
    }

    #slider-window {
        position: absolute;
        top: 50px;
        left: 50px;
        right: 50px;
    }

</style>
<template>
    <div class = "container">
        <div class="row">
            <h3>Shanxi Province, China</h3>
            <div class="col-md-9">
                <div id="map" class="map">
                    <l-map style="height: 100%" :zoom="zoom" :center="center">
                        <l-tile-layer :url="url" :attribution="attribution">
                        </l-tile-layer>
                        <l-geo-json :geojson="coors.geojson" :options="coors.options" :visible="coors.visible">
                        </l-geo-json>
                    </l-map>
                </div>
            </div>
            <div class="col-md-3">
                <div id="filter-window" class="filter-window">
                    <vue-slider v-model="sliderVals.value" v-bind="sliderVals"></vue-slider>
                    <button v-on:click="coors.visible=!coors.visible">Filter</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

	import { LMap, LTileLayer, LGeoJson } from 'vue2-leaflet';
	import vueSlider from 'vue-slider-component'
	import {default as data} from "../assets/geo.js";
	import 'bootstrap/dist/css/bootstrap.css'
	import 'bootstrap-vue/dist/bootstrap-vue.css'

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
						max: 1910,
						value: [1600, 1910],
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
					options:
                      {
                        style: function (feature)
                        {
                          return feature.properties && feature.properties.style;
                        },
                        pointToLayer: this.filterByYear,
                        onEachFeature: this.onEachFeature,
                      },
                    visible: false
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
            filterByYear(feature, latlng)
            {
              let start_year = feature.properties.objects[0].time.start_year;
              if (start_year >= this.sliderVals.value[0] && start_year <= this.sliderVals.value[1])
              {
                return L.circleMarker(latlng, {
                  radius: 8,
                  fillColor: "#ff7800",
                  color: "#000",
                  weight: 1,
                  opacity: 1,
                  fillOpacity: 0.8
                });
              }
            },
			pushPoints(pt)
			{
				this.pointData.push(pt);
			},
			pushData(f) {
				let coords = [f.latlng.lng, f.latlng.lat];
				let pt = findPoint(coords);
				this.pointData = [];
				this.pushPoints(pt);
			},
			filtData()
			{
				console.log(this.sliderVals.value[0]);
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
        height: 600px;
        border: 3px solid green;
    }

    #filter-window {
        border: 3px solid green;
    }

</style>
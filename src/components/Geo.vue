<template>
    <div class = "container">
        <div class="row">
            <h3>Shanxi Province, China</h3>
            <div class="col-md-9">
                <div id="map" class="map">
                    <l-map style="height: 100%" :zoom="zoom" :center="center">
                        <l-tile-layer :url="url" :attribution="attribution"/>
                        <l-marker
                                v-for="marker in markers"
                                :key="marker.id"
                                :lat-lng="marker.position"
                                :visible="marker.visible"
                                :icon="icon"
                        />
                    </l-map>
                </div>
            </div>
            <div class="col-md-3">
                <div id="filter-window" class="filter-window">
                    <vue-slider v-model="sliderVals.value" v-bind="sliderVals"/>
                    <button v-on:click="filterData">Filter</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

	import { LMap, LTileLayer, LMarker, LIcon } from 'vue2-leaflet';
	import vueSlider from 'vue-slider-component'
	import {default as data} from "../assets/geo.js";
	import 'bootstrap/dist/css/bootstrap.css'
	import 'bootstrap-vue/dist/bootstrap-vue.css'
    import "leaflet/dist/leaflet.css"



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
			LMarker,
			vueSlider,
            LIcon
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
                icon: L.icon(
                  {
                    iconUrl: "static/images/marker-icon.png",
                    iconSize: [32, 37],
                    iconAnchor: [16, 37]
                  }),
				zoom: 7,
				center: [35.026413, 111.007530],
				url: 'https://api.tiles.mapbox.com/v4/mapbox.light/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWJvdWNoYXVkIiwiYSI6ImNpdTA5bWw1azAyZDIyeXBqOWkxOGJ1dnkifQ.qha33VjEDTqcHQbibgHw3w',
				attribution:'&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
				markers: [],
				pointData: []
			}
		},
		methods: {
			hello(coord) {
				alert(coord.geometry.type);
			},
			pushPoints(pt)
			{
				this.pointData.push(pt);
			},
            filterData()
            {
            	this.markers = [];

            	let yearLowerBound = this.sliderVals.value[0];
            	let yearUpperBound = this.sliderVals.value[1];
            	let featureArray = data.coords.features;

            	let ids = 0;

                for (let i = 0; i < featureArray.length; i++)
                {
                	let year = featureArray[i].properties.objects[0].time.start_year;
                	if (year > yearLowerBound && year < yearUpperBound)
                    {
                    	let newLon = featureArray[i].geometry.coordinates[0];
                    	let newLat = featureArray[i].geometry.coordinates[1];

                    	let newMarker =
                          {
                          	id: ids.toString(),
                    		position: [newLat, newLon],
                            visible: true
                          };
                    	this.markers.push(newMarker);
                    	ids++;
                    }
                }
                for ( let i = 0; i < this.markers.length; i++)
                {
                	console.log(this.markers[i]);
                }
            },
		}
	}
</script>

<style>

    @import "../../node_modules/leaflet/dist/leaflet.css";

    #map {
        height: 600px;
        border: 3px solid green;
    }

    #filter-window {
        border: 3px solid green;
    }

</style>
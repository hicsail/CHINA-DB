<template>
    <div class = "container">
        <div class="row">
            <h3>Shanxi Province, China</h3>
            <div class="col-md-9">
                <div id="map">
                    <l-map
                            style="height: 100%"
                            :zoom="zoom"
                            :center="center">
                        <l-tile-layer
                                :url="url"
                                :attribution="attribution"/>
                        <l-marker
                                v-for="marker in markers"
                                :key="marker.id"
                                :lat-lng="marker.position"
                                :visible="marker.visible"
                                :icon="icon"
                                @click="pushPoints(marker)"
                        />
                    </l-map>
                </div>
            </div>
            <div class="col-md-3">
                <b-form-group
                    label="Filter by:">
                        <b-form-checkbox
                                id="yearBox"
                                @change="indivShow.showYear = !indivShow.showYear"
                        >Year</b-form-checkbox>
                        <b-form-checkbox
                                id="titleBox"
                                @change="indivShow.showTitle = !indivShow.showTitle"
                        >Title</b-form-checkbox>
                </b-form-group>
                <b-form @submit="filterData">
                    <b-form-group
                        id="yearFilterSlider"
                        label="Filter by Year"
                        v-if="indivShow.showYear">
                        <vue-slider
                                v-model="filters.sliderVals.value"
                                v-bind="filters.sliderVals"
                        />
                    </b-form-group>
                    <b-form-group
                        id="titleFilter"
                        label="Filter by Name"
                        label-for="titleFilterBox"
                        v-if="indivShow.showTitle">
                        <b-form-input
                            id="titleFilterBox"
                            type="text"
                            v-model="filters.searchTitles"
                            placeholder="Name of individual">
                        </b-form-input>
                    </b-form-group>
                    <b-button type="submit" variant="primary">
                        Filter
                    </b-button>
                    <div>state: {{ indivShow.showYear }}</div>
                </b-form>
            </div>
        </div>
        <div class="row">
            <div class="col-md-12">
                <div id="results-box">
                    <li v-for="pt in renderedData">
                        <div class="row">
                            {{ pt }}
                        </div>
                    </li>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

	import { LMap, LTileLayer, LMarker, LIcon } from 'vue2-leaflet';
	import vueSlider from 'vue-slider-component'
	import {default as geoData} from "../assets/geo.js";
	import 'bootstrap/dist/css/bootstrap.css'
	import 'bootstrap-vue/dist/bootstrap-vue.css'
    import "leaflet/dist/leaflet.css"


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
				indivShow:
                  {
                  	showYear: false,
                    showTitle: false
                  },
				flags:
                  {
                  	yearFlag: false,
                    titleFlag: false
                  },
                filters:
                  {
                    sliderVals:
                      {
                        min: 1600,
                        max: 1930,
                        value: [1600, 1930],
                        formatter: "{value}",
                        mergeFormatter: "{value1} ~ {value2}",
                        tooltip: "always",
                        enableCross: false
                      },
                    searchTitles: ""
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
				pointData: {},
                renderedData: []
			}
		},
		methods: {
			hello(coord) {
				alert(coord.geometry.type);
			},
			pushPoints(pt)
			{
				// refresh renderedData
				this.renderedData = [];
				// push new data
				this.renderedData = this.pointData[pt.id];
			},
            filterData()
            {
            	/*
            	Loop over point data, display points that contain
            	 */
            	this.markers = [];
            	let newMarkerFlag = true;

            	let yearLowerBound = this.filters.sliderVals.value[0];
            	let yearUpperBound = this.filters.sliderVals.value[1];
            	let featureArray = geoData.coords.features;

                for (let i = 0; i < featureArray.length; i++)
                {
                	let dataArray = featureArray[i].properties.objects;
                	for (let j = 0; j < dataArray.length; j++)
                    {
                    	let pointId = featureArray[i].id;
                    	// TODO pass featureArray[i].properties.objects[j] to filterPoint() here
                    	let year = featureArray[i].properties.objects[j].time.start_year;
                    	// TODO replace this with a large filter method
                        if (year > yearLowerBound && year < yearUpperBound)
                        {
                        	if (newMarkerFlag)
                        	{

                              // create new entry in pointData dict for this point
                              this.pointData[pointId] = [];

                              let newLon = featureArray[i].geometry.coordinates[0];
                              let newLat = featureArray[i].geometry.coordinates[1];

                              let newMarker =
                                {
                                  id: pointId,
                                  position: [newLat, newLon],
                                  visible: true
                                };
                              this.markers.push(newMarker);
                              newMarkerFlag = false;
                            }

                            // push this data to entry in pointData
                            this.pointData[pointId].push(featureArray[i].properties.objects[j]);
                        }
                    }
                    newMarkerFlag = true;

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

    #results-box {
        border: 3px solid green;
    }

</style>
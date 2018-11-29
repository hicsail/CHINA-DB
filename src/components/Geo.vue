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
                <b-form>
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
                </b-form>
                <button v-on:click="filterData">
                    Filter
                </button>
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
			pushPoints(pt)
			{
				// refresh renderedData
				this.renderedData = [];
				// push new data
				this.renderedData = this.pointData[pt.id];
			},
            pushMarker(featureArrayEntry)
            {
              let pointId = featureArrayEntry.id;
              this.pointData[pointId] = [];

              let newLon = featureArrayEntry.geometry.coordinates[0];
              let newLat = featureArrayEntry.geometry.coordinates[1];

              let newMarker =
                {
                  id: pointId,
                  position: [newLat, newLon],
                  visible: true
                };

              this.markers.push(newMarker);
            },
            filterByYears(thisYear)
            {
              let yearLower = this.filters.sliderVals.value[0];
              let yearUpper = this.filters.sliderVals.value[1];

              if (thisYear > yearLower && thisYear < yearUpper)
              {
                return true;
              }

              return false;
            },
            filterByTitle(thisTitles)
            {
              for (let key in thisTitles)
              {
                if (thisTitles[key].includes(this.filters.searchTitles))
                {
                  return true;
                }
              }
              return false;
            },
            filterData()
            {
              this.markers = [];
              let newMarkerFlag = true;
              console.log("Hi");

              let featureArray = geoData.coords.features;

              for (let i = 0; i < featureArray.length; i++)
              {
                let dataArray = featureArray[i].properties.objects;

                // refresh newMarkerFlag
                newMarkerFlag = true;

                for (let j = 0; j < dataArray.length; j++)
                {
                  if (this.indivShow.showYear)
                  {
                    let thisYear = featureArray[i].properties.objects[j].time.start_year;

                    if (this.filterByYears(thisYear))
                    {
                      if (newMarkerFlag)
                      {
                        this.pushMarker(featureArray[i]);
                        newMarkerFlag = false;
                      }
                      this.pointData[featureArray[i].id].push(featureArray[i].properties.objects[j]);
                      continue;
                    }
                  }
                  if (this.indivShow.showTitle)
                  {
                    let thisTitles = featureArray[i].properties.objects[j].titles;

                    if (this.filterByTitle(thisTitles))
                    {
                      if (newMarkerFlag)
                      {
                        this.pushMarker(featureArray[i]);
                        newMarkerFlag = false;
                      }
                      this.pointData[featureArray[i].id].push(featureArray[i].properties.objects[j]);
                      continue;
                    }
                  }
                }
              }
            }
		}
	}
</script>

<style>

    @import "../../node_modules/leaflet/dist/leaflet.css";

    #map {
        height: 600px;
        border: 3px solid green;
    }

    #results-box {
        border: 3px solid green;
    }

</style>
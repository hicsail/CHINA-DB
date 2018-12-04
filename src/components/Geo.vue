<template>
    <!--<div class = "container">-->
    <div class="padding-sides">
        <div class="row padding">
            <div class="col-md-9 grey-text">
                <h3>Shanxi Province, China</h3>
            </div>
            <div class="col-md-3"></div>
        </div>


        <!---- MAP ----->
        <div class="row ">
            <!--<div class="container">-->
            <div class="col-md-12 padding-sides">
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
        </div>


        <!---- TITLES ----->
        <div class="row padding padding-sides">
            <div class="col-md-3" style="text-align: center; border:1px solid black;">Individuals</div>
            <div class="col-md-3" style="text-align: center; border:1px solid black;">Institutions</div>
            <div class="col-md-3" style="text-align: center; border:1px solid black;">Corporate Entities</div>
             <div class="col-md-3" style="text-align: center; border:1px solid black;">Events</div>
        </div>


        <div class="row padding">

            <!-- INDIVIDUALS -->
            <div class="col-md-3">
                <!-- year -->
                <div class="row padding center-button">
                    <b-form-group>
                        <button size="sm" class="btn btn-secondary center-button" id="yearBox"
                                v-on:click="indivShow.showYear = !indivShow.showYear"
                        >Year</button>
                    </b-form-group>
                </div>
                <b-form-group class="padding-top-heavy"
                        id="yearFilterSlider"
                        v-if="indivShow.showYear">
                    <vue-slider class="style-slider"
                            v-model="filters.sliderVals.value"
                            v-bind="filters.sliderVals"
                    />
                </b-form-group>

                <!-- title -->
                <div class="row padding center-button">
                    <b-form-group>
                        <button class="btn btn-secondary center-button" id="titleBox"
                                v-on:click="indivShow.showTitle = !indivShow.showTitle"
                        >Title</button>
                    </b-form-group>
                </div>
                <b-form-group
                        id="titleFilter"
                        label-for="titleFilterBox"
                        v-if="indivShow.showTitle">
                    <b-form-input
                            id="titleFilterBox"
                            size="sm"
                            type="text"
                            v-model="filters.searchTitles"
                            placeholder="Name of individual">
                    </b-form-input>
                </b-form-group>


                <!-- nationality -->
                <div class="row center-button">
                    <b-form-group>
                        <div class = "row padding">
                            <button class="btn btn-secondary center-button" id="nationalityBox"
                                    v-on:click="indivShow.showNationality = !indivShow.showNationality"
                            >Nationality</button>
                        </div>
                    </b-form-group>
                </div>
                <b-form-group
                        id="nationalityFilter"
                        label-for="nationalityFilterBox"
                        v-if="indivShow.showNationality">
                    <b-form-input
                            id="nationalityFilterBox"
                            size="sm"
                            type="text"
                            v-model="filters.searchNationality"
                            placeholder="Nationality of individual">
                    </b-form-input>
                </b-form-group>


                <!-- gender -->
                <div class="row center-button">
                    <b-form-group>
                        <div class = "row padding">
                            <button class="btn btn-secondary center-button" id="genderBox"
                                    v-on:click="indivShow.showGender = !indivShow.showGender"
                            >Gender</button>
                        </div>
                    </b-form-group>
                </div>
                <b-form-group
                        id="genderFilter"
                        label-for="genderFilterBox"
                        v-if="indivShow.showGender">
                    <b-form-input
                            id="genderFilterBox"
                            size="sm"
                            type="text"
                            v-model="filters.searchGender"
                            placeholder="Male or Female">
                    </b-form-input>
                </b-form-group>
            </div>

            <!-- INSTITUTIONS -->
           <div class="col-md-3">
               <b-form-group>
                   Institutions filter
               </b-form-group>
           </div>


            <!-- CORPORATE ENTITIES -->
            <div class="col-md-3">
                <b-form-group>
                        Corporate Entities filter
                </b-form-group>
            </div>

            <!-- EVENTS -->
            <div class="col-md-3">
                <b-form-group>
                    Events filter
                </b-form-group>
            </div>
        </div>


        <!-- SUBMIT BUTTON -->
        <div class="row center-button">
            <b-button v-if="selectedAFilter" class="btn blue" size="lg" v-on:click="filterData">
                Submit
            </b-button>
        </div>




        <!--<div v-if="submittedFilter" class="row padding">-->
            <!--<div class="col-md-12">-->
                <!--<div id="results-box">-->
                    <!--<li v-for="pt in renderedData">-->
                        <!--<div class="row">-->
                            <!--{{ pt }}-->
                        <!--</div>-->
                    <!--</li>-->
                <!--</div>-->
            <!--</div>-->
        <!--</div>-->
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
				individualsSelected: false,
                selected: null,
				indivShow:
                  {
                  	showYear: false,
                    showTitle: false,
                    showNationality: false,
                    showGender: false
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
                        enableCross: false,
                        bgStyle: {
                          "backgroundColor": "#fff",
                          "boxShadow": "inset 0.5px 0.5px 3px 1px rgba(0,0,0,.36)"
                        },
                        tooltipStyle: {
                          "backgroundColor": "#0033FF",
                          "borderColor": "#0033FF"
                        },
                        processStyle: {
                          "backgroundColor": '#0033FF'
                        }
                      },
                    searchTitles: "",
                    searchNationality: "",
                    searchGender: ""
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
                renderedData: [],
                selectedAFilter: false
			}
		},
		methods: {
			refresh()
            {
            	this.indivShow.showYear = false;
            	this.indivShow.showNationality = false;
            	this.indivShow.showGender = false;
            	this.indivShow.showTitle = false;

            },
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
                if (thisTitles[key].includes(this.filters.searchTitles.toLowerCase()))
                {
                  return true;
                }
              }
              return false;
            },
            filterByNationality(thisNationality)
            {
            	return (thisNationality === this.filters.searchNationality.toLowerCase());
            },
            filterByGender(thisGender)
            {
            	return (thisGender === this.filters.searchGender.toLowerCase());
            },
            checkIndivFilters(checks)
            {
                if (this.indivShow.showYear)
                {
                	if (!checks.years)
                    {
                    	return false;
                    }
                }
                if (this.indivShow.showTitle)
                {
                	if (!checks.title)
                    {
                    	return false;
                    }
                }
                if (this.indivShow.showNationality)
                {
                	if (!checks.nationality)
                    {
                    	return false;
                    }
                }
                if (this.indivShow.showGender)
                {
                	if (!checks.gender)
                    {
                    	return false;
                    }
                }
                return true;
            },
            buildIndivChecks(featureEntry)
            {
              let checks =
                {
                  "years": false,
                  "nationality": false,
                  "title": false,
                  "gender": false
                };

              if (this.indivShow.showYear)
              {
                if (this.filterByYears(featureEntry.time.start_year))
                {
                  checks.years = true;
                }
              }
              if (this.indivShow.showTitle)
              {
                if (this.filterByTitle(featureEntry.titles))
                {
                  checks.title = true;
                }
              }
              if (this.indivShow.showNationality)
              {
                if (this.filterByNationality(featureEntry.nationality))
                {
                  checks.nationality = true;
                }
              }
              if (this.indivShow.showGender)
              {
                if (this.filterByGender(featureEntry.gender))
                {
                  checks.gender = true;
                }
              }

              return checks;
            },
            filterData()
            {
              this.markers = [];
              let featureArray = geoData.coords.features;
              let newMarker = true;

              for (let i = 0; i < featureArray.length; i++)
              {
                let dataArray = featureArray[i].properties.objects;
                newMarker = true;

                for (let j = 0; j < dataArray.length; j++)
                {
                  if (this.selected === 'individuals')
                  {
                  	let checks = this.buildIndivChecks(featureArray[i].properties.objects[j]);

                  	if (this.checkIndivFilters(checks))
                    {
                    	if (newMarker)
                        {
                          this.pushMarker(featureArray[i]);
                          newMarker = false;
                        }
                        this.pointData[featureArray[i].id].push(featureArray[i].properties.objects[j]);
                    }
                  }
                  else if (this.selected === 'institutions')
                  {}
                  else if (this.selected === 'corporateEntities')
                  {}
                  else if (this.selected === 'events')
                  {}
                  else
                  {
                  	// no filter selected
                  	break;
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
        border: 3px solid #101010;
    }

    #results-box {
        border: 3px solid #101010;
    }

    .padding {
        padding-top: 10px;
        padding-bottom: 10px;
    }
    .padding-top-heavy {
        padding-top: 20px;
        padding-bottom: 10px;
    }

    .padding-sides {
        padding-left: 40px;
        padding-right: 40px;
    }


    .filter-text {
        font-size: 20px;
        text-align: center;
    }

    .center-button {
        width: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .grey-text {
        color: #101010;
    }


    .blue {
        background-color: #0033FF;
        color: #fff;
    }


</style>
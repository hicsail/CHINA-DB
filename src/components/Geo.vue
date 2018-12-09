<template>
    <!--<div class = "container">-->
    <div class="padding-sides">
        <div class="row padding">
            <div class="col-md-10 grey-text title-row">
                <h3>Shanxi Province, China</h3>
            </div>

            <div v-on:click="openOverlay = !openOverlay" class="filter-btn-flex filter-btn-border">
                <div class="col-md-0.5 grey-text" style="font-size:28px; margin-left: 10px; margin-right: 10px;">Filter</div>
                <div class="col-md-0.5 center-item" style="margin-right: 10px;">
                    <font-awesome-icon icon="bars" size="2x"></font-awesome-icon>
                </div>
            </div>

        </div>


        <!-- FILTER BOX OVERLAY -->
        <div v-if="openOverlay" class="overlay-top transparent-background padding">
            <b-container>
                <b-row >
                    <b-col cols="12">
                    </b-col>
                </b-row>

                <!--INDIVIDUALS -->
                <div class="row">

                    <div v-b-toggle.collapse1 class="row center-button drop-down-div"  v-on:click="individualsSelected = !individualsSelected" >
                        <div class="col-md-1 orange center-item align-middle">
                            <font-awesome-icon icon="male" size="2x"></font-awesome-icon>
                        </div>

                        <div class="col-md-9 drop-down-title-text">Individuals</div>
                        <div class="col-md-2 center-item">
                            <font-awesome-icon v-if="!individualsSelected" icon="chevron-down" class="grey" size="2x"></font-awesome-icon>
                            <font-awesome-icon v-if="individualsSelected" icon="chevron-up"  class="grey" size="2x"></font-awesome-icon>
                        </div>
                    </div>


                    <b-col cols="12">

                        <b-collapse id="collapse1" class="white-background grey-border">

                            <!-- year -->
                            <b-row class="padding-top-heavy">
                                <b-col cols="1" class="grey-text">Year</b-col>
                                <b-col cols="10">
                                    <b-form-group class="padding-top-heavy"
                                                  id="yearFilterSlider"
                                                  v-if="openOverlay && individualsSelected">
                                        <vue-slider class="style-slider"
                                                    v-model="filters.sliderVals.value"
                                                    v-bind="filters.sliderVals"
                                        />
                                    </b-form-group>
                                </b-col>
                                <b-col cols="1"></b-col>
                            </b-row>


                            <!-- title and nationality-->
                            <b-row class="padding-small">
                                <b-col cols="2" class="grey-text">Name</b-col>
                                <b-col cols="4">
                                    <b-form-group
                                            style="align-items: left"
                                            id="titleFilter"
                                            label-for="titleFilterBox">
                                        <b-form-input
                                                id="titleFilterBox"
                                                size="sm"
                                                type="text"
                                                v-model="filters.searchTitles"
                                                placeholder="">
                                        </b-form-input>
                                    </b-form-group>
                                </b-col>

                                <b-col cols="2" class="grey-text">Nationality</b-col>
                                <b-col cols="4">
                                    <b-form-group
                                            id="nationalityFilter"
                                            label-for="nationalityFilterBox">
                                        <b-form-input
                                                id="nationalityFilterBox"
                                                size="sm"
                                                type="text"
                                                v-model="filters.searchNationality"
                                                placeholder="">
                                        </b-form-input>
                                    </b-form-group>
                                </b-col>

                            </b-row>


                            <!-- gender and location-->
                            <b-row class="padding-small">
                                <b-col cols="2" class="grey-text">Gender</b-col>
                                <b-col cols="4" class="grey-text">
                                    <b-form-radio-group id="btnRadios"
                                                        sz="sm"
                                                        button-variant="outline-secondary"
                                                        v-model="filters.searchGender"
                                                        stacked
                                                        :options="genderOptions"
                                    ></b-form-radio-group>
                                </b-col>

                                <b-col cols="2" class="grey-text">Location</b-col>
                                <b-col cols="4">
                                    <b-form-group
                                            id="locFilter"
                                            label-for="locFilterBox">
                                        <b-form-input
                                                id="locFilterBox"
                                                size="sm"
                                                type="text"
                                                v-model="filters.searchLocation"
                                                placeholder="name or type"
                                        >
                                        </b-form-input>
                                    </b-form-group>
                                </b-col>
                            </b-row>

                        </b-collapse>
                    </b-col>
                </div>


                <!-- INSTITUTIONS -->
                <div class="row padding-neg">

                    <div v-b-toggle.collapse2 class="row center-button drop-down-div"  v-on:click="institutionsSelected = !institutionsSelected" >
                        <div class="col-md-1 green center-item align-middle">
                            <font-awesome-icon icon="university" size="2x"></font-awesome-icon>
                        </div>
                        <div class="col-md-9 drop-down-title-text ">Institutions</div>
                        <div class="col-md-2 center-item">
                            <font-awesome-icon v-if="!institutionsSelected" icon="chevron-down" class="grey" size="2x"></font-awesome-icon>
                            <font-awesome-icon v-if="institutionsSelected" icon="chevron-up"  class="grey" size="2x"></font-awesome-icon>
                        </div>
                    </div>


                    <b-col cols="12">

                        <b-collapse id="collapse2" class="white-background grey-border">

                            <!-- year -->
                            <b-row class="padding-top-heavy">
                                <b-col cols="1" class="grey-text">Year</b-col>
                                <b-col cols="10" class="grey-text">
                                    TODO
                                </b-col>
                            </b-row>


                            <!-- title and nationality-->
                            <b-row class="padding-small">
                                <b-col cols="2" class="grey-text">Name</b-col>
                                <b-col cols="4" class="grey-text">
                                    TODO
                                </b-col>

                                <b-col cols="2" class="grey-text">Nationality</b-col>
                                <b-col cols="4" class="grey-text">
                                    TODO
                                </b-col>
                            </b-row>


                            <!-- gender and location-->
                            <b-row class="padding-small">
                                <b-col cols="2" class="grey-text">Type</b-col>
                                <b-col cols="4" class="grey-text">
                                    TODO
                                </b-col>

                                <b-col cols="2" class="grey-text">Location</b-col>
                                <b-col cols="4" class="grey-text">
                                    TODO
                                </b-col>
                            </b-row>
                        </b-collapse>
                    </b-col>
                </div>


                <!-- CORPORATE ENTITIES -->
                <div class="row padding-neg">

                    <div v-b-toggle.collapse3 class="row center-button drop-down-div"  v-on:click="corporateEntitiesSelected = !corporateEntitiesSelected" >
                        <div class="col-md-1 pink center-item align-middle">
                            <font-awesome-icon icon="building" size="2x"></font-awesome-icon>
                        </div>
                        <div class="col-md-9 drop-down-title-text">Corporate Entities</div>
                        <div class="col-md-2 center-item">
                            <font-awesome-icon v-if="!corporateEntitiesSelected" icon="chevron-down" class="grey" size="2x"></font-awesome-icon>
                            <font-awesome-icon v-if="corporateEntitiesSelected" icon="chevron-up"  class="grey" size="2x"></font-awesome-icon>
                        </div>
                    </div>
                    <b-col cols="12">


                        <b-collapse id="collapse3" class=" white-background grey-border">

                            <!-- year -->
                            <b-row class="padding-top-heavy">
                                <b-col cols="1" class="grey-text">Year</b-col>
                                <b-col cols="10" class="grey-text">
                                    TODO
                                </b-col>
                            </b-row>


                            <!-- title and nationality-->
                            <b-row class="padding-small">
                                <b-col cols="2" class="grey-text">Name</b-col>
                                <b-col cols="4" class="grey-text">
                                    TODO
                                </b-col>

                                <b-col cols="2" class="grey-text">Nationality</b-col>
                                <b-col cols="4" class="grey-text">
                                    TODO
                                </b-col>
                            </b-row>


                            <!-- gender and location-->
                            <b-row class="padding-small">
                                <b-col cols="2" class="grey-text">Type</b-col>
                                <b-col cols="4" class="grey-text">
                                    TODO
                                </b-col>

                                <b-col cols="2" class="grey-text">Location</b-col>
                                <b-col cols="4" class="grey-text">
                                    TODO
                                </b-col>
                            </b-row>
                        </b-collapse>
                    </b-col>
                </div>


                <!-- EVENTS -->
                <div class="row padding-neg">

                    <div v-b-toggle.collapse4 class="row center-button drop-down-div"  v-on:click="eventsSelected = !eventsSelected" >
                        <div class="col-md-1 purple center-item align-middle">
                            <font-awesome-icon icon="church" size="2x"></font-awesome-icon>
                        </div>
                        <div class="col-md-9 drop-down-title-text">Historical Events</div>
                        <div class="col-md-2 center-item">
                            <font-awesome-icon v-if="!eventsSelected" icon="chevron-down" class="grey" size="2x"></font-awesome-icon>
                            <font-awesome-icon v-if="eventsSelected" icon="chevron-up"  class="grey" size="2x"></font-awesome-icon>
                        </div>
                    </div>

                    <b-col cols="12">

                        <b-collapse id="collapse4" class="white-background grey-border">


                            <!-- year -->
                            <b-row class="padding-top-heavy">
                                <b-col cols="1" class="grey-text">Year</b-col>
                                <b-col cols="10" class="grey-text">
                                    TODO
                                </b-col>
                            </b-row>


                            <!-- title and nationality-->
                            <b-row class="padding-small">
                                <b-col cols="2" class="grey-text">Name</b-col>
                                <b-col cols="4" class="grey-text">
                                    TODO
                                </b-col>
                            </b-row>


                            <!-- gender and location-->
                            <b-row class="padding-small">
                                <b-col cols="2" class="grey-text">Type</b-col>
                                <b-col cols="4" class="grey-text">
                                    TODO
                                </b-col>

                                <b-col cols="2" class="grey-text">Location</b-col>
                                <b-col cols="4" class="grey-text">
                                    TODO
                                </b-col>
                            </b-row>
                        </b-collapse>
                    </b-col>
                </div>

                <!-- SUBMIT - TODO -->
                <div class="row padding-neg">
                    <div v-b-toggle.collapse2 class="row blue center-button drop-down-div"  v-on:click="filterData">
                        Submit (TODO)
                    </div>
                </div>



            </b-container>
        </div>


        <!---- MAP ----->
        <div class="row overlay-bottom">
            <!--<div class="container">-->
            <div class="col-md-12 padding-sides">
                <div id="map" >
                    <l-map
                            style="height: 100%"
                            :zoom="zoom"
                            :z-index=1
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



    </div>
</template>




<script>

	import { LMap, LTileLayer, LMarker, LIcon, LLayerGroup, LPopup } from 'vue2-leaflet';
	import vueSlider from 'vue-slider-component'
	import {default as geoData} from "../assets/geo.js";
	import 'bootstrap/dist/css/bootstrap.css'
	import 'bootstrap-vue/dist/bootstrap-vue.css'
    import "leaflet/dist/leaflet.css"
    import LRectangle from "../../node_modules/vue2-leaflet/src/components/LRectangle.vue";

	export default {
		name: "shanxiMap",
		components: {
          LRectangle,
          LMap,
			LTileLayer,
			LMarker,
			vueSlider,
            LIcon,
            LLayerGroup,
            LPopup
		},
		data () {
			return {
			    openOverlay: false,
				individualsSelected: false,
                institutionsSelected: false,
                selected: null,
				indivShow:
                  {
                  	showYear: false,
                    showTitle: false,
                    showNationality: false,
                    showGender: false,
                    showLocation: false
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
                    searchGender: "Both",
                    searchLocation: ""
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
                selectedAFilter: false,
                genderOptions: [
                  {text: 'M', value: 'Men'},
                  {text: 'W', value: 'Women'},
                  {text: 'Both', value: 'Both'}
                ]
			}
		},
		methods: {
			refresh()
            {
            	this.indivShow.showYear = false;
            	this.indivShow.showNationality = false;
            	this.indivShow.showGender = false;
            	this.indivShow.showTitle = false;
            	this.indivShow.showLocation = false;
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

              return (thisYear > yearLower && thisYear < yearUpper);
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
            filterByLocation(thisLocationType, thisLocationName)
            {
            	return (thisLocationType === this.filters.searchLocation.toLowerCase()
                  || thisLocationName === this.filters.searchLocation.toLowerCase());
            },
            checkIndivFilters(checks)
            {
            	// TODO: hack, there's probably a better way to do this
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
                if (this.indivShow.showLocation)
                {
                	if (!checks.location)
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
                  "gender": false,
                  "location": false
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
              if (this.indivShow.showLocation)
              {
              	console.log(featureEntry.loc.location_type);
              	if (this.filterByLocation(featureEntry.loc.location_type, featureEntry.loc.location_name))
                {
                  checks.location = true;
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
                  if (this.individualsSelected)
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
            },
          openFilter() {
            console.log(this.$refs);
            this.$refs.popz.mapObject.openPopup([28.026413, 111.007530]);
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

    .overlay-top {

        position: absolute;
        z-index: 2000;
        left: 110px;
        top: 175px;
        color: white;
        width: 50%;
    }

    .overlay-bottom {
        position: absolute;
        width:100%;
        height:100%;
        z-index: 1;
    }

    .center-button {
        width: 100%;
        display: flex;
        justify-content: center;
    }

    .center-item {
        display: flex;
        align-items: center;
        justify-content: center;
    }


    .grey-text {
        color: #101010;
        text-align: left;
    }


    /* POP-UP WITH FILTER OPTIONS */

    .drop-down-div {
        border: 2px solid #D3D3D3;
        margin-left: 20px;
        margin-right: 20px;
        margin-top: -2px;
        background-color: white;
        line-height: 2;
    }

    .grey-border {
        border: 2px solid #D3D3D3;
        border-top: none;
        margin-left: 5px;
        margin-right: 5px;
        margin-top: 0px;
    }

    .white-background {
        background-color: white;
        margin-top: none;
        border-top: none;
    }

    .transparent-background {
        background-color: transparent;
    }

    .drop-down-title-text {
        color: #101010;
        text-align: left;
        font-size: 22px;
    }

    .grey {
        color: #D3D3D3;
    }

    .orange {
        background-color: #ff8000;
    }

    .pink {
        background-color: #ff0080;
    }

    .green {
        background-color: #009900;
    }

    .purple {
        background-color: #8000ff;
    }



    /* TITLE ROW WITH FILTER BUTTON */

    .title-row {
        margin-left: 25px;
    }

    .filter-btn-border {
        border: 2px solid #D3D3D3;
        margin-left: 5px;
        margin-right: 5px;
    }

    .filter-button .icon {
        vertical-align: middle;
        margin-right: 0.5rem;
    }
    .filter-button .icon:last-child {
        margin-right: 0;
    }

    .filter-btn-flex {
        display: flex;
    }


    /* PADDING TODO - rework layout to use less padding */

    .padding {
        padding-top: 10px;
        padding-bottom: 10px;
    }

    .padding-neg {
        padding-top: -20px;
        padding-bottom: -20px;
    }

    .padding-small {
        padding-top: 5px;
        padding-bottom: 5px;
    }
    .padding-top-heavy {
        padding-top: 17px;
        padding-bottom: 5px;
    }

    .padding-sides {
        padding-left: 40px;
        padding-right: 40px;
    }


    /* SUBMIT BUTTON */

    .blue {
        background-color: #0033FF;
        color: #fff;
    }


</style>


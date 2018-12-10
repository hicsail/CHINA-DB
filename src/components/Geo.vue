<template>
    <!--<div class = "container">-->
    <div class="padding-sides">
        <div class="row padding">
            <div class="col-md-8 grey-text title-row">
                <h3>Shanxi Province, China</h3>
            </div>

            <!-- FILTER BUTTON -->
            <div class="col-md-0.5 center-item" >
                <font-awesome-icon icon="filter" size="2x"></font-awesome-icon>
            </div>
            <div class="col-md-1=0.5 white-btn display-flex center-item" style="font-size:24px">Filter:</div>
            <div v-on:click="openOverlay = !openOverlay" class="display-flex center-item">
                <div v-if="openOverlay">
                    <div class="col-md-0.5 filter-btn-off-text"> Options </div>
                </div>
                <div v-if="!openOverlay">
                    <div class="col-md-0.5 filter-btn-on-text"> Options </div>
                </div>
            </div>
            <div class="col-md-0.5 display-flex center-item filter-btn-on-text" >|</div>
            <div class="display-flex center-item">
                <div v-if="openOverlay" v-on:click="filterData">
                    <div class="col-md-0.5 filter-btn-on-text"> Apply </div>
                </div>
                <div v-if="!openOverlay">
                    <div class="col-md-0.5 filter-btn-off-text"> Apply </div>
                </div>
            </div>
        </div>


        <!-- FILTER BOX OVERLAY -->
        <div v-if="openOverlay" class="overlay-top transparent-background padding">
            <b-container>

                <!--INDIVIDUALS -->
                <div class="row">

                    <div v-b-toggle.collapse1 class="row center-button drop-down-div"  v-on:click="individualsSelected = !individualsSelected" >
                        <div class="col-md-1 row-one-color center-item align-middle">
                            <font-awesome-icon icon="male" size="2x"></font-awesome-icon>
                        </div>

                        <div class="col-md-9 drop-down-title-text">Individuals</div>
                        <div class="col-md-2 center-item">
                            <font-awesome-icon v-if="!individualsSelected" icon="chevron-down" class="grey" size="2x"></font-awesome-icon>
                            <font-awesome-icon v-if="individualsSelected" icon="chevron-up"  class="grey" size="2x"></font-awesome-icon>
                        </div>
                    </div>


                    <div class="col-md-12">

                        <b-collapse id="collapse1" class="white-background grey-border">

                            <!-- year -->
                            <div class="row padding-top-only">
                                <div class="col-md-1" ></div>
                                <div class="col-md-10" >
                                    <b-form-group class="padding-top-only"
                                                  id="yearFilterSlider"
                                                  v-if="openOverlay && individualsSelected">
                                        <vue-slider class="style-slider"
                                                    v-model="filters.sliderVals.value"
                                                    v-bind="filters.sliderVals"
                                        />
                                    </b-form-group>
                                </div>
                                <div class="col-md-1" ></div>
                            </div>
                            <div class="row grey-text center-item padding-top-neg" >Years</div>


                            <!-- title and nationality-->
                            <div class="row padding-top-only">
                                <div class="col-md-1"></div>
                                <div class="col-md-4">
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
                                </div>
                                <div class="col-md-1"></div>
                                <div class="col-md-4">
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
                                </div>
                                <div class="col-md-1"></div>
                            </div>
                            <div class="row padding-neg">
                                <div class="col-md-1"></div>
                                <div class="col-md-4 grey-text" >Name</div>
                                <div class="col-md-1"></div>
                                <div class="col-md-4 grey-text">Nationality</div>
                                <div class="col-md-1"></div>
                            </div>

                            <!-- gender and location-->
                            <div class="row padding-top-only">
                                <div class="col-md-1"></div>
                                <div class="col-md-4">
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
                                </div>

                                <div class="col-md-6 grey-text left-item">
                                    <b-form-radio-group id="btnRadios"
                                                        sz="sm"
                                                        button-variant="outline-secondary"
                                                        v-model="filters.searchGender"
                                                        :options="genderOptions"
                                    ></b-form-radio-group>
                                </div>
                            </div>

                            <div class="row padding-bottom-only">
                                <div class="col-md-1"></div>
                                <div class="col-md-4 grey-text">Location</div>
                                <div class="col-md-1"></div>
                                <div class="col-md-4 grey-text">Gender</div>
                            </div>

                        </b-collapse>
                    </div>
                </div>


                <!-- INSTITUTIONS -->
                <div class="row padding-neg">

                    <div v-b-toggle.collapse2 class="row center-button drop-down-div"  v-on:click="institutionsSelected = !institutionsSelected" >
                        <div class="col-md-1 row-two-color center-item align-middle">
                            <font-awesome-icon icon="university" size="2x"></font-awesome-icon>
                        </div>
                        <div class="col-md-9 drop-down-title-text ">Institutions</div>
                        <div class="col-md-2 center-item">
                            <font-awesome-icon v-if="!institutionsSelected" icon="chevron-down" class="grey" size="2x"></font-awesome-icon>
                            <font-awesome-icon v-if="institutionsSelected" icon="chevron-up"  class="grey" size="2x"></font-awesome-icon>
                        </div>
                    </div>

                    <div class="col-md-12">
                        <b-collapse id="collapse2" class="white-background grey-border">
                            <div class="grey-text center-item">TODO</div>
                        </b-collapse>
                    </div>
                </div>


                <!-- CORPORATE ENTITIES -->
                <div class="row padding-neg">

                    <div v-b-toggle.collapse3 class="row center-button drop-down-div"  v-on:click="corporateEntitiesSelected = !corporateEntitiesSelected" >
                        <div class="col-md-1 row-three-color center-item align-middle">
                            <font-awesome-icon icon="building" size="2x"></font-awesome-icon>
                        </div>
                        <div class="col-md-9 drop-down-title-text">Corporate Entities</div>
                        <div class="col-md-2 center-item">
                            <font-awesome-icon v-if="!corporateEntitiesSelected" icon="chevron-down" class="grey" size="2x"></font-awesome-icon>
                            <font-awesome-icon v-if="corporateEntitiesSelected" icon="chevron-up"  class="grey" size="2x"></font-awesome-icon>
                        </div>
                    </div>
                    <div class="col-md-12">
                        <b-collapse id="collapse3" class=" white-background grey-border">
                           <div class="grey-text center-item">TODO</div>
                        </b-collapse>
                    </div>
                </div>


                <!-- EVENTS -->
                <div class="row padding-neg">

                    <div v-b-toggle.collapse4 class="row center-button drop-down-div"  v-on:click="eventsSelected = !eventsSelected" >
                        <div class="col-md-1 row-four-color center-item align-middle">
                            <font-awesome-icon icon="church" size="2x"></font-awesome-icon>
                        </div>
                        <div class="col-md-9 drop-down-title-text">Historical Events</div>
                        <div class="col-md-2 center-item">
                            <font-awesome-icon v-if="!eventsSelected" icon="chevron-down" class="grey" size="2x"></font-awesome-icon>
                            <font-awesome-icon v-if="eventsSelected" icon="chevron-up"  class="grey" size="2x"></font-awesome-icon>
                        </div>
                    </div>

                    <div class="col-md-12">
                        <b-collapse id="collapse4" class="white-background grey-border">
                            <div class="grey-text center-item">TODO</div>
                        </b-collapse>
                    </div>
                </div>

            </b-container>
        </div>


        <!---- MAP ----->
        <div class="row overlay-bottom">
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
                selected: null,
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
                openOverlay: false,
                individualsSelected: false,
                institutionsSelected: false,
                corporateEntitiesSelected: false,
                eventsSelected: false,
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
                this.openOverlay = false;
                this.individualsSelected = false;
                this.institutionsSelected = false;
                this.corporateEntitiesSelected = false;
                this.eventsSelected = false;
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

              console.log("FilterByYears - param is ", thisYear, " returning ", (thisYear > yearLower && thisYear < yearUpper));
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
              if (!checks.years && !checks.title &&
                !checks.nationality && !checks.gender && !checks.location)
              {
                return false;
              }

              return true;
            },
            buildIndivChecks(featureEntry)
            {
              console.log("BuildIndivChecks, featureEntry is ", featureEntry);
              let checks =
                {
                  "years": false,
                  "nationality": false,
                  "title": false,
                  "gender": false,
                  "location": false
                };

              console.log("time is ", featureEntry.time);
              console.log("start year is ", featureEntry.time.start_year);
              if (this.filterByYears(featureEntry.time.start_year))
              {
                checks.years = true;
              }
              if (this.filterByTitle(featureEntry.titles))
              {
                checks.title = true;
              }
              if (this.filterByNationality(featureEntry.nationality))
              {
                checks.nationality = true;
              }
              if (this.filterByGender(featureEntry.gender))
              {
                checks.gender = true;
              }
              if (this.filterByLocation(featureEntry.loc.location_type, featureEntry.loc.location_name))
              {
                checks.location = true;
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

    .left-item {
        display: flex;
        align-items: left;
        justify-content: flex-end;
    }


    .grey-text {
        color: #101010;
        text-align: left;
    }

    .light-grey-text {
        color: #D3D3D3;
        text-align: left;
    }

    .filter-btn-on-text {
        color: #101010;
        text-align: left;
        font-size: 24px;
    }

    .filter-btn-off-text {
        color: #D3D3D3;
        text-align: left;
        font-size: 24px;
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

    .row-one-color {
        background-color: #00CC99;
    }

    .row-two-color {
        background-color: #9933CC;
    }

    .row-three-color {
        background-color: #00CCCC;
    }

    .row-four-color {
        background-color: #FF9900;
    }


    /* TITLE ROW WITH FILTER BUTTON */
    .title-row {
        margin-left: 25px;
    }

    .filter-button .icon {
        vertical-align: middle;
        margin-right: 0.5rem;
    }
    .filter-button .icon:last-child {
        margin-right: 0;
    }

    .display-flex {
        display: flex;
    }


    /* SUBMIT ROW */

    .white-btn {
        color: #101010;
        text-align: left;
        font-size: 18px;
        margin-left: 10px;
        margin-right: 10px;
    }




    /* PADDING TODO - rework layout to use less padding */
    .form-group {
        margin-bottom: 0rem !important;
    }

    .padding {
        padding-top: 10px;
        padding-bottom: 10px;
    }

    .padding-neg {
        padding-top: -20px;
        padding-bottom: -20px;
    }

    .padding-top-neg {
        padding-top: -20px;
    }

    .padding-top-only {
        padding-top: 20px;
    }
    .padding-bottom-only {
        padding-bottom: 10px;
    }

    .padding-sides {
        padding-left: 40px;
        padding-right: 40px;
    }

    .blue {
        background-color: #0033FF;
        color: #fff;
    }


</style>


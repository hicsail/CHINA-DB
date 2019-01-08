<template>
    <div>
        <div class="row large-padding-top-and-bottom">
            <div class="col-md-8 my-auto grey-text padding-left"  >
                <h3>Shanxi Province, China</h3>
            </div>

            <div class="col-md-1 my-auto center-grey-text center-item">
                <div v-on:click="resetData()" class=" display-flex">
                    <div class="white-btn display-flex">Refresh</div>
                </div>
            </div>

            <div class="col-md-2 my-auto center-grey-text center-item" >
                <div v-on:click="openOverlay = !openOverlay" class=" display-flex">
                    <div class="white-btn display-flex">Filter</div>
                    <div class="display-flex">
                        <font-awesome-icon icon="filter" size="2x"></font-awesome-icon>
                    </div>
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

                               <Individuals
                                    :individualsSelected="individualsSelected"
                                    :openOverlay="openOverlay"
                                    :filters="filters"
                                    @individualLocationChanged="changeIndividualLocation"
                                    @individualYearChanged="changeIndividualYear"
                                    />

                            </b-collapse>
                         </div>
                    </div>


                <!-- INSTITUTIONS -->
                <!-- 1)type, 2)nationality, 3) religious family, 4) denomination, 5) name, and 6) where and when it existed. -->
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
            <div class="col-md-12 padding-left">
                <div id="map" >
                    <l-map
                            style="height: 100%"
                            :zoom="zoom"
                            :z-index=1
                            :center="center">
                        <l-tile-layer
                                :url="url"
                                :attribution="attribution"/>

                        <!-- TODO - drop pins with matching color/icon for institutions, entities, etc. -->
                        <l-marker
                                v-for="marker in markers"
                                :key="marker.id"
                                :lat-lng="marker.position"
                                :visible="marker.visible"
                                :icon="personDropPin"
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
    import Individuals from "./Individuals.vue";


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
            LPopup,
            Individuals
		},
      data: () => ({
          selected: null,
          orangeIcon: L.AwesomeMarkers.icon({
            prefix: 'fa',
            icon: 'male',
            markerColor: 'orange',
            iconColor: 'black'
          }),
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
              searchLocation: "",
            },
          personDropPin : L.AwesomeMarkers.icon({
            markerColor: 'green',
            prefix: 'fas fa-male',
            icon: 'male'
          }),
          zoom: 7,
          center: [35.026413, 111.007530],
          url: 'https://api.tiles.mapbox.com/v4/mapbox.light/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWJvdWNoYXVkIiwiYSI6ImNpdTA5bWw1azAyZDIyeXBqOWkxOGJ1dnkifQ.qha33VjEDTqcHQbibgHw3w',
          attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
          markers: [],
          pointData: {},
          renderedData: [],
          selectedAFilter: false,
          openOverlay: false,
          individualsSelected: false,
          institutionsSelected: false,
          corporateEntitiesSelected: false,
          eventsSelected: false
        }),
      beforeMount(){
        this.filterData();
      },

		methods: {
			refresh()
            {
                this.openOverlay = false;
                this.individualsSelected = false;
                this.institutionsSelected = false;
                this.corporateEntitiesSelected = false;
                this.eventsSelected = false;

                this.indivFilterYear = true;
                this.indivFilterTitle = false;
                this.indivFilterNationality = false;
                this.indivFilterGender = false;
                this.indivFilterLocation = false;

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

              //let type = featureArrayEntry.properties.objects[0].type;

              let pointId = featureArrayEntry.id;
              this.pointData[pointId] = [];

              let newLon = featureArrayEntry.geometry.coordinates[0];
              let newLat = featureArrayEntry.geometry.coordinates[1];

              let newMarker =
                {
                  id: pointId,
                  position: [newLat, newLon],
                  visible: true,
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
              // if user selected years,
                if (this.indivFilterYear)
                {
                  if (!checks.years)
                  {
                    return false;
                  }
                }
                if (this.indivFilterTitle)
                {
                  if (!checks.title)
                  {
                    return false;
                  }
                }
                if (this.indivFilterNationality)
                {
                  if (!checks.nationality)
                  {
                    return false;
                  }
                }
                if (this.indivFilterGender)
                {
                  if (!checks.gender)
                  {
                    return false;
                  }
                }
                if (this.indivFilterLocation)
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
              //console.log("featureEntry is ", featureEntry);
              let checks =
                {
                  "years": false,
                  "nationality": false,
                  "title": false,
                  "gender": false,
                  "location": false
                };

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
            resetData(){
                this.refresh();
            },
            changeIndividualLocation(newLocation){
              this.filters.searchLocation = newLocation;
              this.indivFilterLocation = true;
              this.filterData();
            },
            changeIndividualYear(newYears){
              this.filters.sliderVals.value = newYears;
              this.indivFilterYear = true;
              this.filterData();
            }
		}
	}
</script>



<style>

    /* TODO clean up CSS */

    @import "../../node_modules/leaflet/dist/leaflet.css";

    #map {
        height: 600px;
        border: 3px solid #101010;
    }

    .awesome-marker i {
        font-size: 18px;
        margin-top: 12px;
    }

    .overlay-top {

        position: absolute;
        z-index: 200;
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

    /* Colors match Leaflet.awesome-markers, so must be primary. */
    .row-one-color {
        background-color: green;
    }

    .row-two-color {
        background-color: purple;
    }

    .row-three-color {
        background-color: orange;
    }

    .row-four-color {
        background-color: blue;
    }


    /* TITLE ROW WITH FILTER BUTTON */

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
        font-size: 24px;
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

    .large-padding-top-and-bottom {
        padding-top: 20px;
        padding-bottom: 20px;
    }



</style>


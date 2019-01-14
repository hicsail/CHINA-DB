<template>
    <div>

        <!-- year  -->
        <div class="row padding-top-only">
            <div class="col-md-1" ></div>
            <div class="col-md-10" >
                <b-form-group class="padding-top-only"
                              id="yearFilterSliderInst"
                              v-if="openOverlay && institutionsSelected"
                >
                    <vue-slider class="style-slider"
                                v-model="filters.sliderVals.value"
                                v-bind="filters.sliderVals"
                    />
                </b-form-group>
            </div>
            <div class="col-md-1" ></div>
        </div>
        <div class="row grey-text center-item padding-top-neg" >Years</div>


        <!-- name and nationality-->
        <div class="row padding-top-only">
            <div class="col-md-1"></div>
            <div class="col-md-4">
                <b-form-group
                        style="align-items: left"
                        id="nameFilterInst"
                        label-for="nameFilterBoxInst">
                    <b-form-input
                            id="nameFilterBoxInst"
                            size="sm"
                            type="text"
                            v-model="filters.searchName"
                            placeholder="name">
                    </b-form-input>
                </b-form-group>
            </div>
            <div class="col-md-1"></div>
            <div class="col-md-4">
                <b-form-group
                        id="nationalityFilterInst"
                        label-for="nationalityFilterBoxInst">
                    <b-form-input
                            id="nationalityFilterBoxInst"
                            size="sm"
                            type="text"
                            v-model="filters.searchNationality"
                            placeholder="nationality">
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

        <!-- type and location-->
        <div class="row padding-top-only">
            <div class="col-md-1"></div>
            <div class="col-md-4">
                <b-form-group
                        id="locFilterInst"
                        label-for="locFilterBox">
                    <b-form-input
                            id="locFilterBoxInst"
                            size="sm"
                            type="text"
                            v-model="filters.searchLocation"
                            placeholder="name or type"
                    >
                    </b-form-input>
                </b-form-group>
            </div>

            <div class="col-md-1"></div>
            <div class="col-md-4">
                <b-form-group
                        id="typeFilterInst"
                        label-for="typeFilterBoxInst">
                    <b-form-input
                        id="typeFilterBoxInst"
                        size="sm"
                        type="text"
                        v-model="filters.searchType"
                        placeholder="institution type"
                    >
                    </b-form-input>
                </b-form-group>
            </div>
        </div>

        <div class="row padding-bottom-only">
            <div class="col-md-1"></div>
            <div class="col-md-4 grey-text">Location</div>
            <div class="col-md-1"></div>
            <div class="col-md-4 grey-text">Institution Type</div>
        </div>

        <!-- religious family and association-->
        <div class="row padding-top-only">
            <div class="col-md-1"></div>
            <div class="col-md-4">
                <b-form-group
                        id="religiousFamilyFilter"
                        label-for="religiousFamilyFilterBox">
                    <b-form-input
                            id="religiousFamilyFilterBox"
                            size="sm"
                            type="text"
                            v-model="filters.searchReligiousFam"
                            placeholder="name"
                    >
                    </b-form-input>
                </b-form-group>
            </div>

            <div class="col-md-1"></div>
            <div class="col-md-4">
                <b-form-group
                        id="associationFilterInst"
                        label-for="associationFilterBoxInst">
                    <b-form-input
                            id="associationFilterBoxInst"
                            size="sm"
                            type="text"
                            v-model="filters.searchAssociation"
                            placeholder="corporate entity name"
                    >
                    </b-form-input>
                </b-form-group>
            </div>
        </div>

        <div class="row padding-bottom-only">
            <div class="col-md-1"></div>
            <div class="col-md-4 grey-text">Religious Family</div>
            <div class="col-md-1"></div>
            <div class="col-md-4 grey-text">Association</div>
        </div>

        <div class="row padding-bottom-only center-item">
            <b-button size="small" variant="primary" v-on:click="submitInst(filters)">Submit</b-button>
        </div>

    </div>
</template>

<script>
	import vueSlider from 'vue-slider-component';

	export default {
		name: "Institutions",
        components: {
			vueSlider
        },
        data: () => ({
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
                searchLocation: "",
                searchNationality: "",
                searchAssociation: "",
                searchReligiousFam: "",
                searchName: "",
                searchType: ""
              }
        }),
        props: [
            'institutionsSelected',
            'openOverlay'
        ],
        methods: {
          submitInst(filters){

            // if 'true', user selected the filter attribute
            let attributesSelected = {
              "years": true,
              "nationality": false,
              "name": false,
              "type": false,
              "location": false,
              "association": false,
              "religious_family": false
            };

            if (filters.searchNationality !== ""){
              attributesSelected.nationality = true;
            }
            if (filters.searchName !== ""){
              attributesSelected.title = true;
            }
            if (filters.searchType !== ""){
              attributesSelected.gender = true;
            }
            if (filters.searchLocation !== ""){
              attributesSelected.location = true;
            }
            if (filters.searchAssociation !== ""){
              attributesSelected.association = true;
            }
            if (filters.searchReligiousFam !== ""){
              attributesSelected.religious_family = true;
            }

            let filterResults = { filters: filters, userSelections: attributesSelected};

            this.$emit('filterInstitutions', filterResults);
          },
          resetFiltersInst(){
            this.filters.sliderVals.values = [1600, 1930];
            this.filters.searchNationality = "";
            this.filters.searchName = "";
            this.filters.searchType = "";
            this.filters.searchLocation = "";
            this.filters.searchReligiousFam = "";
            this.filters.searchAssociation = "";
          }
        }
	}
</script>

<style>

    @import "../../node_modules/leaflet/dist/leaflet.css";

    .center-item {
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .grey-text {
        color: #101010;
        text-align: left;
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

</style>
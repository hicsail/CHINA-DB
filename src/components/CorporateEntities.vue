<!-- Shows corporate entity filter options and filtered markers. -->
<template>
    <div>

        <!-- year  -->
        <div class="row padding-top-only">
            <div class="col-md-1" ></div>
            <div class="col-md-10" >
                <b-form-group class="padding-top-only"
                              id="yearFilterSliderCorp"
                              v-if="openOverlay && corporateEntitiesSelected"
                              >
                    <vue-slider class="style-slider"
                                v-model="filtersCorp.sliderVals.value"
                                v-bind="filtersCorp.sliderVals"
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
                        id="nameFilterCorp"
                        label-for="nameFilterBoxCorp">
                    <b-form-input
                            id="nameFilterBoxCorp"
                            size="sm"
                            type="text"
                            v-model="filtersCorp.searchName"
                            placeholder="">
                    </b-form-input>
                </b-form-group>
            </div>
            <div class="col-md-1"></div>
            <div class="col-md-4">
                <b-form-group
                        id="nationalityFilterCorp"
                        label-for="nationalityFilterBoxCorp">
                    <b-form-input
                            id="nationalityFilterBoxCorp"
                            size="sm"
                            type="text"
                            v-model="filtersCorp.searchNationality"
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

        <!-- location and association-->
        <div class="row padding-top-only">
            <div class="col-md-1"></div>
            <div class="col-md-4">
                <b-form-group
                        id="locFilterCorp"
                        label-for="locFilterBoxCorp">
                    <b-form-input
                            id="locFilterBoxCorp"
                            size="sm"
                            type="text"
                            v-model="filtersCorp.searchLocation"
                            placeholder="name or type"
                    >
                    </b-form-input>
                </b-form-group>
            </div>
            <div class="col-md-1"></div>

            <div class="col-md-4">
                <b-form-group
                        id="assocFilterCorp"
                        label-for="assocFilterBoxCorp">
                    <b-form-input
                            id="assocFilterBoxCorp"
                            size="sm"
                            type="text"
                            v-model="filtersCorp.searchAssociation"
                    >
                    </b-form-input>
                </b-form-group>
            </div>
            <div class="col-md-1"></div>

        </div>

        <div class="row padding-bottom-only">
            <div class="col-md-1"></div>
            <div class="col-md-4 grey-text">Location</div>
            <div class="col-md-1"></div>
            <div class="col-md-4 grey-text">Association</div>
        </div>


        <div class="row padding-bottom-only center-item">
            <b-button size="small" variant="primary" v-on:click="submitCorp(filtersCorp)">Submit</b-button>
        </div>

    </div>
</template>

<script>
	import vueSlider from 'vue-slider-component';

    export default {
        name: 'CorporateEntities',
        components: {
            vueSlider
        },
        data: () => ({
          filtersCorp:
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
              searchName: "",
              searchNationality: "",
              searchLocation: "",
              searchInstitutionType: "",
              searchAssociation: "",
            }
        }),
        props: [
          'corporateEntitiesSelected',
          'openOverlay'
        ],
        methods: {
          submitCorp(filtersCorp){

            // if 'true', user selected the filter attribute
            let attributesSelected = {
                "years": true,
                "location": false,
                "nationality": false,
                "association": false,
                "name": false
            };

            if (filtersCorp.searchLocation !== ""){
              attributesSelected.location = true;
            }
            if (filtersCorp.searchNationality !== ""){
              attributesSelected.nationality = true;
            }
            if (filtersCorp.searchAssociation !== ""){
              attributesSelected.association = true;
            }
            if (filtersCorp.searchName !== ""){
              attributesSelected.name = true;
            }

            let filterResultsCorp = {
              filtersCorp: filtersCorp,
              userSelections: attributesSelected,
            clear:true};

            this.$emit('filterCorporateEntities', (filterResultsCorp, true));
          },
          resetFiltersCorp(){

            this.filtersCorp.sliderVals.values = [1600, 1930];
            this.filtersCorp.searchLocation= "";
            this.filtersCorp.searchNationality= "";
            this.filtersCorp.searchAssociation= "";
            this.filtersCorp.searchName= "";
          }
        }

    };
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

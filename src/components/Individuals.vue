<template>
    <div>

        <!-- year  -->
        <div class="row padding-top-only">
            <div class="col-md-1" ></div>
            <div class="col-md-10" >
                <b-form-group class="padding-top-only"
                              id="yearFilterSlider"
                              v-if="openOverlay && individualsSelected"
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

            <div class="col-md-6 grey-text" style="margin-left:40px">
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

    </div>
</template>

<script>
	import vueSlider from 'vue-slider-component';

    export default {
        name: 'Individuals',
        components: {
            vueSlider
        },
        data: () => ({
          genderOptions: [
            {text: 'M', value: 'Men'},
            {text: 'W', value: 'Women'},
            {text: 'Both', value: 'Both'}
          ]
        }),
        props: [
          'individualsSelected',
          'openOverlay',
          'filters'
        ],
        watch: {
            'filters.sliderVals.value': function(v) {
             this.$emit('individualYearChanged', this.filters.sliderVals.value);
            },
            'filters.searchLocation': function(v) {
              this.$emit('individualLocationChanged', this.filters.searchLocation);
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

    .form-group {
        margin-bottom: 0rem !important;
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

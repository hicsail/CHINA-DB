<!-- Shows all corp entity markers. -->
<template>
    <div>
    </div>
</template>

<script>

    export default {
        name: 'CorporateEntitiesOnLoad',
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
      created() {
        console.log("in CE - created.");

        EventBus.$on('showCorporateEntitiesOnLoad', () => {

            let attributesSelected = {
              "years": true,
              "nationality": false,
              "title": false,
              "gender": false,
              "location": false
            };

            let filterResultsCorp = {
              filtersCorp: this.filtersCorp,
              userSelections: attributesSelected,
              clear:false};
            this.$emit('filterCorporateEntities', filterResultsCorp);

        });
      }
    };
</script>



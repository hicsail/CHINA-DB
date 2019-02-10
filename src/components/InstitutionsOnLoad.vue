<!-- Shows all institution markers. -->
<template>
    <div></div>
</template>

<script>
  export default {
    name: 'IndividualsOnLoad',
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
    created() {

      EventBus.$on('showInstitutionsOnLoad', () => {

        let attributesSelected = {
          "years": true,
          "nationality": false,
          "name": false,
          "type": false,
          "location": false,
          "association": false,
          "religious_family": false
        };

        let filterResults = {
          filters: this.filters,
          userSelections: attributesSelected,
          clear:false};

        this.$emit('filterInstitutions', filterResults);
      });
    }
  }
</script>


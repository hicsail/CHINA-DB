
export const CorporateEntityFilterHelpers = {

  methods: {
    filterCorporateEntityHelper(filtersCorp, userSelections, featureArray)
    {

      let markerData={};
      let markersToPush = [];
      let markersAddedSoFar = [];

      //for each location (i)
      for (let i = 0; i < featureArray.length; i++)
      {

        let dataArray = featureArray[i].properties.corporate_entities;

        // for each object entry in location (i)
        for (let j = 0; j < dataArray.length; j++)
        {

          let uniqId = this.getUniqueIdCorp(featureArray[i], j);

          // check if any object attributes (time, loc, etc.) matches any filter
          let matches = this.dataMatchesFilterCorp(dataArray[j], filtersCorp, uniqId);

          // if user selected a filter that has matching attribute data
          if (this.userSelectedAndFilterMatchesCorp(matches, userSelections))
          {

            // if not added yet, add new marker
            if (markersAddedSoFar.indexOf(uniqId) === -1){
              markersAddedSoFar.push(uniqId);
              markerData=this.getMarkerDataCorp(featureArray[i], j);
              markersToPush.push(markerData);
            }
          }
        }
      }

      return markersToPush;
    },
    getMarkerDataCorp(featureArrayEntry, j, uniqId){
      let markerData={};
      markerData.id = uniqId;
      markerData.lon = featureArrayEntry.geometry.coordinates[0];
      markerData.lat = featureArrayEntry.geometry.coordinates[1];
      markerData.data = featureArrayEntry.properties.corporate_entities[j];
      return markerData;
    },
    getUniqueIdCorp(featureArrayEntry,j){
      let nationality = featureArrayEntry.properties.corporate_entities[j].nationality;
      let loc = featureArrayEntry.properties.corporate_entities[j].loc.location_name;
      let assoc = featureArrayEntry.properties.corporate_entities[j].corp_relations.association;
      return nationality + loc + assoc;
    },
    dataMatchesFilterCorp(featureEntry, filtersCorp) {
    /*
     *  Checks whether DB entry (featureEntry) matches any filter selection.
     *
     *  @param  featureEntry   Object  one DB entry for a corporate entity
     *  @param  filters        Object  filters set by user
     *  @return matches        Object  for each attribute (eg, 'years'),
     *                                  'true' if DB entry matches selection
     */


      // for each attribute, store whether the DB entry is a match
      let matches =
            {
              "years": false,
              "location": false,
              "nationality": false,
              "association": false,
              "name": false
            };

      // call helper methods to determine if DB entry matches each filter
      if (this.filterByYearsCorp(featureEntry.time.start_year, filtersCorp))
      {
        matches.years = true;
      }
      if (this.filterByLocationCorp(featureEntry.loc.location_name, featureEntry.loc.location_type, filtersCorp))
      {
        matches.title = true;
      }
      if (this.filterByNationalityCorp(featureEntry.nationality, filtersCorp))
      {
        matches.nationality = true;
      }
      if (this.filterByAssociationCorp(featureEntry.corp_relations.association, filtersCorp))
      {
        matches.association = true;
      }
      if (this.filterByNameCorp(featureEntry.name, filtersCorp))
      {
        matches.name = true;
      }

      return matches;
    },
    filterByYearsCorp(thisYear, filtersCorp)
    {

      let yearLower = filtersCorp.sliderVals.value[0];
      let yearUpper = filtersCorp.sliderVals.value[1];

      return (thisYear > yearLower && thisYear < yearUpper);
    },
    filterByLocationCorp(thisLocationName, thisLocationType, filtersCorp) {

      if (thisLocationType === filtersCorp.searchLocation.toLowerCase()
          || thisLocationName.includes(filtersCorp.searchLocation.toLowerCase())){
        return true;
      }

      return false;
    },
    filterByNationalityCorp(thisNationality, filtersCorp) {
      if (thisNationality.includes(filtersCorp.searchNationality.toLowerCase())){
        return true;
      }
      return false;
    },
    filterByAssociationCorp(thisAssociation, filtersCorp) {
      if (thisAssociation.includes(filtersCorp.searchAssociation.toLowerCase())){
        return true;
      }
      return false;
    },
    filterByNameCorp(thisName, filtersCorp) {
      if (thisName.includes(filtersCorp.searchName.toLowerCase())){
        return true;
      }
      return false;
    },
    userSelectedAndFilterMatchesCorp(matches, attributesSelected) {
      /*
       * For each attribute, return false if:
       *   1) user requested to filter based on that attribute, and
       *   2) the data does match the filter
       *
       *
       *   @param  matches            Object    for one DB entry, a map of attributes to booleans,
       *                                        eg: years:true - means this DB entry matches the filter
       *
       *   @param  attributesSelected Object    for one DB entry, a map of attributes to booleans,
       *                                        eg: years:true - means user filtered based on years
       *
       *   @return boolean                      true - DB entry matches all filters
       *                                        false - DB entry does not match at least one filter
       */

      if (attributesSelected.years)
      {
        if (!matches.years)
        {
          return false;
        }
      }
      if (attributesSelected.location)
      {
        if (!matches.location)
        {
          return false;
        }
      }
      if (attributesSelected.institution_type)
      {
        if (!matches.institution_type)
        {
          return false;
        }
      }
      if (attributesSelected.nationality)
      {
        if (!matches.nationality)
        {
          return false;
        }
      }
      if (attributesSelected.association)
      {
        if (!matches.association)
        {
          return false;
        }
      }
      if (attributesSelected.name)
      {
        if (!matches.name)
        {
          return false;
        }
      }
      return true;
    }
  }
}
export const InstitutionFilterHelpers = {

  methods: {
    filterInstitutionHelper(filters, userSelections, featureArray)
    {
      let markerData={};
      let markersToPush = [];
      let markersAddedSoFar = [];

      //for each location (i)
      for (let i = 0; i < featureArray.length; i++)
      {

        let dataArray = featureArray[i].properties.institutions;

        // for each object entry in location (i)
        for (let j = 0; j < dataArray.length; j++)
        {

          let uniqId = this.getUniqueIdInst(featureArray[i], j);

          // check if any object attributes (time, loc, etc.) matches any filter
          let matches = this.dataMatchesFilterInst(dataArray[j], filters, uniqId);

          // if user selected a filter that has matching attribute data
          if (this.userSelectedAndFilterMatchesInst(matches, userSelections))
          {

            // if not added yet, add new marker
            if (markersAddedSoFar.indexOf(uniqId) === -1){
              markersAddedSoFar.push(uniqId);
              markerData=this.getMarkerDataInst(featureArray[i], j);
              markersToPush.push(markerData);
            }
          }
        }
      }

      return markersToPush;
    },
    getMarkerDataInst(featureArrayEntry, j, uniqId){
      let markerData={};
      markerData.id = uniqId;
      markerData.lon = featureArrayEntry.geometry.coordinates[0];
      markerData.lat = featureArrayEntry.geometry.coordinates[1];
      markerData.data = featureArrayEntry.properties.institutions[j];
      return markerData;
    },
    getUniqueIdInst(featureArrayEntry,j){
      let name = featureArrayEntry.properties.institutions[j].name;
      let startName = featureArrayEntry.properties.institutions[j].start_year;
      let location = featureArrayEntry.properties.institutions[j].loc.location_name;
      return name + startName + location;
    },
    dataMatchesFilterInst(featureEntry, filters) {
      /*
       *  Checks whether DB entry (featureEntry) matches any filter selection.
       *
       *  @param  featureEntry   Object  one DB entry for a person
       *  @param  filters        Object  filters set by user
       *  @return matches        Object  for each attribute (eg, 'years'),
       *                                  'true' if DB entry matches selection
       */

      // for each attribute, store whether the DB entry is a match
      let matches =
            {
              "years": false,
              "nationality": false,
              "name": false,
              "type": false,
              "location": false,
              "association": false,
              "religious_family": false
            };

      // call helper methods to determine if DB entry matches each filter
      if (this.filterByYearsInst(featureEntry.time.start_year, filters))
      {
        matches.years = true;
      }
      if (this.filterByNationalityInst(featureEntry.nationality, filters))
      {
        matches.nationality = true;
      }
      if (this.filterByNameInst(featureEntry.name, filters))
      {
        matches.nationality = true;
      }
      if (this.filterByTypeInst(featureEntry.institution_type, filters))
      {
        matches.type = true;
      }
      if (this.filterByLocationInst(featureEntry.loc.location_name, featureEntry.loc.location_type, filters))
      {
        matches.title = true;
      }
      if (this.filterByAssociationInst(featureEntry.corp_relations.association, filters))
      {
        matches.association = true;
      }
      if (this.filterByReligiousFamilyInst(featureEntry.corp_relations.religious_family, filters))
      {
        matches.religion = true;
      }


      return matches;
    },
    filterByYearsInst(thisYear, filters)
    {

      let yearLower = filters.sliderVals.value[0];
      let yearUpper = filters.sliderVals.value[1];

      return (thisYear > yearLower && thisYear < yearUpper);
    },
    filterByNationalityInst(thisNationality, filters) {

      if (thisNationality.indexOf(filters.searchNationality) > -1){
        return true;
      }

      return false;
    },
    filterByNameInst(thisName, filters) {
      if (thisName.indexOf(filters.searchName) > -1){
        return true;
      }

      return false;
    },
    filterByTypeInst(thisType, filters) {
      if (thisType.indexOf(filters.searchType) > -1){
        return true;
      }

      return false;
    },
    filterByLocationInst(thisLocationType, thisLocationName, filters) {

      return (thisLocationType === filters.searchLocation.toLowerCase()
        || thisLocationName === filters.searchLocation.toLowerCase());
    },
    filterByAssociationInst(thisAssoc, filters) {
      if (thisAssoc.indexOf(filters.searchAssociation) > -1){
        return true;
      }

      return false;
    },
    filterByReligiousFamilyInst(thisReligion, filters) {
      if (thisReligion.indexOf(filters.searchReligiousFam) > -1){
        return true;
      }

      return false;
    },
    userSelectedAndFilterMatchesInst(matches, attributesSelected) {
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
      if (attributesSelected.nationality)
      {
        if (!matches.nationality)
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
      if (attributesSelected.type)
      {
        if (!matches.type)
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
      if (attributesSelected.association)
      {
        if (!matches.association)
        {
          return false;
        }
      }
      if (attributesSelected.religious_family)
      {
        if (!matches.religious_family)
        {
          return false;
        }
      }
      return true;
    }
  }
}
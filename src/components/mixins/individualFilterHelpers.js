
export const IndividualFilterHelpers = {

  methods: {
    filterIndividualHelper(filters, userSelections, featureArray)
    {
      let markerData={};
      let markersToPush = [];

      //for each location (i)
      for (let i = 0; i < featureArray.length; i++)
      {

        let dataArray = featureArray[i].properties.objects;

        // for each object entry in location (i)
        for (let j = 0; j < dataArray.length; j++)
        {
          // check if any object attributes (time, loc, etc.) matches any filter
          let matches = this.dataMatchesFilter(featureArray[i].properties.objects[j], filters);

          // if user selected a filter that has matching attribute data
          if (this.userSelectedAndFilterMatches(matches, userSelections))
          {
            //make a marker for match
            markerData=this.getMarkerData(featureArray[i], j);
            markersToPush.push(markerData);
          }
        }
      }

      return markersToPush;
    },
    getMarkerData(featureArrayEntry, j){
      let markerData={};
      markerData.id = featureArrayEntry.id;
      markerData.lon = featureArrayEntry.geometry.coordinates[0];
      markerData.lat = featureArrayEntry.geometry.coordinates[1];
      markerData.data = featureArrayEntry.properties.objects[j];
      return markerData;
    },
    dataMatchesFilter(featureEntry, filters) {
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
              "title": false,
              "gender": false,
              "location": false
            };

      // call helper methods to determine if DB entry matches each filter
      if (this.filterByYears(featureEntry.time.start_year, filters))
      {
        matches.years = true;
      }
      if (this.filterByTitle(featureEntry.titles, filters))
      {
        matches.title = true;
      }
      if (this.filterByNationality(featureEntry.nationality, filters))
      {
        matches.nationality = true;
      }
      if (this.filterByGender(featureEntry.gender, filters))
      {
        matches.gender = true;
      }
      if (this.filterByLocation(featureEntry.loc.location_type, featureEntry.loc.location_name, filters))
      {
        matches.location = true;
      }


      // if(featureEntry.titles.family_name_en.includes('lyons')){
      //   console.log("lyons matche: ", matches);
      // }


      return matches;
    },
    filterByYears(thisYear, filters)
    {

      let yearLower = filters.sliderVals.value[0];
      let yearUpper = filters.sliderVals.value[1];

      return (thisYear > yearLower && thisYear < yearUpper);
    },
    filterByTitle(thisTitles, filters) {

      if (filters.searchTitles === ''){
        return false;
      }

      for (let key in thisTitles)
      {
        if (thisTitles[key].includes(filters.searchTitles.toLowerCase()))
        {
          //console.log(thisTitles[key], " is in ", filters.searchTitles.toLowerCase());
          return true;
        }
      }
      return false;
    },
    filterByNationality(thisNationality, filters) {
      return (thisNationality === filters.searchNationality.toLowerCase());
    },
    filterByGender(thisGender, filters) {
      return (thisGender === filters.searchGender.toLowerCase());
    },
    filterByLocation(thisLocationType, thisLocationName, filters) {

      return (thisLocationType === filters.searchLocation.toLowerCase()
        || thisLocationName === filters.searchLocation.toLowerCase());
    },
    userSelectedAndFilterMatches(matches, attributesSelected) {
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
      if (attributesSelected.title)
      {
        if (!matches.title)
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
      if (attributesSelected.gender)
      {
        if (!matches.gender)
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
      return true;
    }
  }
}
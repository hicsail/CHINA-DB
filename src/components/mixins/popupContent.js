export const PopupContent = {
  methods: {
    getPopupContent(data){
      let type = data.properties.objects[0].type;
      if (type === 'person') {
        return this.getPopupIndividual(data.properties.objects[0])
      }

      //TODO popup content for other types besides 'person'
      return 'TODO';
    },
    getPopupIndividual(data){
      /*
       * @param  data  DB entry for one individual
       * @return       an HTML string to use as popup content
       */

      let start = '<div> <table> <tbody>';
      let name =  '<tr><td>' + data.titles.family_name_en + ', ' +
        data.titles.given_name_en + '</td></tr>';
      let name_py = '<tr><td>' + data.titles.family_name_py + ', ' +
        data.titles.given_name_py + '</td></tr>';
      let loc = '<tr><td>' + data.loc.location_name + '</td></tr>';
      let time = '<tr><td>' + data.time.birth_year + '-' + data.time.death_year + '</td></tr>';
      let end = '</tbody> </table> </div>'
      let popupContent = start + name + name_py + loc + time + end;
      popupContent = popupContent.replace(/, N\/A/g, '').replace(/N\/A-N\/A/g, '').replace(/N\/A/g, '');
      return popupContent;
    }
  }
}




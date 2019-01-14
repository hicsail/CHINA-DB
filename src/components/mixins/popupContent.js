export const PopupContent = {
  methods: {
    getPopupContent(data){
      let type = data.type;

      if (type === 'person') {
        return this.getPopupIndividual(data)
      }
      if (type === 'institution'){
        return this.getPopupInstitution(data);
      }
      if (type === 'corporate_entity'){
        return this.getPopupCorporateEntity(data);
      }

      return 'TODO';
    },
    getPopupIndividual(data){
      /*
       * @param  data  DB entry for one individual
       * @return       an HTML string to use as popup content
       */

      let lastName = this.capitalize(data.titles.family_name_en);
      let firstName = this.capitalize(data.titles.given_name_en);
      let sex = this.capitalize(data.gender);
      let origin = this.capitalize(data.nationality);
      let location = this.capitalize(data.loc.location_name);
      let inst = this.capitalize(data.institution_name);
      let relFam = this.capitalize(data.tradition.religious_family);
      let corpName = this.capitalize(data.tradition.association);

      let start = '<div><table><tbody>';
      let name = "<tr><td> Name: " + firstName + lastName + "</td></tr>";
      let gender = '<tr><td>Gender: ' + sex + '</td></tr>';
      let nationality = '<tr><td>Nationality: ' + origin + '</td></tr>';
			let startYear = "<tr><td>Start Year: " + data.time.start_year + "</td></tr>";
      let loc = '<tr><td>Location: ' + location + '</td></tr>';
      let time = '<tr><td>Lived: ' + data.time.birth_year + '-' + data.time.death_year + '</td></tr>';
			let instName = "<tr><td>Institution Name: " + inst +  "</td></tr>";
			let corp = "<tr><td>Corporate Entity: " + corpName + "</td></tr>";
			let rel = "<tr><td>Religious Family: " + relFam + "</td></tr>";
      let end = '</tbody></table> </div>';

      let popupContent = start + name + gender
				+ nationality + instName + startYear
				+ loc + time + instName
			  + corp + rel + end;
      popupContent = popupContent
				.replace(/, N\/A/g, '')
				.replace(/N\/A-N\/A/g, '')
				.replace(/N\/A/g, '');
      return popupContent;
    },
    getPopupInstitution(data){
      /*
       * @param  data  DB entry for one corporate entity
       * @return       an HTML string to use as popup content
       */

      let instName = this.capitalize(data.name);
      let location = this.capitalize(data.loc.location_name);
      let origin = this.capitalize(data.nationality);
      let religion = this.capitalize(data.corp_relations.religious_family);
      let association = 'Association: ' + this.capitalize(data.corp_relations.association);

      let start = '<div><table><tbody>';
      let name = '<tr><td>' + instName + '</td></tr>';
      let loc_and_time = '<tr><td>' + location + ', ' + data.time.start_year + '</td></tr>';
      let nationality = '<tr><td>' + origin + '</td></tr>';
      let relig = '<tr><td>' + religion + '</td></tr>';
      if (religion.indexOf('N/A') > -1){
        relig = '';
      }
      let assoc = '<tr><td>' + association + '</td></tr>';
      if (association.indexOf('N/A') > -1){
        assoc = '';
      }
      let end = '</tbody></table></div>';

      let popupContent = start + name + loc_and_time + nationality + relig + assoc + end;
      popupContent = popupContent
				.replace(/, N\/A/g, '')
				.replace(/N\/A-N\/A/g, '')
				.replace(/N\/A/g, '');
      return popupContent;
    },
    getPopupCorporateEntity(data){
      /*
       * @param  data  DB entry for one corporate entity
       * @return       an HTML string to use as popup content
       */

      let corpName = this.capitalize(data.name);
      let location = this.capitalize(data.loc.location_name);
      let origin = this.capitalize(data.nationality);
      let religion = this.capitalize(data.corp_relations.religious_family);
      let association = this.capitalize(data.corp_relations.association);
      let child_co = 'Child Company: ' + this.capitalize(data.child_inst_name);

      let start = '<div><table><tbody>';
      let name = '<tr><td>' + corpName + '</td></tr>';
      if (corpName.indexOf('N/A') > -1){
        name = '';
      }
      let loc_and_time = '<tr><td>' + location + ', ' + data.time.start_year + '</td></tr>';
      let nationality = '<tr><td>' + origin + '</td></tr>';
      let relig = '<tr><td>' + religion + '</td></tr>';
      let assoc = '<tr><td>' + association + '</td></tr>';
      let child = '<tr><td>' + child_co + '</td></tr>';

      let end = '</tbody></table></div>';

      let popupContent = start + name + loc_and_time + nationality + relig + assoc + child + end;
      popupContent = popupContent
				.replace(/, N\/A/g, '')
				.replace(/N\/A-N\/A/g, '')
				.replace(/N\/A/g, '');
      return popupContent;
    },
    capitalize(string){
      let capitalized = "";
      let words = string.split(" ");

      // capitalize each word in string (eg, "nettie m" => "Nettie M"),
      for (let i = 0; i < words.length; i++){
        capitalized += words[i].charAt(0).toUpperCase() + words[i].slice(1);
        if (i < words.length - 1){
          capitalized += " ";
        }
      }

      return capitalized;
    }
  }
};




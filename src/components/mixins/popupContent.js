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

      let start = "<div><table><tbody>";
      let name =
				"<tr><td> Name: "
				+ this.capitalize(data.titles.given_name_en)
				+ this.capitalize(data.titles.family_name_en)
				+ "</td></tr>";
      let gender =
				"<tr><td>Gender: "
				+ this.capitalize(data.gender)
				+ "</td></tr>";
      let nationality =
				"<tr><td>Nationality: "
				+ this.capitalize(data.nationality)
				+ "</td></tr>";
			let startYear =
				"<tr><td>Start Year: "
				+ data.time.start_year
				+ "</td></tr>";
      let loc =
				"<tr><td>Location: "
				+ this.capitalize(data.loc.location_name)
				+ "</td></tr>";
      let time =
				"<tr><td>Lived: "
				+ data.time.birth_year
				+ "-"
				+ data.time.death_year
				+ "</td></tr>";
			let instName =
				"<tr><td>Institution Name: "
				+ this.capitalize(data.institution_name)
				+ "</td></tr>";
			let corp =
				"<tr><td>Corporate Entity: "
				+ this.capitalize(data.tradition.association)
				+ "</td></tr>";
			let rel =
				"<tr><td>Religious Family: "
				+ this.capitalize(data.tradition.religious_family)
				+ "</td></tr>";
      let end =
				"</tbody></table> </div>";

      let popupContent =
				start + name + gender
				+ nationality + instName + startYear
				+ loc + time + instName
			  + corp + rel + end;

      return popupContent
				.replace(/, N\/A/g, '')
				.replace(/N\/A-N\/A/g, '')
				.replace(/N\/A/g, '');
    },
    getPopupInstitution(data){
      /*
       * @param  data  DB entry for one corporate entity
       * @return       an HTML string to use as popup content
       */

      let start = '<div><table><tbody>';
      let name =
				"<tr><td>"
				+ this.capitalize(data.name)
				+ "</td></tr>";
      let type =
				"<tr><td>Type: "
				+ this.capitalize(data.institution_type)
				+ "</td></tr>";
      let loc =
				"<tr><td>Location: "
				+ this.capitalize(data.loc.location_name)
				+ "</td></tr>";
      let time =
				"<tr><td>Start Year: "
				+ data.time.start_year
				+ "</td></tr>";
      let nationality =
				"<tr><td>Nationality: "
				+ this.capitalize(data.nationality)
				+ "</td></tr>";
      let relig = "Religious Family: ";
			if (!(this.capitalize(data.corp_relations.religious_family).indexOf('N/A') > -1))
			{
				relig =
					"<tr><td>Religious Family: "
					+ this.capitalize(data.corp_relations.religious_family)
					+ "</td></tr>";
			}
			let assoc = "Association: ";
      if (!(this.capitalize(data.corp_relations.association).indexOf('N/A') > -1))
      {
				assoc =
					"<tr><td>Association: "
					+ this.capitalize(data.corp_relations.association)
					+ "</td></tr>";
      }
      let end = "</tbody></table></div>";

      let popupContent = start + name + type
				+ loc + time + nationality
				+ relig + assoc + end;

      return popupContent
				.replace(/, N\/A/g, '')
				.replace(/N\/A-N\/A/g, '')
				.replace(/N\/A/g, '');
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




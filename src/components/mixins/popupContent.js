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

      let start = "<div><h5>INDIVIDUAL</h5><table><tbody>";
      let title = "Mr.";
      if (data.gender === "female"){
      	title = "Mrs."
			}

      let name =
				"<tr><td> Name: " + title + " "
				+ this.capitalize(data.titles.given_name_en)
				+ " " + this.allCaps(data.titles.family_name_en)
				 + " (" + data.titles.family_name_zh + " " + data.titles.given_name_zh + ")"
				+ "</td></tr>";
			let time =
						"<tr><td>Lived: "
						+ data.time.birth_year
						+ "-"
						+ data.time.death_year
						+ "</td></tr>";
      let gender =
				"<tr><td>Gender: "
				+ this.capitalize(data.gender)
				+ "</td></tr>";
      let nationality =
				"<tr><td>Nationality: "
				+ this.capitalize(data.nationality)
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
			let startYear =
						"<tr><td>Start Year: "
						+ data.time.start_year
						+ "</td></tr>";
			let endYear =
						"<tr><td>End Year: "
						// + data.time.end_year TODO
						+ "</td></tr>";
			let loc =
						"<tr><td>Location: "
						+ this.capitalize(data.loc.location_name)
						+ " (" + data.loc.location_name_zh + ")"
						+ "</td></tr>";

			let end =
						"</tbody></table> </div>";

      let popupContent =
				start + name + time + gender
				+ nationality + instName + corp
				+ rel	+ startYear + endYear
				+ loc + end;

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

      let start = '<div><h5>INSTITUTION</h5><table><tbody>';
      let name =
				"<tr><td>Name: "
				+ this.capitalize(data.name)
				+ " (" + data.name_zh + ")"
				+ "</td></tr>";
      let type =
				"<tr><td>Type: "
				+ this.capitalize(data.institution_type)
				+ "</td></tr>";
			let relig = "<tr><td>Religious Family: </td></tr>";
			if (!(this.capitalize(data.corp_relations.religious_family).indexOf('N/A') > -1))
			{
				relig =
					"<tr><td>Religious Family: "
					+ this.capitalize(data.corp_relations.religious_family)
					+ "</td></tr>";
			}
			let assoc = "<tr><td>Association:</td></tr> ";
			if (!(this.capitalize(data.corp_relations.association).indexOf('N/A') > -1))
			{
				assoc =
					"<tr><td>Association: "
					+ this.capitalize(data.corp_relations.association)
					+ "</td></tr>";
			}
			let nationality =
						"<tr><td>Nationality: "
						+ this.capitalize(data.nationality)
						+ "</td></tr>";
      let loc =
				"<tr><td>Location: "
				+ this.capitalize(data.loc.location_name)
				+ " (" + data.loc.location_name_zh + ")"
				+ "</td></tr>";
      let startYear =
				"<tr><td>Start Year: "
				+ data.time.start_year
				+ "</td></tr>";
			let endYear =
						"<tr><td>End Year: "
						// + data.time.end_year TODO new data will have this
						+ "</td></tr>";

      let end = "</tbody></table></div>";

      let popupContent = start + name + type
				+ relig + assoc + nationality
				+ loc + startYear + endYear + end;

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

      let start = "<div><table><tbody>";
      let name = "<tr><td>Corporate Name:</td></tr> ";
      if (!(this.capitalize(data.name).indexOf('N/A') > -1)) {
				name =
					"<tr><td>Corporate Name: "
					+ this.capitalize(data.name)
					+ "</td></tr>";
			}
      let loc = "<tr><td>Location: "
				+ this.capitalize(data.loc.location_name)
				+ ", "
				+ data.time.start_year
				+ "</td></tr>";
      let time =
				"<tr><td>Start Year: "
				+ data.time.start_year
				+ "</td></tr>";
			let nationality =
				"<tr><td>Nationality: "
				+ this.capitalize(data.nationality)
				+ "</td></tr>";
      let relig =
				"<tr><td>Religion :"
				+ this.capitalize(data.corp_relations.religious_family)
				+ "</td></tr>";
      let assoc =
				"<tr><td>Association: "
				+ this.capitalize(data.corp_relations.association)
				+ "</td></tr>";
      let child =
				"<tr><td>Institution Name: "
				+ this.capitalize(data.child_inst_name)
				+ "</td></tr>";
      let end = "</tbody></table></div>";

      let popupContent =
				start + name + loc
				+ time + nationality + relig
				+ assoc + child + end;

      return popupContent
				.replace(/, N\/A/g, '')
				.replace(/N\/A-N\/A/g, '')
				.replace(/N\/A/g, '');
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
    },
		allCaps(string){
    	let allCaps = "";
			for (let i = 0; i < string.length; i++){
				allCaps += string.charAt(i).toUpperCase();
			}
			return allCaps;
		}
  }
};




const Airtable = require('airtable');
const base = new Airtable({apiKey:'keyvkMlawNyw2WAHK'}).base("appgj7WMdGiUCbfuE");

export const InstitutionQueries = {
	methods: {
		personnelConnections(recId) {
			return new Promise(function(resolve, reject) {
				base('institution').find(recId, function(err, record) {
					if (err) {
						console.log(err);
						return;
					}

					let returnObj = [];

					let personOrgIds = record.get('person_organization');
					if (personOrgIds)
					{
						for (let i = 0; i < personOrgIds.length; i++)
						{

							let currentRel = {
								personName: "",
								personRole: ""
							};

							base('person_organization').find(personOrgIds[i], function(err, record) {
								if (err) {
									console.log(err);
									return;
								}

								let personId = record.get('person_id');
								base('person').find(personId[0], function(err, record) {
									if (err) {
										console.log(err);
										return;
									}

									let personName = record.get('given_name_en');
									let personLastName = record.get('family_name_en');
									currentRel.personName = personName + " " + personLastName;
								});

								let personRoleId = record.get('pers_role_id');
								base('person_organization_role').find(personRoleId[0], function(err, record) {
									if (err) {
										console.log(err);
										return;
									}

									let personRole = record.get('pers_org_role_en');
									if (personRole)
									{
										currentRel.personRole = personRole;
									}
								});

								returnObj.push(currentRel);
							});
						}
					}
					resolve({"data": returnObj});
				})
			})
		}
	}
};
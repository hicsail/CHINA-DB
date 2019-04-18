const Airtable = require('airtable');
const base = new Airtable({apiKey:'keyvkMlawNyw2WAHK'}).base("appgj7WMdGiUCbfuE");

export const IndividualQueries = {
	methods:
		{
			interpersonalConnections(recId) {
				return new Promise(function(resolve, reject) {
					base('person').find(recId, function (err, record) {
						if (err) {
							console.error(err);
							return;
						}

						// these relationships don't exist in the DB yet, returning an empty obj

						let returnObj = {
							children: "N/A",
							parents: "N/A",
							confessorTo: "N/A",
							confessorYear: "N/A"

						};
						resolve({"data": returnObj});
					});
				});
			},
			institutionalConnections(recId) {
				return new Promise(function(resolve, reject) {
					base('person').find(recId, function(err, record) {
						if (err) {
							console.error(err);
							return;
						}

						let returnObj = {
							institution: "N/A",
							institutionYear: "N/A",
							participationType: "N/A"
						};

						let personOrganizationIds = record.get('person_organization');
						base('person_organization').find(personOrganizationIds[0], function(err, record) {
							if (err) {
								console.log(err);
								return;
							}

							let startYear = record.get('start_year');
							if (startYear)
							{
								returnObj.institutionYear = startYear;
							}

							let instId = record.get('inst_id');
							if (instId)
							{
								base('institution').find(instId[0], function(err, record) {
									let instName = record.get('inst_name');
									if (instName)
									{
										returnObj.institution = instName;
									}
								})
							}
							else
							{
								resolve({"data": returnObj});
							}

							let relTypeId = record.get('pers_role_id');
							if (relTypeId)
							{
								base('person_organization_role').find(relTypeId[0], function(err, record) {
									if (err) {
										console.log(err);
										return;
									}

									let relType = record.get('pers_org_role_en');
									if (relType)
									{
										returnObj.participationType = relType;
									}
								});
							}
							resolve({"data": returnObj});
						})
					})
				})
			},
			corporateConnections(recId) {
				return new Promise(function(resolve, reject) {
					base('person_organization').find(recId, function(err, record) {
						if (err) {
							console.log(err);
							return;
						}

						let returnObj = {
							membership: "N/A",
							role: "N/A",
							time: "N/A"
						};

						let corpId = record.get('corp_id');
						if (corpId)
						{
							base('corporate_entity').find(corpId[0], function(err, record) {
								if (err) {
									console.log(err);
									return;
								}
								let corpName = record.get('corp_name_en');
								if (corpName)
								{
									returnObj.membership = corpName;
								}
							})
						}

						let corpRole = record.get('pers_role_id');
						if (corpRole)
						{
							base('person_organization_role').find(corpRole[0], function(err, record) {
								if (err) {
									console.log(err);
									return;
								}

								let roleName = record.get('pers_org_role_en');
								if (roleName)
								{
									returnObj.role = roleName;
								}
								else
								{
									returnObj.role = "Member";
								}
							})
						}

						let startYear = record.get('start_year');
						if (startYear)
						{
							returnObj.time = startYear;
						}

						resolve({"data": returnObj});
					})
				})
			}
		}
};

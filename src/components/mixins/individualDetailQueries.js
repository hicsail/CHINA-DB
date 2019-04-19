const Airtable = require('airtable');
const base = new Airtable({apiKey:'keyvkMlawNyw2WAHK'}).base("appgj7WMdGiUCbfuE");

export const IndividualQueries = {
	methods:
		{
			interpersonalConnections(recId) {
				return new Promise(function(resolve, reject) {

					let returnObj = [];

					base('person').find(recId, function (err, record) {
						if (err) {
							console.error(err);
							return;
						}

						let personPersonIds = record.get('person_person');
						console.log("PersonPerson Ids: ");
						console.log(personPersonIds);
						if (personPersonIds)
						{
							for (let i = 0; i < personPersonIds.length; i++)
							{
								let currentRel = {
									personName: "",
									relationshipOne: "",
									relationshipTwo: ""
								};

								base('person_person').find(personPersonIds[i], function(err, record) {
									let personIdOne = record.get('person_id_1');
									let personIdTwo = record.get('person_id_2');

									if (personIdOne[0] === recId)
									{
										base('person').find(personIdTwo[0], function(err, record) {
											if (err) {
												console.log(err);
												return;
											}

											currentRel.personName = record.get('given_name_en') + " " + record.get('family_name_en');
										});

										let thisPersonRoleId = record.get('person_1_role_id');
										base('person_person_role').find(thisPersonRoleId[0], function(err, record) {
											if (err) {
												console.log(err);
												return;
											}
											currentRel.relationshipOne = record.get('pers_pers_role_en');
										});

										let otherPersonRoleId = record.get('person_2_role_id');
										base('person_person_role').find(otherPersonRoleId[0], function(err, record) {
											if (err) {
												console.log(err);
												return;
											}
											currentRel.relationshipTwo= record.get('pers_pers_role_en');
										});
									}
									else
									{
										base('person').find(personIdOne[0], function(err, record) {
											if (err) {
												console.log(err);
												return;
											}

											currentRel.personName = record.get('given_name_en') + " " + record.get('family_name_en');
										});

										let thisPersonRoleId = record.get('person_2_role_id');
										base('person_person_role').find(thisPersonRoleId[0], function(err, record) {
											if (err) {
												console.log(err);
												return;
											}

											currentRel.relationshipOne = record.get('pers_pers_role_en');
										});

										let otherPersonRoleId = record.get('person_1_role_id');
										base('person_person_role').find(otherPersonRoleId[0], function(err, record) {
											if (err) {
												console.log(err);
												return;
											}

											currentRel.relationShipTwo = record.get('pers_pers_role_en');
										});
									}
								});
								returnObj.push(currentRel);
							}
						}

					});
					resolve({"data": returnObj});
				});
			},
			institutionalConnections(recId) {
				return new Promise(function(resolve, reject) {

					let returnObj = {
						institution: "N/A",
						institutionYear: "N/A",
						participationType: "N/A"
					};

					base('person_organization').find(recId, function(err, record) {
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
					});
					resolve({"data": returnObj});
				})
			},
			corporateConnections(recId) {
				return new Promise(function(resolve, reject) {

					let returnObj = {
						membership: "N/A",
						role: "N/A",
						time: "N/A"
					};

					base('person_organization').find(recId, function(err, record) {
						if (err) {
							console.log(err);
							return;
						}

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

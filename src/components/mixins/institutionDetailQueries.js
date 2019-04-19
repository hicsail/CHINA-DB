const Airtable = require('airtable');
const base = new Airtable({apiKey:'keyvkMlawNyw2WAHK'}).base("appgj7WMdGiUCbfuE");

export const InstitutionQueries = {
	methods: {
		personnelConnections(recId) {
			return new Promise(function(resolve, reject) {

				let returnObj = [];

				base('institution').find(recId, function(err, record) {
					if (err) {
						console.log(err);
						return;
					}

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
				});
				resolve({"data": returnObj});
			})
		},
		institutionalConnections(recId) {
			return new Promise(function(resolve, reject) {

				let returnObj = [];

				base('institution').find(recId, function(err, record) {
					if (err) {
						console.log(err);
						return;
					}

					let orgOrgIds = record.get('organization_organization');
					if (orgOrgIds)
					{
						for (let i = 0; i < orgOrgIds.length; i++) {
							let currentRel = {
								orgName: "",
								orgRole: "",
								parentOrgRole: ""
							};

							base('organization_organization').find(orgOrgIds[i], function(err, record) {
								if (err) {
									console.log(err);
									return;
								}

								let orgIdOne = record.get("inst_id_1");
								let orgIdTwo = record.get("inst_id_2");

								if (orgIdOne && orgIdTwo)
								{
									if (orgIdOne === recId)
									{

										let orgRoleOne = record.get("org_role_id_1");
										// grab name from orgIdTwo
										base('organization_organization_role').find(orgRoleOne[0], function(err, record) {
											if (err) {
												console.log(err);
												return;
											}
											currentRel.parentOrgRole = record.get('org_org_role_en');
										});

										let orgRoleTwo = record.get("org_role_id_2");
										base('organization_organization_role').find(orgRoleTwo[0], function(err, record) {
											if (err) {
												console.log(err);
												return;
											}
											currentRel.orgRole = record.get('org_org_role_en');
										});

										base('institution').find(orgIdTwo, function(err, record) {
											if (err) {
												console.log(err);
												return;
											}
											currentRel.orgName = record.get('inst_name');
										});
									}
									else
									{
										let orgRoleTwo = record.get("org_role_id_2");
										// grab name from orgIdOne
										base('organization_organization_role').find(orgRoleTwo[0], function(err, record) {
											if (err) {
												console.log(err);
												return;
											}
											currentRel.parentOrgRole = record.get('org_org_role_en');
										});

										let orgRoleOne = record.get("org_role_id_1");
										base('organization_organization_role').find(orgRoleOne[0], function(err, record) {
											if (err) {
												console.log(err);
												return;
											}
											currentRel.orgRole = record.get('org_org_role_en');
										});

										base('institution').find(orgIdOne, function(err, record) {
											if (err) {
												console.log(err);
												return;
											}
											currentRel.orgName = record.get('inst_name');
										});
									}
									returnObj.push(currentRel);
								}
							});
						}
					}
				});
				resolve({"data": returnObj})
			});
		},
		corporateConnections(recId) {
			return new Promise(function(resolve, reject) {

				let returnObj = [];

				base('institution').find(recId, function(err, record) {
					if (err) {
						console.log(err);
						return;
					}

					let orgOrgIds = record.get('organization_organization');
					if (orgOrgIds) {
						for (let i = 0; i < orgOrgIds.length; i++) {
							let currentRel = {
								orgName: "",
								orgRole: "",
								parentOrgRole: ""
							};

							base('organization_organization').find(orgOrgIds[i], function(err, record) {
								if (err) {
									console.log(err);
									return;
								}

								let instId = record.get('inst_id_1');
								let corpId = record.get('corp_id_2');

								if (instId && corpId)
								{
									let instRole = record.get('org_role_id_1');
									base('organization_organization_role').find(instRole[0], function(err, record) {
										if (err) {
											console.log(err);
											return;
										}

										currentRel.parentOrgRole = record.get('org_org_role_en');
									});

									let corpRole = record.get('org_role_id_2');
									base('organization_organization_role').find(corpRole[0], function(err, record) {
										if (err) {
											console.log(err);
											return;
										}

										currentRel.orgRole = record.get('org_org_role_en');
									});

									base('corporate_entity').find(corpId[0], function(err, record) {
										if (err) {
											console.log(err);
											return;
										}

										currentRel.orgName = record.get('corp_name_en');
									});
									returnObj.push(currentRel);
								}
							});
						}
					}
				});

				resolve({"data": returnObj});

			});
		}
	}
};
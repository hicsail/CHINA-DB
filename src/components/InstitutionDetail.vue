<template>
    <div class = "container">

    <br>
    <b-container>
        <h3>Institutional Data</h3>
            <span class="subTitle">Name:</span> {{ name }}
            <br><span class="subTitle">Alternate names:</span> {{ alternateName }}
            <br><span class="subTitle">Type:</span> {{ type }}
            <br><span class="subTitle">Start-End:</span> {{ startEnd }}
            <br><span class="subTitle">Location:</span> {{ location }}
            <br>
    </b-container>


    <hr>
    <b-container>
        <h3>Personnel</h3>
            <tr v-for="row in personell">
                <br><span class="subTitle">Name: </span> {{ row.personName }}
                <br><span class="subTitle">Role: </span> {{ row.personRole }}
            </tr>
    </b-container>


    <hr>
    <b-container>
        <h3>Institutional Relationships</h3>
            <tr v-for="row in institutional">
                <br><span class="subTitle">Name: </span> {{ row.orgName }}
                <br><span class="subTitle">Relationship: </span> {{ row.parentOrgRole }} - {{ row.orgRole }}
            </tr>
    </b-container>


    <hr>
    <b-container>
        <h3>Corporate Entity Relationships</h3>
            <tr v-for="row in corporate">
                <br><span class="subTitle">Name: </span> {{row.orgName }}
                <br><span class="subTitle">Relationship: </span> {{ row.parentOrgRole }} - {{ row.orgRole }}
            </tr>
    </b-container>

    </div>
</template>

<script>
  import vueSlider from 'vue-slider-component';
  import  { PopupContent }  from "./mixins/popupContent";
  import { InstitutionQueries } from "./mixins/institutionDetailQueries"

  export default {
    name: 'Institution',
    components: {
      vueSlider,
      PopupContent,
      InstitutionQueries
    },
    data: () => ({
      institution: {},
      personell: [],
      institutional: [],
      corporate: [],
      name: '',
      alternateName: '',
      type: '',
      startEnd: '',
      location: '',
      president1: '',
      president1Year: '',
      teacher: '',
      teacherYear: '',
      partner: '',
      partnerYear: '',
      overseer: '',
      overseerYear: '',
      corporateEntityOverseer: '',
      corporateEntityOverseerYear: '',
      corporateEntityAffiliate: '',
      corporateEntityAffiliateYear: '',
    }),
    mounted() {
      this.institution = this.$store.getters.institutionData;

      // Institutional Data
      this.name= this.capitalize(this.institution.name);
      // this.alternateName= '';
      this.type= this.institution.institution_type;
      this.startEnd = this.getStartEnd();
      this.location= this.capitalize(this.institution.loc.location_name);

      // Personnel
      // this.president1= '';
      // this.president1Year= '';
      // this.teacher= '';
      // this.teacherYear= '';

      // Institutional Relationships
      // this.partner= '';
      // this.partnerYear= '';
      // this.overseer= '';
      // this.overseerYear= '';

      // Corporate Entity Relationships
      // this.corporateEntityOverseer= '';
      // this.corporateEntityOverseerYear= '';
      this.corporateEntityAffiliate= this.institution.corp_relations.association !== 'N/A' ? this.institution.corp_relations.association : '';
      // this.corporateEntityAffiliateYear= '';

      this.resolvePersonnel();
      this.resolveInstitutional();
      this.resolveCorporate();

    },
    methods: {
      getStartEnd(){
        let years = '';
        if (this.institution.time.start_year) {
          years = this.institution.time.start_year.toString().toString() + " - "
        }
        if (this.institution.time.end_year){
          years += this.institution.time.end_year.toString()
        }
        return years;
      },
      async resolvePersonnel() {
      	let obj = await this.personnelConnections(this.institution.rec_id);
      	console.log("Personnel data: ");
      	console.log(obj)
        this.personell = obj.data;
      },
      async resolveInstitutional() {
      	let obj = await this.institutionalConnections(this.institution.rec_id);
      	console.log("Institutional data: ");
      	console.log(obj);
      	this.institutional = obj.data;
      },
      async resolveCorporate() {
      	let obj = await this.corporateConnections(this.institution.rec_id);
      	console.log("Corporate data: ");
      	console.log(obj);
      	this.corporate = obj.data;
      }
    },
    // Use PopupContent mixin for 'capitalize' function, which capitalizes names
    mixins: [
      PopupContent,
      InstitutionQueries
    ]

  };
</script>

<style>

    .subTitle {
        font-weight: bold;
    }

</style>

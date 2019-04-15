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
            <span class="subTitle">President:</span> {{ president1, president1Year }}
            <br><span class="subTitle">Teacher:</span> {{ teacher, teacherYear }}
    </b-container>


    <hr>
    <b-container>
        <h3>Institutional Relationships</h3>
            <span class="subTitle">Partner with:</span> {{ partner, partnerYear }}
            <br><span class="subTitle">Overseen by:</span> {{ overseer, overseerYear }}
    </b-container>


    <hr>
    <b-container>
        <h3>Corporate Entity Relationships</h3>
            <span class="subTitle">Overseen by:</span> {{ corporateEntityOverseer, corporateEntityOverseerYear }}
            <br><span class="subTitle">Affiliated with:</span> {{ corporateEntityAffiliate, corporateEntityAffiliateYear }}
    </b-container>

    </div>
</template>

<script>
  import vueSlider from 'vue-slider-component';
  import  { PopupContent }  from "./mixins/popupContent";

  export default {
    name: 'Institution',
    components: {
      vueSlider,
      PopupContent
    },
    data: () => ({
      institution: {},
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
      console.log('the institution detail data is:');
      console.log(this.institution);

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
      }
    },
    // Use PopupContent mixin for 'capitalize' function, which capitalizes names
    mixins: [
      PopupContent
    ]

  };
</script>

<style>

    .subTitle {
        font-weight: bold;
    }

</style>

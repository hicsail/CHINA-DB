<template>
    <div class = "container">

    <br>
    <b-container>
        <h3>Biographical Data</h3>
            <span class="subTitle">Name:</span> {{ name }}
            <br><span class="subTitle">Alternate names:</span> {{ chineseName }}
            <br><span class="subTitle">Titles:</span> {{ titles }}
            <br><span class="subTitle">Birth-Death:</span> {{ birthDeath }}
            <br><span class="subTitle">Nationality:</span> {{ nationality }}
            <br><span class="subTitle">Gender:</span> {{ gender }}
            <br>
    </b-container>


    <hr>
    <b-container>
        <h3>Interpersonal Connections</h3>
            <span class="subTitle">Parent to:</span> {{ children }}
            <br><span class="subTitle">Child of:</span> {{ parents }}
            <br><span class="subTitle">Confessor to:</span> {{ confesee, confeseeYear }}
    </b-container>


    <hr>
    <b-container>
        <h3>Institutional Relationships</h3>
            <span class="subTitle">Pastor/Minister of:</span> {{ institution, institutionYear }}
            <br><span class="subTitle">Principal of:</span> {{ principalOf, principalOfYear }}
    </b-container>


    <hr>
    <b-container>
        <h3>Corporate Entity Relationships</h3>
            <span class="subTitle">Jinshi in:</span> {{ jinshi, jinshiDate }}
            <br><span class="subTitle">Member of:</span> {{ membership, membershipYear }}
            <br><span class="subTitle">Minister of:</span> {{ corporateEntityMinister, corporateEntityMinisterYear }}
    </b-container>


    <hr>
    <b-container>
        <h3>Participation in Special Events</h3>
            <span class="subTitle">Participant at:</span> {{ participant, participantYear }}
            <br><span class="subTitle">Chairperson at:</span> {{ chair, chairYear }}
            <br><span class="subTitle">Disembarked on:</span> {{ disembarked, disembarkedYear }}
    </b-container>

    </div>
</template>

<script>
  import vueSlider from 'vue-slider-component';
  import  { PopupContent }  from "./mixins/popupContent";

  export default {
    name: 'Individual',
    components: {
      vueSlider,
      PopupContent
    },
    data: () => ({
      individual: {},
      name: '',
      chineseName: '',
      titles: '',
      birthDeath: '',
      nationality: '',
      gender: '',
      children: '',
      parents: '',
      confesee: '',
      confeseeYear: '',
      institution: '',
      institutionYear: '',
      principalOf: '',
      principalOfYear: '',
      jinshi: '',
      jinshiDate: '',
      membership: '',
      membershipYear: '',
      corporateEntityMinister: '',
      corporateEntityMinisterYear: '',
      participant: '',
      participantYear: '',
      chair: '',
      chairYear: '',
      disembarked: '',
      disembarkedYear: ''
    }),
    mounted() {
      this.individual = this.$store.getters.individualData;
      console.log('the individual detail data is:');
      console.log(this.individual);

      this.name =  this.capitalize(this.individual.titles.given_name_en) + " " + this.capitalize(this.individual.titles.family_name_en);
      //this.chineseName = this.capitalize(this.individual.titles.family_name_zh) + " " + this.capitalize(this.individual.titles.given_name_zh);
      this.titles = this.individual.gender === 'male' ? 'Mr.' : 'Ms.';
      this.birthDeath = this.getBirthDeath();
      this.nationality = this.individual.nationality !== 'N/A' ? this.individual.nationality : 'unknown';
      this.gender = this.individual.gender;

      // Interpersonal Connections
      // this.children: ;
      // this.parents: '';
      // this.confesee: '';
      // this.confeseeYear: '';

      // Institutional Relationships
      this.institution = this.capitalize(this.individual.institution_name);
      // this.institutionYear: '';
      // this.principalOf= '';
      // this.principalOfYear= '';

      // Corporate Entity Relationships
      // this.jinshi = '';
      // this.jinshiDate= '';
      this.membership = this.capitalize(this.individual.tradition.association);
      // this.membershipYear= '';
      // this.corporateEntityMinister= '';
      // this.corporateEntityMinisterYear= '';

      // Participation in Special Events
      // this.participant= '';
      // this.participantYear= '';
      // this.chair= '';
      // this.chairYear= '';
      // this.disembarked= '';
      // this.disembarkedYear= '';

    },
    methods: {
      getBirthDeath(){
        let years = '';
        if (this.individual.time.start_year) {
          years = this.individual.time.start_year.toString() + " - "
        }
        if (this.individual.time.end_year){
          years += this.individual.time.end_year.toString()
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

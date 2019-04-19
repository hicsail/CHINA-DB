<template>
    <div class = "container">

    <br>
    <b-container>
        <h3>Biographical Data</h3>
            <span class="subTitle">Name:</span> {{ personal.name }}
            <br><span class="subTitle">Alternate names:</span> {{ personal.chineseName }}
            <br><span class="subTitle">Titles:</span> {{ personal.titles }}
            <br><span class="subTitle">Birth-Death:</span> {{ personal.birthDeath }}
            <br><span class="subTitle">Nationality:</span> {{ personal.nationality }}
            <br><span class="subTitle">Gender:</span> {{ personal.gender }}
            <br>
    </b-container>

    <hr>
    <b-container>
        <h3>Interpersonal Connections</h3>
        <tr v-for="row in interpersonal">
            <br><span class="subTitle">Name: </span> {{ row.personName}}
            <br><span class="subTitle">Relationship: </span> {{ row.relationshipOne }} - {{ row.relationshipTwo }}
        </tr>
    </b-container>


    <hr>
    <b-container>
        <h3>Institutional Relationships</h3>
            <span class="subTitle">Present at:</span> {{ institutional.institution }} ({{ institutional.institutionYear }})
            <br><span class="subTitle">Participation Type:</span> {{ institutional.participationType }}
    </b-container>


    <hr>
    <b-container>
        <h3>Corporate Entity Relationships</h3>
            <span class="subTitle">Member of:</span> {{ corporate.membership }} ({{ corporate.time }})
            <br><span class="subTitle">Role:</span> {{ corporate.role }}
    </b-container>

    </div>
</template>

<script>
  import vueSlider from 'vue-slider-component';
  import  { PopupContent }  from "./mixins/popupContent";
  import { IndividualQueries } from "./mixins/individualDetailQueries";

  export default {
    name: 'Individual',
    components: {
      vueSlider,
      PopupContent,
      IndividualQueries
    },
    data: () => ({
      individual: {},
      personal: [],
      interpersonal: {},
      institutional: {},
      corporate: {}
    }),
    mounted() {
      this.individual = this.$store.getters.individualData;

      this.resolvePersonal();
      this.resolveInterpersonal();
      this.resolveInstitutional();
      this.resolveCorporate();
      this.resolveEvents()

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
      },
      resolvePersonal() {
        this.personal.name =
          this.capitalize(this.individual.titles.given_name_en)
          + " " + this.capitalize(this.individual.titles.family_name_en);
        this.personal.chineseName =
          this.capitalize(this.individual.titles.family_name_zh)
          + " " + this.capitalize(this.individual.titles.given_name_zh);
        this.personal.titles = this.individual.gender === 'male' ? 'Mr.' : 'Ms.';
        this.personal.birthDeath = this.getBirthDeath();
        this.personal.nationality = this.individual.nationality !== 'N/A' ? this.individual.nationality : 'unknown';
        this.personal.gender = this.individual.gender;
      },
      async resolveInterpersonal() {
        let obj = await this.interpersonalConnections(this.individual.rec_id);
        console.log("Interpersonal Connections: ");
        console.log(obj.data);
        this.interpersonal = obj.data
      },
      async resolveInstitutional() {
      	let obj = await this.institutionalConnections(this.individual.pers_org_id);
      	this.institutional = obj.data;
      },
      async resolveCorporate() {

      	console.log(this.individual);
        if (this.individual.pers_org_type === "corporate")
        {
            let obj = await this.corporateConnections(this.individual.pers_org_id);
            this.corporate = obj.data;
        }
        else
        {
          this.corporate = {
            membership: this.capitalize(this.individual.tradition.association),
            role: "Member",
            time: this.individual.time.start_year
          }
        }
      },
    },
    // Use PopupContent mixin for 'capitalize' function, which capitalizes names
    mixins: [
      PopupContent,
      IndividualQueries
    ]

  };
</script>

<style>

    .subTitle {
        font-weight: bold;
    }

</style>

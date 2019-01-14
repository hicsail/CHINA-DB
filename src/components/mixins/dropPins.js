export const DropPins = {
  methods: {
    getIndividualPin() {
      return L.AwesomeMarkers.icon({
        markerColor: 'green',
        prefix: 'fas fa-male',
        icon: 'male'
      })
    },
    getInstitutionPin() {
      return L.AwesomeMarkers.icon({
        markerColor: 'purple',
        prefix: 'fas fa-university',
        icon: 'university'
      })
    },
    getCorporateEntityPin() {
      return L.AwesomeMarkers.icon({
        markerColor: 'orange',
        prefix: 'fas fa-building',
        icon: 'building'
      })
    }
  }
}
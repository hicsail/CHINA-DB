export const DropPins = {
  methods: {
    getIndividualPin() {
      return L.AwesomeMarkers.icon({
        markerColor: 'green',
        prefix: 'fas fa-male',
        icon: 'male'
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
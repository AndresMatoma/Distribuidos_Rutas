//Creacion mapa
let map = L.map('map').setView([4.639386,-74.082412],7)

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
  maxZoom: 18,
}).addTo(map);

//Diseño marcadores
let iconMarker = L.icon({
    iconUrl:'marker.png',
    iconSize:[25,41],
    iconAnchor:[12,41],
    popupAnchor:[-1, -34]
})

let iconMarkerbus = L.icon({
    iconUrl:'marker-bus.png',
    iconSize:[41,41],
    iconAnchor:[12,41],
    popupAnchor:[-1, -34]
})

let markers =[]
//Ubicación actual
navigator.geolocation.getCurrentPosition(function (position) {
    var lat = position.coords.latitude;
    var lng = position.coords.longitude;
    console.log(lat,lng);
    var marker = L.marker([lat, lng],{icon:iconMarker}).addTo(map);
    marker.bindPopup("<b>Tu ubicacion actual</b>").openPopup();

    map.setView([lat, lng], 15);
    markers.push(marker)
    document.getElementById('me-location').addEventListener('click',function(e){
        let coords = L.latLng(lat,lng);
        map.flyTo(coords,14);
    })
});

//Hora actual
function showTime() {
    var now = new Date(); // Crear un objeto Date con la hora actual
    var hours = now.getHours(); // Obtener las horas actuales
    var minutes = now.getMinutes(); // Obtener los minutos actuales
    var seconds = now.getSeconds(); // Obtener los segundos actuales
    
    if(minutes==0 && seconds ==0){
        location.reload();
    }
    document.getElementById('clock').innerHTML = convertirHora(hours,minutes,seconds); // Actualizar la hora en el elemento HTML con ID "clock"
  }
  
  setInterval(showTime, 1000); // Actualizar la hora cada segundo

  let url_ruta = 'http://127.0.0.1:8000/ruta/'
  fetch(url_ruta)
    .then(response=>response.json())
    .then(data=>{
        var current_time = new Date();
        var current_hour = current_time.getHours();
        var current_minutes = current_time.getMinutes();
        var current_seconds = current_time.getSeconds();
        
        let closest_time = null;
        let min_diff = Infinity;
        
        //Obtener la hora siguiente de las rutas disponibles
        for (const ruta of data) {
            
            const [hour, minutes, seconds] = ruta.hora.split(':').map(Number);
            
            let diff =(hour - current_hour) * 60 + (minutes - current_minutes) + (seconds - current_seconds) / 60;
            if (diff <= 0) {
                diff += 24 * 60; // Añadimos un día completo en minutos
            }
            if (diff < min_diff) {
                min_diff = diff;
                closest_time = ruta.hora;
            }
        }

        var [hora, minutos, segundos] = closest_time.split(':').map(Number);
        document.getElementById('next-clock').innerHTML = convertirHora(hora,minutos,segundos);
    
        //Pintar las ubicaciones con la siguiente hora
        data.forEach(dato => {
                if(dato.hora === closest_time){
                var marker = L.marker([dato.latitud, dato.longitud],{icon:iconMarkerbus}).addTo(map);
                marker.bindPopup(`<b>Lugar: </b>${dato.ubicacion},<b>Hora: </b>${dato.hora}`).openPopup();
                markers.push(marker);
                }
        });
        map.fitBounds(L.featureGroup(markers).getBounds())
    })
    .catch(error=>console.error(error));

    function convertirHora(hora,minutos,segundos){
        var amOrPm = hora >= 12 ? 'pm' : 'am'; // Determinar si es antes o después del mediodía
  
    // Convertir la hora a formato de 12 horas
    hora = hora % 12;
    hora = hora ? hora : 12;
  
    var timeString = hora + ':' + (minutos < 10 ? '0' : '') + minutos + ':' + (segundos < 10 ? '0' : '') + segundos + ' ' + amOrPm;
    return timeString;
    }
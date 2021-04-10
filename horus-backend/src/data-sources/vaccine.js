const axios = require('axios');
async function getData(){
  const response = await axios.post('https://gis.minsa.gob.pe/WebApiRep2/api/Establecimiento/ListarPuntosVacunacion')
  
}



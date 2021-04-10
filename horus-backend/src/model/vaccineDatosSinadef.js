const mongoose = require('mongoose');
const Schema = mongoose.Schema;

var VaccineDatosSinadefSchema = new Schema(
  {
    ubigeo: { type: String, required: true },
    totalFallecidos: {type: Number},
    mujeresFallecidos: { type: Number  },
    hombresFallecidos: { type: Number },
    mujeresEdad : {type: Object},
    hombresEdad: {type: Object}
  },
  { collection: 'vaccineDatosAbiertosCovidFall' }
);

const vaccineDatosSinadef = mongoose.model(
  'vaccineDatosAbiertosCovidFall',
  VaccineDatosSinadefSchema
);

module.exports = vaccineDatosSinadef;

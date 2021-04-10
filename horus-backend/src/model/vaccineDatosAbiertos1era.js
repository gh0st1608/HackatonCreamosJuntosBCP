const mongoose = require('mongoose');
const Schema = mongoose.Schema;

var VaccineDatosAbiertos1eraSchema = new Schema(
  {
    ubigeo: { type: String, required: true },
    totalVacunados: {type: Number},
    mujeresVacunados: { type: Number  },
    hombresVacunados: { type: Number },
    mujeresEdad : {type: Object},
    hombresEdad: {type: Object}
  },
  { collection: 'vaccineDatosAbiertos1era' }
);

const VaccineDatosAbiertos1era = mongoose.model(
  'vaccineDatosAbiertos1era',
  VaccineDatosAbiertos1eraSchema
);

module.exports = VaccineDatosAbiertos1era;

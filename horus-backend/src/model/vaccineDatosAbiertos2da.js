const mongoose = require('mongoose');
const Schema = mongoose.Schema;

var VaccineDatosAbiertos2daSchema = new Schema(
  {
    ubigeo: { type: String, required: true },
    totalVacunados: {type: Number},
    mujeresVacunados: { type: Number  },
    hombresVacunados: { type: Number },
    mujeresEdad : {type: Object},
    hombresEdad: {type: Object}
  },
  { collection: 'vaccineDatosAbiertos2da' }
);

const VaccineDatosAbiertos2da = mongoose.model(
  'vaccineDatosAbiertos2da',
  VaccineDatosAbiertos2daSchema
);

module.exports = VaccineDatosAbiertos2da;

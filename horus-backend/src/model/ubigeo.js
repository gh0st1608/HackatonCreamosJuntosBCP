const mongoose = require('mongoose');
const Schema = mongoose.Schema;

var UbigeoSchema = new Schema(
  {
    ubigeo: { type: String, required: true },
    departamento: { type: String, required: true },
    provincia: { type: String, required: true },
    distrito: { type: String, required: true },
  },
  { collection: 'ubigeo' }
);

const Ubigeo = mongoose.model('ubigeo', UbigeoSchema);

module.exports = Ubigeo;

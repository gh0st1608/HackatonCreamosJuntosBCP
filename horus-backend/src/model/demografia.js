const mongoose = require("mongoose");
const Schema = mongoose.Schema;

var DemografiaSchema = new Schema({
    ubigeo:{type:String, required: true},    
    pob_total: {type: String, required: true},
 },
 { collection: 'demografia' });

const Demografia = mongoose.model("demografia", DemografiaSchema);

module.exports = Demografia;
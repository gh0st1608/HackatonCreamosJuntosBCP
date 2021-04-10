const express = require('express');
const router = express.Router();
const Ubigeo = require('../model/ubigeo');
const Demografia = require('../model/demografia');
const VaccineDatosAbiertos1era = require('../model/vaccineDatosAbiertos1era');
const VaccineDatosAbiertos2da = require('../model/vaccineDatosAbiertos2da');
const vaccineDatosSinadef = require('../model/vaccineDatosSinadef');
router.get('/departamentos', async (req, res) => {
  try {
    const departamentos = await Ubigeo.find({
      ubigeo: /^[0-9]{2}0000$/,
      provincia: '',
      distrito: '',
    })
      .select('-_id ubigeo departamento provincia distrito')
      .exec();
    console.log('entro a ubigeos');
    res.json({ departamentos });
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});
//ubigeodedepartamento 010000
router.get('/provincias/:dptoid', async (req, res) => {
  try {
    const dptoid = req.params.dptoid.substring(0, 2);
    const redpto = new RegExp('^' + dptoid);
    const provincias = await Ubigeo.find({
      ubigeo: redpto,
      provincia: { $ne: '' },
      distrito: '',
    })
      .select('-_id')
      .exec();
    res.json({ provincias });
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

//ubigeodeprovincia 010100
router.get('/distritos/:provid', async (req, res) => {
  try {
    const provid = req.params.provid.substring(0, 4);
    console.log(provid);
    const reprov = new RegExp('^' + provid);
    console.log(reprov);
    const distritos = await Ubigeo.find({
      ubigeo: reprov,
      distrito: { $ne: '' },
    }).exec();
    res.json({ distritos });
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

router.get('/resumen/peru', async (req, res) => {
  try {
    const demografia = await Demografia.findOne({ ubigeo: '000000' }).exec();
    const vacuna1 = await VaccineDatosAbiertos1era.findOne({
      ubigeo: '000000',
    }).exec();
    const vacuna2 = await VaccineDatosAbiertos2da.findOne({
      ubigeo: '000000',
    }).exec();
    res.json({ demografia, vacuna1, vacuna2 });
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

router.get('/resumen/departamento/:dptoid', async (req, res) => {
  try {
    const dptoid = req.params.dptoid;
    const pattern = new RegExp(`^${dptoid}$`);
    const nombres = await Ubigeo.findOne({ ubigeo: pattern })
      .select('-_id')
      .exec();
    const demografia = await Demografia.findOne({ ubigeo: pattern })
      .select('-_id')
      .exec();
    const vacuna1 = await VaccineDatosAbiertos1era.findOne({ ubigeo: pattern })
      .select('-_id')
      .exec();
    const vacuna2 = await VaccineDatosAbiertos2da.findOne({ ubigeo: pattern })
      .select('-_id')
      .exec();
    const sinadef = await vaccineDatosSinadef.findOne({ ubigeo: pattern })
      .select('-_id')
      .exec();

    res.json({ nombres, demografia, vacuna1, vacuna2, sinadef });
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

router.get('/resumen/provincia/:provid', async (req, res) => {
  try {
    const provid = req.params.provid;
    const pattern = new RegExp(`^${provid}$`);
    const nombres = await Ubigeo.findOne({ ubigeo: pattern })
      .select('-_id')
      .exec();
    const demografia = await Demografia.findOne({ ubigeo: pattern })
      .select('-_id')
      .exec();
    const vacuna1 = await VaccineDatosAbiertos1era.findOne({ ubigeo: pattern })
      .select('-_id')
      .exec();
    const vacuna2 = await VaccineDatosAbiertos2da.findOne({ ubigeo: pattern })
      .select('-_id')
      .exec();
    const sinadef = await vaccineDatosSinadef.findOne({ ubigeo: pattern })
    .select('-_id')
    .exec();

    res.json({ nombres, demografia, vacuna1, vacuna2, sinadef });
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

router.get('/resumen/distrito/:distid', async (req, res) => {
  try {
    const distid = req.params.distid;
    const pattern = new RegExp(`^${distid}$`);
    const nombres = await Ubigeo.findOne({ ubigeo: pattern })
      .select('-_id')
      .exec();
    const demografia = await Demografia.findOne({ ubigeo: pattern })
      .select('-_id')
      .exec();
    const vacuna1 = await VaccineDatosAbiertos1era.findOne({ ubigeo: pattern })
      .select('-_id')
      .exec();
    const vacuna2 = await VaccineDatosAbiertos2da.findOne({ ubigeo: pattern })
      .select('-_id')
      .exec();
    const sinadef = await vaccineDatosSinadef.findOne({ ubigeo: pattern })
    .select('-_id')
    .exec();
    res.json({ nombres, demografia, vacuna1, vacuna2, sinadef });
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

module.exports = router;

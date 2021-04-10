const express = require('express');

const router = express.Router();

router.get('/vacunados/', function(req,res){
  res.json({success: true, data: ["a"]})
});





module.exports = router


const express= require('express');
const dataSources = require('./dataSources.routes')
const vaccine = require('./vaccine.routes')
const routes = express.Router();

routes.use('/api-thirdparty', dataSources);
routes.use('/api', vaccine);


module.exports = routes;



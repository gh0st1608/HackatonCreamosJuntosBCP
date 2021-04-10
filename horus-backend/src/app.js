const createError = require('http-errors');
const express = require('express');
const path = require('path');
const logger = require('morgan');
const bodyParser = require('body-parser');
const compress= require('compression');
const helmet = require('helmet')
const routes = require('./routes/');
const db = require('./db/mongoose');
const cors = require('cors');
const methodOverride = require('method-override');


const app = express();



/*
mongoose.Promise = global.Promise
mongoose.connect('mongodb+srv://vaccine-devs:vaccine-devs123@clustervaccinedeveloper.imldj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority', {useMongoClient: true})
var db = mongoose.connection

db.on('error', function(err){
  console.log('connection error', err)
})

db.once('open', function(){
  console.log('Connection to DB successful')
})
*/
app.use(logger('dev'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(compress());
app.use(cors());
app.use(methodOverride());
app.use(helmet())
app.use(routes);

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  next(createError(404));
});

app.use(function(err, req, res, next) {
  
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  res.status(err.status || 500);
  res.json({success: false});
});

module.exports = app;

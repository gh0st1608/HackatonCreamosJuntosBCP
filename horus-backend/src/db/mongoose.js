const mongoose = require('mongoose');
const config = require('../config/index')


mongoose.connect(config.MONGOOSE_BD.URI_MONGO_BD, {
    useUnifiedTopology: true,
    useNewUrlParser: true,
  });
  
  const connection = mongoose.connection;
  
  connection.once('open', () => {
    console.log('MongoDB database connection established successfully');
  });

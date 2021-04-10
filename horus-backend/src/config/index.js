require('dotenv').config({path:'.env'})

module.exports = {
MONGOOSE_BD : {
    URI_MONGO_BD:process.env.Mongo_URI
}
}
const express = require('express')
const app = express()
const port = 3000
const path = require('path')

app.get('/', function(request, response){
    response.sendFile(path.resolve(__dirname, 'api_ui.html'));
});

app.listen(port, () => console.log(`Example app listening on port ${port}!`))
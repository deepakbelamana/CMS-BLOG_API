const express = require('express');
const registerUser = require('./user/register')
const app = express();
const cors = require('cors');
const bodyparser = require("body-parser")
const userlogin=require('./user/login')
app.use(bodyparser.json())
app.use(cors());

app.get('/',(req,res)=>
{
    res.send("Hello world!")
})

app.post('/register',registerUser.registerUser)

app.post('/login',userlogin.login)


app.listen(3000,()=>
{
    console.log("Server Started Successfully..!");
})
const { json } = require("express")

var registerUser=function(req,res)
{
    console.log(req.body)
    res.json("hello")
}

module.exports={
    registerUser
}
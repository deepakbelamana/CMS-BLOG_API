const { json } = require("express")

const login= function(req,res)
{
    console.log(req.body);
    res.json("login here")
}

module.exports={
    login
}
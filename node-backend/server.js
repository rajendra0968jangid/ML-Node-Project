const express = require("express");
const axios = require("axios");
const cors = require("cors");

const app = express();

app.use(cors());
app.use(express.json());

app.post("/student-result", async (req, res) => {
    try {
        const response = await axios.post(
            "http://127.0.0.1:5000/predict",
            req.body
        );

        res.json(response.data);
    } catch (error) {
        console.log(error.message);
        res.status(500).json({
            message: "Prediction failed"
        });
    }
});

app.listen(3000, () => {
    console.log("Node server running on port 3000");
});
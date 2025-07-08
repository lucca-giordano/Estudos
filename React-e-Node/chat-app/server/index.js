const express = require('express');
const cors = require('cors');
const mongoose = require('mongoose');
const userRoutes = require('./routes/userRoutes');

const app = express();
require('dotenv').config();

app.use(cors());
app.use(express.json());

mongoose.connect(process.env.MONGO_URL,{
    useNewUrlParser: true,
    useUnifiedTopology: true
}).then(() => {
    console.log("Connected to MongoDB");
}).catch(err => {
    console.log("Error: ", err.message);
});

app.use('/api/auth', userRoutes);

const server = app.listen(process.env.PORT, () => {
  console.log(`Server is running on port: ${process.env.PORT}`);
})
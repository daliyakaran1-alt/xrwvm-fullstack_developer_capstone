const express = require('express');
const mongoose = require('mongoose');
const fs = require('fs');
const cors = require('cors');
const app = express();
const port = 3030;

app.use(cors());
app.use(require('body-parser').urlencoded({ extended: false }));
app.use(express.json());

const reviewsPath = fs.existsSync("reviews.json") ? "reviews.json" : (fs.existsSync("data/reviews.json") ? "data/reviews.json" : "./data/reviews.json");
const dealershipsPath = fs.existsSync("dealerships.json") ? "dealerships.json" : (fs.existsSync("data/dealerships.json") ? "data/dealerships.json" : "./data/dealerships.json");

const reviews_data = JSON.parse(fs.readFileSync(reviewsPath, 'utf8'));
const dealerships_data = JSON.parse(fs.readFileSync(dealershipsPath, 'utf8'));

let memoryReviews = [...reviews_data['reviews']];
let memoryDealerships = [...dealerships_data['dealerships']];

let Reviews = null;
let Dealerships = null;
let useMongo = false;

try {
  Reviews = require('./review');
  Dealerships = require('./dealership');
  mongoose.connect("mongodb://mongo_db:27017/", { dbName: 'dealershipsDB', serverSelectionTimeoutMS: 2000 })
    .then(() => {
      useMongo = true;
      console.log("Connected to MongoDB successfully");
      Reviews.deleteMany({}).then(() => {
        Reviews.insertMany(reviews_data['reviews']);
      });
      Dealerships.deleteMany({}).then(() => {
        Dealerships.insertMany(dealerships_data['dealerships']);
      });
    })
    .catch((err) => {
      console.log("MongoDB connection unavailable, using in-memory JSON data:", err.message);
      useMongo = false;
    });
} catch (error) {
  console.log("Mongoose initialization notice:", error.message);
  useMongo = false;
}

// Express route to home
app.get('/', async (req, res) => {
  res.send("Welcome to the Mongoose API");
});

// Express route to fetch all reviews
app.get('/fetchReviews', async (req, res) => {
  try {
    if (useMongo && Reviews) {
      const documents = await Reviews.find();
      return res.json(documents);
    }
    res.json(memoryReviews);
  } catch (error) {
    res.status(500).json({ error: 'Error fetching documents' });
  }
});

// Express route to fetch reviews by a particular dealer
app.get('/fetchReviews/dealer/:id', async (req, res) => {
  try {
    const dealerId = parseInt(req.params.id);
    if (useMongo && Reviews) {
      const documents = await Reviews.find({ dealership: req.params.id });
      return res.json(documents);
    }
    const filtered = memoryReviews.filter(r => r.dealership === dealerId || String(r.dealership) === String(req.params.id));
    res.json(filtered);
  } catch (error) {
    res.status(500).json({ error: 'Error fetching documents' });
  }
});

// Express route to fetch all dealerships
app.get('/fetchDealers', async (req, res) => {
  try {
    if (useMongo && Dealerships) {
      const documents = await Dealerships.find();
      return res.json(documents);
    }
    res.json(memoryDealerships);
  } catch (error) {
    res.status(500).json({ error: 'Error fetching documents' });
  }
});

// Express route to fetch Dealers by a particular state
app.get('/fetchDealers/:state', async (req, res) => {
  try {
    const stateParam = req.params.state;
    if (useMongo && Dealerships) {
      const documents = await Dealerships.find({
        state: { $regex: new RegExp(`^${stateParam}$`, 'i') }
      });
      return res.json(documents);
    }
    const filtered = memoryDealerships.filter(d => 
      d.state.toLowerCase() === stateParam.toLowerCase() || 
      (d.st && d.st.toLowerCase() === stateParam.toLowerCase())
    );
    res.json(filtered);
  } catch (error) {
    res.status(500).json({ error: 'Error fetching documents' });
  }
});

// Express route to fetch dealer by a particular id
app.get('/fetchDealer/:id', async (req, res) => {
  try {
    const dealerId = parseInt(req.params.id);
    if (useMongo && Dealerships) {
      const documents = await Dealerships.find({ id: dealerId });
      return res.json(documents);
    }
    const filtered = memoryDealerships.filter(d => d.id === dealerId);
    res.json(filtered);
  } catch (error) {
    res.status(500).json({ error: 'Error fetching documents' });
  }
});

// Express route to insert review
app.post('/insert_review', express.raw({ type: '*/*' }), async (req, res) => {
  try {
    let data;
    if (typeof req.body === 'string') {
      data = JSON.parse(req.body);
    } else if (Buffer.isBuffer(req.body)) {
      data = JSON.parse(req.body.toString('utf8'));
    } else {
      data = req.body;
    }

    let new_id = 1;
    if (useMongo && Reviews) {
      const documents = await Reviews.find().sort({ id: -1 });
      new_id = (documents.length > 0 && documents[0]['id']) ? documents[0]['id'] + 1 : 1;
      const review = new Reviews({
        "id": new_id,
        "name": data['name'],
        "dealership": data['dealership'],
        "review": data['review'],
        "purchase": data['purchase'],
        "purchase_date": data['purchase_date'],
        "car_make": data['car_make'],
        "car_model": data['car_model'],
        "car_year": data['car_year'],
      });
      const savedReview = await review.save();
      return res.json(savedReview);
    } else {
      const maxId = memoryReviews.reduce((max, r) => r.id > max ? r.id : max, 0);
      new_id = maxId + 1;
      const reviewObj = {
        "id": new_id,
        "name": data['name'],
        "dealership": parseInt(data['dealership']),
        "review": data['review'],
        "purchase": data['purchase'],
        "purchase_date": data['purchase_date'],
        "car_make": data['car_make'],
        "car_model": data['car_model'],
        "car_year": data['car_year'],
      };
      memoryReviews.push(reviewObj);
      return res.json(reviewObj);
    }
  } catch (error) {
    console.log(error);
    res.status(500).json({ error: 'Error inserting review' });
  }
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});

const express = require("express");
const fs = require("fs");
const bodyParser = require("body-parser");

const app = express();
const PORT = 3000;

app.use(express.static(__dirname));
app.use(bodyParser.json());

app.post("/save", (req, res) => {
  const { selections } = req.body;

  if (!selections) return res.sendStatus(400);

  const row =
    `${new Date().toISOString()},"${selections.join(",")}"\n`;

  fs.appendFileSync(FILE, row);

  res.sendStatus(200);
});

app.listen(PORT, () =>
  console.log(`Server running at http://localhost:${PORT}`)
);

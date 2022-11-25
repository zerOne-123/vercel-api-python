module.exports = (req, res) => {
  try {
    const { who = 'anonymous' } = req.query;
    res.status(200).send(`Hello ${who}!`);
  } catch (error) {
    res.status(400).json({ error: 'My custom 400 error' });
  }
};

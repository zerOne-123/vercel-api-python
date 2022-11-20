module.exports = (req, res) => {
  try {
    let who = req.query?.who || 'anonymous';
    res.status(200).send(`Hello ${who}!`);
  } catch (error) {
    res.status(400).json({ error: 'My custom 400 error' });
  }
};

export default function handler(req, res) {
  const { name = 'js' } = req.query;
  return res.send(`Hello ${name}!`);
}
const axios = require('axios').default

export default async function handler(req, res) {
  const { name = 'js' } = req.query;
  const html = (await axios.get('https://www.baidu.com')).data
  return res.send(html);
}